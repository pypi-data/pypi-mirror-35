import websocket
from . import container_pb2
from promise import Promise
from time import sleep
from collections import namedtuple
import time


class Client:

    def __init__(self, host, port=17000, auto_reconnect=True):
        self._reqid = -1
        self._auto_reconnect = auto_reconnect
        self._is_open = False
        self._queued_requests = {}
        self._stored_promises = {}
        self._ws = self._connect("ws://" + host + ":" + str(port))
        self._name_to_id = {}
        self._id_to_name = {}
        self._time_diff = 0
        self._time_received = None
        self._last_time_request = time.time()
        self._have_sent_queued_req = False
        self._round_trip_times = {}

    def run_event_loop(self):
        self._ws.run_forever()
        while self._auto_reconnect:
            sleep(1)
            self._ws = self._connect(self._ws.url)
            self._ws.run_forever()

    def disconnect(self):
        self._auto_reconnect = False
        self._cleanup_queued_requests()
        self._is_open = False
        self._ws.close()

    def request_api_version(self):  # eVersionRequest
        self._time_request()
        request_id = self._get_request_id()
        if not self._is_open:
            self._queued_requests[request_id] = "api_version"
        else:
            self._send_api_version_request(request_id)
        stored_promise = Promise()
        self._stored_promises[request_id] = stored_promise
        return stored_promise

    def request_logged_nodes(self):  # eSignalInfoRequest
        self._time_request()
        request_id = self._get_request_id()
        if not self._is_open:
            self._queued_requests[request_id] = "logged_nodes"
        else:
            self._send_logged_nodes_request(request_id)
        stored_promise = Promise()
        self._stored_promises[request_id] = stored_promise
        return stored_promise

    def request_log_limits(self):  # eCriterionLimitsRequest
        self._time_request()
        request_id = self._get_request_id()
        if not self._is_open:
            self._queued_requests[request_id] = "log_limits"
        else:
            self._send_log_limits_request(request_id)
        stored_promise = Promise()
        self._stored_promises[request_id] = stored_promise
        return stored_promise

    def request_data_points(self, node_names, start_s, end_s, no_of_data_points):  # eSignalDataRequest
        self._time_request()
        request_id = self._get_request_id()
        self._stored_promises[request_id] = Promise()
        if not self._is_open:
            self._queued_requests[request_id] = ["node_values", node_names, start_s, end_s, no_of_data_points]
        else:
            self._req_data_points(node_names, start_s, end_s, no_of_data_points, request_id)
        return self._stored_promises[request_id]

    def _connect(self, url):
        return websocket.WebSocketApp(url,
                                      on_message=self._handle_message,
                                      on_error=self._on_error,
                                      on_close=self._on_close,
                                      on_open=self._on_open)

    def _on_open(self, ws):
        self._is_open = True
        self._update_time_diff()
        self._last_time_request = time.time()

    def _on_error(self, error=None):
        if error is None:
            error = UnknownError("Something went wrong")
        if not self._auto_reconnect:
            for promise in self._stored_promises:
                promise.do_reject(error)
            self._stored_promises.clear()
            self._queued_requests.clear()

    def _error_feedback(self, error, request_id):
        self._stored_promises[request_id].do_reject(error)

    def _on_close(self, ws):
        self._is_open = False
        if not self._auto_reconnect:
            self._on_error(ConnectionError("Connection was closed"))

    def _cleanup_queued_requests(self):
        for promise in self._stored_promises:
            self._stored_promises.get(promise).do_reject(ConnectionError("Connection was closed"))
        self._stored_promises.clear()
        self._queued_requests.clear()

    def _handle_message(self, ws, message):
        self._parse_message(message)

    def _parse_message(self, message):
        data = container_pb2.Container()
        data.ParseFromString(message)
        if data.message_type == container_pb2.Container.eError:
            promise = self._stored_promises[data.error.request_id]
            del self._stored_promises[data.error.request_id]
            promise.do_reject(CommunicationError(str(data.error.errorMessage)))

        elif data.message_type == container_pb2.Container.eTimeResponse:  # time_request
            self._time_received = time.time()
            promise = self._stored_promises[data.time_response.request_id]
            del self._stored_promises[data.time_response.request_id]
            promise.do_resolve(data.time_response.timestamp)

        elif data.message_type == container_pb2.Container.eSignalInfoResponse:  # logged_nodes_request
            nodes = []
            self._name_to_id = {}
            self._id_to_name = {}
            Node = namedtuple('Node', 'name, routing')
            for i in range(0, len(data.signal_info_response.name)):
                node = Node(str(data.signal_info_response.name[i]), str(data.signal_info_response.path[i]))
                self._name_to_id[str(data.signal_info_response.name[i])] = data.signal_info_response.id[i]
                self._id_to_name[data.signal_info_response.id[i]] = str(data.signal_info_response.name[i])
                nodes.append(node)
            promise = self._stored_promises[data.signal_info_response.request_id]
            del self._stored_promises[data.signal_info_response.request_id]
            promise.do_resolve(nodes)

        elif data.message_type == container_pb2.Container.eCriterionLimitsResponse:  # log_limits_request
            data.criterion_limits_response.criterion_min = data.criterion_limits_response.criterion_min\
                + self._time_diff
            data.criterion_limits_response.criterion_max = data.criterion_limits_response.criterion_max\
                + self._time_diff
            Limits = namedtuple('Limits', 'start_s, end_s')
            limits = Limits(data.criterion_limits_response.criterion_min, data.criterion_limits_response.criterion_max)
            promise = self._stored_promises[data.criterion_limits_response.request_id]
            del self._stored_promises[data.criterion_limits_response.request_id]
            promise.do_resolve(limits)

        elif data.message_type == container_pb2.Container.eVersionResponse:  # api_version_request
            version = float(data.version_response.version[0])
            if version < 3.0:
                self._stored_promises[data.version_response.request_id].do_reject(CommunicationError(
                    "CDP version needs to be 3.0 or newer."))
            promise = self._stored_promises[data.version_response.request_id]
            del self._stored_promises[data.version_response.request_id]
            promise.do_resolve(data.version_response.version)

        elif data.message_type == container_pb2.Container.eSignalDataResponse:  # node_values_request
            data_points = []
            index = 0
            for r in data.signal_data_response.row:
                data.signal_data_response.criterion[index] = data.signal_data_response.criterion[index]\
                    + self._time_diff
                signal_names = []
                for signal_id in r.signal_id:
                    signal_names.append(self._id_to_name.get(signal_id))
                DataPoint = namedtuple('DataPoint', 'timestamp, value')
                value = self._create_value(signal_names, r.min_values, r.max_values, r.last_values)
                data_point = DataPoint(data.signal_data_response.criterion[index], value)
                data_points.append(data_point)
                index += 1
            promise = self._stored_promises[data.signal_data_response.request_id]
            del self._stored_promises[data.signal_data_response.request_id]
            promise.do_resolve(data_points)

    def _send_queued_requests(self):
        for request_id in self._queued_requests:
            if self._queued_requests.get(request_id) == "logged_nodes":
                self._send_logged_nodes_request(request_id)
            elif self._queued_requests.get(request_id) == "log_limits":
                self._send_log_limits_request(request_id)
            elif self._queued_requests.get(request_id)[0] == "node_values":
                self._req_data_points(self._queued_requests.get(request_id)[1],
                                      self._queued_requests.get(request_id)[2],
                                      self._queued_requests.get(request_id)[3],
                                      self._queued_requests.get(request_id)[4], request_id)
            elif self._queued_requests.get(request_id) == "api_version":
                self._send_api_version_request(request_id)
        self._queued_requests.clear()

    def _get_request_id(self):
        self._reqid += 1
        return self._reqid

    def _time_request(self):
        if time.time() > self._last_time_request + 10:
            self._update_time_diff()

    def _update_time_diff(self):
        request_id = self._get_request_id()
        time_sent = time.time()
        self._request_time(request_id).then(lambda timestamp: self._set_time_diff(timestamp, time_sent)).catch(
            self._stored_promises[request_id].do_reject)

    def _request_time(self, req_id):
        request_id = req_id
        self._last_time_request = time.time()
        self._send_time_request(request_id)
        stored_promise = Promise()
        self._stored_promises[request_id] = stored_promise
        return stored_promise

    def _send_time_request(self, request_id):
        data = container_pb2.Container()
        data.message_type = container_pb2.Container.eTimeRequest
        data.time_request.request_id = request_id
        self._ws.send(data.SerializeToString())

    def _set_time_diff(self, timestamp, time_sent):
        client_time = self._time_received
        round_trip_time = self._time_received - time_sent
        server_time = timestamp/1000000000.0 + round_trip_time/2.0
        time_diff = client_time - server_time  # time_diff in seconds
        self._round_trip_times[round_trip_time] = time_diff
        if len(self._round_trip_times) != 3:
            self._update_time_diff()
        else:
            self._time_diff = self._round_trip_times.get(min(self._round_trip_times.keys()))
            self._round_trip_times = {}
            if self._have_sent_queued_req is False:
                self._send_queued_requests()
                self._have_sent_queued_req = True

    def _send_logged_nodes_request(self, request_id):
        data = container_pb2.Container()
        data.message_type = container_pb2.Container.eSignalInfoRequest
        data.signal_info_request.request_id = request_id
        self._ws.send(data.SerializeToString())

    def _send_log_limits_request(self, request_id):
        data = container_pb2.Container()
        data.message_type = container_pb2.Container.eCriterionLimitsRequest
        data.criterion_limits_request.request_id = request_id
        self._ws.send(data.SerializeToString())

    def _req_data_points(self, node_names, start_s, end_s, no_of_data_points, request_id):
        def _get_data_points(node_ids):
            self._send_data_points_request(node_ids, start_s, end_s, request_id, no_of_data_points)

        def reject(error):
            promise = self._stored_promises[request_id]
            del self._stored_promises[request_id]
            promise.do_reject(error)

        if not end_s < start_s:
            self._request_node_ids(node_names).then(lambda node_ids: _get_data_points(node_ids)).catch(reject)
        else:
            self._error_feedback(InvalidRequestError(
                "InvalidRequestError on node values request: end_s cannot be smaller than start_s"), request_id)

    def _request_node_ids(self, node_names):
        def _parse_ids():
            for name in node_names:
                if name not in self._name_to_id.keys():
                    raise InvalidRequestError("Node with name "+name+" does not exist.")
            return [self._name_to_id.get(name) for name in node_names]

        def _resolver(resolve, reject):
            if all(name in self._name_to_id.keys() for name in node_names):
                resolve(_parse_ids())
            else:
                self.request_logged_nodes().then(lambda nodes: resolve(_parse_ids())).catch(reject)
        return Promise(_resolver)

    def _send_data_points_request(self, node_ids, start_s, end_s, request_id, no_of_data_points):
        data = container_pb2.Container()
        data.message_type = container_pb2.Container.eSignalDataRequest
        data.signal_data_request.request_id = request_id
        data.signal_data_request.signal_id[:] = node_ids
        data.signal_data_request.num_of_datapoints = no_of_data_points
        data.signal_data_request.criterion_min = start_s - self._time_diff
        data.signal_data_request.criterion_max = end_s - self._time_diff
        self._ws.send(data.SerializeToString())

    def _send_api_version_request(self, request_id):
        data = container_pb2.Container()
        data.message_type = container_pb2.Container.eVersionRequest
        data.version_request.request_id = request_id
        self._ws.send(data.SerializeToString())

    def _create_value(self, signal_names, min_values, max_values, last_values):
        value = {}
        Value = namedtuple('Value', 'min, max, last')
        for i in range(len(signal_names)):
            value[signal_names[i]] = Value(self._value_from_variant(min_values[i]), self._value_from_variant(max_values[i]),
                                           self._value_from_variant(last_values[i]))
        return value

    def _value_from_variant(self, value):
            if value.HasField("d_value"):
                return value.d_value
            elif value.HasField("f_value"):
                return value.f_value
            elif value.HasField("ui64_value"):
                return value.ui64_value
            elif value.HasField("i64_value"):
                return value.i64_value
            elif value.HasField("ui_value"):
                return value.ui_value
            elif value.HasField("i_value"):
                return value.i_value
            elif value.HasField("us_value"):
                return value.us_value
            elif value.HasField("s_value"):
                return value.s_value
            elif value.HasField("uc_value"):
                return value.uc_value
            elif value.HasField("c_value"):
                return value.c_value
            elif value.HasField("b_value"):
                return value.b_value
            elif value.HasField("str_value"):
                return value.str_value


class ConnectionError(Exception):
    pass


class CommunicationError(Exception):
    pass


class InvalidRequestError(Exception):
    pass


class UnknownError(Exception):
    pass
