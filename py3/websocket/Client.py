import websocket
import time


def init():
    ws = websocket.WebSocket()
    ws.connect("ws://localhost:8090/wschat")

    msg = ws.recv()
    print(msg)

    time.sleep(1)
    msg = "Hello, Server, " + msg
    print(msg)
    ws.send(msg)

    time.sleep(1)
    msg = ws.recv()
    print(msg)

    ws.close()
    time.sleep(1)


for i in range(9):
    init()
