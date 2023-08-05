from cdplogger_client import cdplogger
from . import fake_data
import unittest
import mock
import time


class ClientTester(unittest.TestCase):
    def __init__(self, method_name):
        unittest.TestCase.__init__(self, method_name)
        self._client = None

    def setUp(self):
        self._client = cdplogger.Client('127.0.0.1', 17000, True)
        self._client._last_time_request = time.time() - 11
        self._client._id_to_name = {0: "Output", 1: "CPULoad"}
        self._client._name_to_id = {"Output": 0, "CPULoad": 1}

    def tearDown(self):
        del self._client

    def test_this(self):
        self.assertEquals(True, True)

    @mock.patch.object(cdplogger.Client, 'run_event_loop')
    def test_run_event_loop(self, mock_run_event_loop):
        self._client.run_event_loop()
        mock_run_event_loop.assert_called_once_with()

    @mock.patch.object(cdplogger.websocket.WebSocketApp, 'close')
    @mock.patch.object(cdplogger.Client, '_cleanup_queued_requests')
    def test_disconnect(self, mock_close, mock_cleanup_queued_requests):
        self._client.disconnect()
        mock_close.assert_called_once_with()
        mock_cleanup_queued_requests.assert_called_once_with()

    @mock.patch.object(cdplogger.Client, '_send_time_request')
    def test_time_request(self, mock_send_time_request):
        self._client._is_open = True
        self._client._time_request()
        mock_send_time_request.assert_called_once()

    @mock.patch.object(cdplogger.Client, '_send_time_request')
    @mock.patch.object(cdplogger.Client, '_send_api_version_request')
    def test_version_request_also_sends_time_request(self, mock_send_api_version_request, mock_send_time_request):
        self._client._is_open = True
        self._client.request_api_version()
        mock_send_time_request.assert_called_once_with(0)
        mock_send_api_version_request.assert_called_once_with(1)

    @mock.patch.object(cdplogger.Client, '_send_time_request')
    @mock.patch.object(cdplogger.Client, '_send_log_limits_request')
    def test_log_limits_request_also_sends_time_request(self, mock_send_log_limits_request, mock_send_time_request):
        self._client._is_open = True
        self._client.request_log_limits()
        mock_send_time_request.assert_called_once_with(0)
        mock_send_log_limits_request.assert_called_once_with(1)

    @mock.patch.object(cdplogger.Client, '_send_time_request')
    @mock.patch.object(cdplogger.Client, '_send_logged_nodes_request')
    def test_logged_nodes_request_also_sends_time_request(self, mock_send_logged_nodes_request, mock_send_time_request):
        self._client._is_open = True
        self._client.request_logged_nodes()
        mock_send_time_request.assert_called_once_with(0)
        mock_send_logged_nodes_request.assert_called_once_with(1)

    @mock.patch.object(cdplogger.Client, '_send_time_request')
    @mock.patch.object(cdplogger.Client, '_send_data_points_request')
    def test_data_points_request_also_sends_time_request(self, mock_send_data_points_request, mock_send_time_request):
        self._client._is_open = True
        self._client.request_data_points(["Output", "CPULoad"], 1530613239.0, 1530613270.0, 500)
        mock_send_time_request.assert_called_once_with(0)
        mock_send_data_points_request.assert_called_once_with([0, 1], 1530613239.0, 1530613270.0, 1, 500)

    @mock.patch.object(cdplogger.Client, '_send_time_request')
    @mock.patch.object(cdplogger.Client, '_send_api_version_request')
    def test_version_request(self, mock_send_api_version_request, mock_send_time_request):
        self._client._is_open = True
        result = []
        self._client.request_api_version().then(lambda version: result.append(version))
        self._client._parse_message(fake_data.create_api_version_response().SerializeToString())
        self.assertEquals(len(result), 1)
        self.assertIsNot(result[0], None)
        mock_send_time_request.assert_called_once_with(0)
        mock_send_api_version_request.assert_called_once_with(1)

    @mock.patch.object(cdplogger.Client, '_send_time_request')
    @mock.patch.object(cdplogger.Client, '_send_api_version_request')
    def test_version_request_error(self, mock_send_api_version_request, mock_send_time_request):
        self._client._is_open = True
        result = []
        self._client.request_api_version().then(lambda version: result.append(version))
        self._client._parse_message(fake_data.create_api_version_error_response().SerializeToString())
        self.assertRaises(cdplogger.CommunicationError)
        self.assertEquals(len(result), 0)
        mock_send_time_request.assert_called_once_with(0)
        mock_send_api_version_request.assert_called_once_with(1)

    @mock.patch.object(cdplogger.Client, '_send_time_request')
    @mock.patch.object(cdplogger.Client, '_send_log_limits_request')
    def test_log_limits_request(self, mock_send_log_limits_request, mock_send_time_request):
        self._client._is_open = True
        result = []
        self._client.request_log_limits().then(lambda limits: result.append(limits))
        self._client._parse_message(fake_data.create_log_limits_response().SerializeToString())
        self.assertEquals(len(result), 1)
        self.assertEquals(result[0].start_s, 1529497537.61)
        self.assertEquals(result[0].end_s, 1531389483.02)
        mock_send_time_request.assert_called_once_with(0)
        mock_send_log_limits_request.assert_called_once_with(1)

    @mock.patch.object(cdplogger.Client, '_send_time_request')
    @mock.patch.object(cdplogger.Client, '_send_log_limits_request')
    def test_log_limits_request_with_time_diff(self, mock_send_log_limits_request, mock_send_time_request):
        self._client._time_diff = 10
        self._client._is_open = True
        result = []
        self._client.request_log_limits().then(lambda limits: result.append(limits))
        self._client._parse_message(fake_data.create_log_limits_response().SerializeToString())
        self.assertEquals(len(result), 1)
        self.assertEquals(result[0].start_s, 1529497537.61+10)
        self.assertEquals(result[0].end_s, 1531389483.02+10)
        mock_send_time_request.assert_called_once_with(0)
        mock_send_log_limits_request.assert_called_once_with(1)

    @mock.patch.object(cdplogger.Client, '_send_time_request')
    @mock.patch.object(cdplogger.Client, '_send_logged_nodes_request')
    def test_logged_nodes_request(self, mock_send_logged_nodes_request, mock_send_time_request):
        self._client._is_open = True
        result = []
        self._client.request_logged_nodes().then(lambda nodes: result.append(nodes))
        self._client._parse_message(fake_data.create_logged_nodes_response(1).SerializeToString())
        self.assertEquals(len(result), 1)
        self.assertEquals(result[0][0].name, "Output")
        self.assertEquals(result[0][0].routing, "loggerApp.Sine.Output")
        mock_send_time_request.assert_called_once_with(0)
        mock_send_logged_nodes_request.assert_called_once_with(1)

    @mock.patch.object(cdplogger.Client, '_send_time_request')
    @mock.patch.object(cdplogger.Client, '_send_data_points_request')
    def test_data_points_request(self, mock_send_data_points_request, mock_send_time_request):
        self._client._is_open = True
        result = []
        self._client.request_data_points(["Output", "CPULoad"], 1531313250.0, 1531461231.0, 500).then(
            lambda data_points: result.append(data_points))
        self._client._parse_message(fake_data.create_data_point_response().SerializeToString())
        self.assertEquals(len(result), 1)
        self.assertEquals(result[0][0].timestamp, 1531313250.0)
        self.assertEquals(result[0][0].value["Output"].min, 0.638855091434)
        self.assertEquals(result[0][0].value["Output"].max, 0.639955091434)
        self.assertEquals(result[0][0].value["Output"].last, 0.638855091434)
        mock_send_time_request.assert_called_once_with(0)
        mock_send_data_points_request.assert_called_once_with([0, 1], 1531313250.0, 1531461231.0, 1, 500)

    @mock.patch.object(cdplogger.Client, '_send_time_request')
    @mock.patch.object(cdplogger.Client, '_send_logged_nodes_request')
    def test_data_points_request_error_on_names(self, mock_send_logged_nodes_request, mock_send_time_request):
        self._client._is_open = True
        result = []
        self._client.request_data_points(["Outputt", "CPULoad"], 1531313250.0, 1531461231.0, 500).catch(
            lambda error: result.append(error))
        self._client._parse_message(fake_data.create_logged_nodes_response(2).SerializeToString())
        self.assertEquals(len(result), 1)
        mock_send_time_request.assert_called_once_with(0)
        mock_send_logged_nodes_request.assert_called_once_with(2)
        actual = result[0]
        expected = cdplogger.InvalidRequestError('Node with name Outputt does not exist.')
        self.assertTrue(type(actual) is type(expected) and actual.args == expected.args)

    @mock.patch.object(cdplogger.Client, '_send_time_request')
    @mock.patch.object(cdplogger.Client, '_send_log_limits_request')
    def test_error_response_on_log_limits_request(self, mock_send_log_limits_request, mock_send_time_request):
        self._client._is_open = True
        result = []
        self._client.request_log_limits().catch(lambda error: result.append(error))
        self._client._parse_message(fake_data.create_error_response().SerializeToString())
        self.assertEquals(len(result), 1)
        mock_send_time_request.assert_called_once_with(0)
        mock_send_log_limits_request.assert_called_once_with(1)
        actual = result[0]
        expected = cdplogger.CommunicationError("Error message")
        self.assertTrue(type(actual) is type(expected) and actual.args == expected.args)
