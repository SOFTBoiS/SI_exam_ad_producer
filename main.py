import logging
import py_eureka_client.eureka_client as eureka_client

your_rest_server_port = 5000
eureka_client.init(eureka_server="http://localhost:8761/",
                                app_name="python_module_1",
                                instance_port=your_rest_server_port)
logging.basicConfig()
