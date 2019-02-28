import irisnative


def run():
    ip = "localhost"
    port = 51773
    namespace = "USER"
    username = "SuperUser"
    password = "SYS"

    connection = irisnative.createConnection(ip, port, namespace, username, password)
    print("Hello World! You have successfully connected to InterSystems IRIS.")


if __name__ == '__main__':
    run()
