from LocalHost import LocalHost


def startLocalhost():
    host = LocalHost(6789)
    host.Route()
    host.Run()
    print("host starting")


startLocalhost()
