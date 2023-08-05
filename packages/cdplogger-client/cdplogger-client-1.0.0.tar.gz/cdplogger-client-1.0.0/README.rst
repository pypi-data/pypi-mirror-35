**CDP-Client**
==============

A simple python interface for the CDP Studio development platform that allows Python scripts to interact with CDP Applications - to access logger data. For more information about CDP Studio see `https://cdpstudio.com/ <https://cdpstudio.com/>`_

The API makes heavy use of promise library for asynchronous operations. For more information see `https://pypi.python.org/pypi/promise <https://pypi.org/project/promise/>`_

**Installation**
----------------

``$ pip install cdplogger-client``


**Usage**
---------

``from cdplogger_client import cdplogger``


``def on_data_points_received(data_points):``
    ``for point in data_points:``
        ``print("Timestamp: " + str(point.timestamp) + "\nMin: " + str(point.value["CDPSignal"].min) + "\nMax: " + str(point.value["CDPSignal"].max) + "\nLast: " + str(point.value["CDPSignal"].last))``

``def request_data_points(limits):``
    ``return client.request_data_points(["CDPSignal"], limits.start_s, limits.end_s, 500)``

``def on_error(e):``
    ``print e``


``client = cdplogger.Client('127.0.0.1')
client.request_log_limits().then(request_data_points).then(on_data_points_received).catch(on_error)
client.run_event_loop())``


**API**
-------

Before all examples, you need:

``from cdplogger_client import cdplogger_client``

**Global API**
**************

Client(host, port, auto_reconnect)

- Arguments

    host - String for hosts ip address
    
    port - Optional port number to connect to. If not specified default port 17000 is used. To find the correct port start the logger application and look at console output. Find something like "14:10:27.832 CDPLogger: Database server started on 127.0.0.1:17000." This will give you the IP and port.

    
    auto_reconnect - Optional argument to enable/disable automatic reconnect when connection is lost. Defaults to True if not specified.

- Returns

    The connected client object.

-     Usage

        ``client = cdplogger_client.Client('127.0.0.1')``

**Instance Methods / Client**
*****************************

**client.request_api_version()**

Gets the api version of the connected application.

    - Returns

        Promise containing api version when fulfilled.

    - Usage

       ``def on_success(version):``
            ``print("\nVersion: " + version)``

       ``client.request_api_version().then(on_success)``


**client.request_logged_nodes()**

Gets the logged nodes from the logger.

    - Returns

        Promise containing a list of nodes with name and routing when fulfilled.

    - Usage

        ``def on_success(nodes):``
            ``for node in nodes:``
                ``print("Name: " + node.name)``
                ``print("Routing in API: "+ node.routing)``

        ``client.request_logged_nodes().then(on_success)``

**client.request_log_limits()**

Criterion limits request that retrieve the limits from the logger.

    - Returns

        Promise containing log limits when fulfilled.

    - Usage

        ``import datetime``

        ``def on_success(limits):``
            ``print("Logging start: " + datetime.datetime.fromtimestamp(int(limits.start_s)).strftime('%Y-%m-%d %H:%M:%S') + "\nLogging end: " + datetime.datetime.fromtimestamp(int(limits.end_s)).strftime('%Y-%m-%d %H:%M:%S'))``

        ``client.request_log_limits().then(on_success)``


**client.request_data_points(node_names, start_s, end_s, no_of_data_points)**

Gets list of data points that contain min, max and last values for selected nodes from the logger.

    - Arguments

        - node_names - list of node names. To find node names:
             - open CDP Studio and look at logged values table in the logger component, or
             - use request_logged_nodes()
        - start_s - timestamp in seconds
        - end_s - timestamp in seconds
        - no_of_data_points - number of data points wanted.
            - For example when plotting data on a graph that is 500 pixels wide, there is no need to request more than 500 data points. Note that implementation may still return a different amount of data points.

    - Returns

        Promise containing a list of data points when fulfilled.

    - Usage

        ``def on_success(data_points):``
             ``for point in data_points:``
                ``print("Timestamp: " + str(point.timestamp) + "\nMin: " + str(point.value["Output"].min) + "\nMax: " + str(point.value["Output"].max) + "\nLast: " + str(point.value["Output"].last))``
     
        ``client.request_data_points(node_names, start_s, end_s, no_of_data_points).then(on_success)``
        
**client.run_event_loop()**

Runs the event loop that serves network communication layer for incoming/outgoing data. **This is a blocking call that must be run for any communication to happen.** The method can be cancelled by calling disconnect.

**client.disconnect()**

Stops the event loop and closes the connection to connected application. This method also releases the blocking run_event_loop call.

Tests
------------------

To run the test suite execute the following command in package root folder:

``$ python setup.py test``

License
------------------

MIT License