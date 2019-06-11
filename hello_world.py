"""
PURPOSE: Makes a connection to an instance of InterSystems IRIS Data Platform.
This example also stores data natively into your instance of InterSystems IRIS.
"""


import irisnative


def run():
    # Credentials to connect to InterSystems IRIS database
    ip = "localhost"
    port = 51773
    namespace = "USER"
    username = "SuperUser"
    password = "SYS"

    # Make connection to InterSystems IRIS database
    connection = irisnative.createConnection(ip, port, namespace, username, password)
    print("Hello World! You have successfully connected to InterSystems IRIS.")

    # Create an InterSystems IRIS native object
    iris_native = irisnative.createIris(connection)

    # Store data natively into a global using the InterSystems IRIS native object
    iris_native.set(8888, "^testglobal", "1")
    global_value = iris_native.get("^testglobal", "1")
    print("The value of ^testglobal(1) is {}".format(global_value))


if __name__ == '__main__':
    run()
