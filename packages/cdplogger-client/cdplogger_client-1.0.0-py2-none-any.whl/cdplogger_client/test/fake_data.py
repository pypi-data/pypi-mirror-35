from cdplogger_client import container_pb2
from cdplogger_client import database_pb2
from cdplogger_client import variant_pb2


def create_api_version_response():
    response = container_pb2.Container()
    response.message_type = container_pb2.Container.eVersionResponse
    response.version_response.request_id = 1
    response.version_response.version = "3.0"
    return response


def create_api_version_error_response():
    response = container_pb2.Container()
    response.message_type = container_pb2.Container.eVersionResponse
    response.version_response.request_id = 1
    response.version_response.version = "1.0"
    return response


def create_log_limits_response():
    response = container_pb2.Container()
    response.message_type = container_pb2.Container.eCriterionLimitsResponse
    response.criterion_limits_response.request_id = 1
    response.criterion_limits_response.criterion_min = 1529497537.61
    response.criterion_limits_response.criterion_max = 1531389483.02
    return response


def create_logged_nodes_response(request_id):
    response = container_pb2.Container()
    response.message_type = container_pb2.Container.eSignalInfoResponse
    response.signal_info_response.request_id = request_id
    response.signal_info_response.name.extend(["Output", "CPULoad", "MemUsed", "CDPSignal"])
    response.signal_info_response.id.extend([0, 1, 2, 3])
    response.signal_info_response.type.extend([])
    response.signal_info_response.path.extend(["loggerApp.Sine.Output", "loggerApp.CPULoad", "loggerApp.MemUsed",
                                               "loggerApp.CDPSignal"])
    return response


def create_data_point_response():
    response = container_pb2.Container()
    response.message_type = container_pb2.Container.eSignalDataResponse
    response.signal_data_response.request_id = 1
    response.signal_data_response.row.extend([database_pb2.SignalDataRow(), database_pb2.SignalDataRow()])
    response.signal_data_response.row[0].min_values.extend([variant_pb2.VariantValue(), variant_pb2.VariantValue()])
    response.signal_data_response.row[0].max_values.extend([variant_pb2.VariantValue(), variant_pb2.VariantValue()])
    response.signal_data_response.row[0].last_values.extend([variant_pb2.VariantValue(), variant_pb2.VariantValue()])
    response.signal_data_response.row[1].min_values.extend([variant_pb2.VariantValue(), variant_pb2.VariantValue()])
    response.signal_data_response.row[1].max_values.extend([variant_pb2.VariantValue(), variant_pb2.VariantValue()])
    response.signal_data_response.row[1].last_values.extend([variant_pb2.VariantValue(), variant_pb2.VariantValue()])
    response.signal_data_response.criterion.extend([1531313250.0, 1530613239.063119])
    response.signal_data_response.row[0].signal_id.extend([0, 1])
    response.signal_data_response.row[0].min_values[0].d_value = 0.638855091434
    response.signal_data_response.row[0].max_values[0].d_value = 0.639955091434
    response.signal_data_response.row[0].last_values[0].d_value = 0.638855091434
    response.signal_data_response.row[0].min_values[1].d_value = 0.538855091434
    response.signal_data_response.row[0].max_values[1].d_value = 0.53955091434
    response.signal_data_response.row[0].last_values[1].d_value = 0.538855091434
    response.signal_data_response.row[1].signal_id.extend([0, 1])
    response.signal_data_response.row[1].min_values[0].d_value = 0.738855091434
    response.signal_data_response.row[1].max_values[0].d_value = 0.739955091434
    response.signal_data_response.row[1].last_values[0].d_value = 0.738855091434
    response.signal_data_response.row[1].min_values[1].d_value = 0.338855091434
    response.signal_data_response.row[1].max_values[1].d_value = 0.358855091434
    response.signal_data_response.row[1].last_values[1].d_value = 0.348855091434
    return response


def create_error_response():
    response = container_pb2.Container()
    response.message_type = container_pb2.Container.eError
    response.error.request_id = 1
    response.error.errorMessage = "Error message"
    response.error.errorCode = 1234567
    return response
