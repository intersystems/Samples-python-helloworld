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

    # Create iris object
    iris_native = irisnative.createIris(connection)

    # Store data natively into a global
    iris_native.set(8888, "^testglobal", "1")
    global_value = iris_native.get("^testglobal", "1")
    print("The value of ^testglobal(1) is {}".format(global_value))


if __name__ == '__main__':
    run()
