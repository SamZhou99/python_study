# https://pypi.org/project/websocket_client/
import websocket

TOKEN = "cm754e9r01qjend3k6v0cm754e9r01qjend3k6vg"


def on_message(ws, message):
    print(message)


def on_error(ws, error):
    print(error)


def on_close(ws):
    print("### closed ###")


def on_open(ws):
    ws.send('{"type":"subscribe","symbol":"AAPL"}')
    ws.send('{"type":"subscribe","symbol":"AMZN"}')
    ws.send('{"type":"subscribe","symbol":"BINANCE:BTCUSDT"}')
    ws.send('{"type":"subscribe","symbol":"IC MARKETS:1"}')


def initWebSocket_1():
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(
        "wss://ws.finnhub.io?token=" + TOKEN,
        on_message=on_message,
        on_error=on_error,
        on_close=on_close,
    )
    ws.on_open = on_open
    ws.run_forever()


def initWebSocket_2():
    ws = websocket.WebSocket()
    ws.connect("wss://ws.finnhub.io?token=" + TOKEN)
    ws.on_open = on_open
    ws.on_message = on_message
    ws.on_error = on_error
    ws.on_close = on_close
    msg = ws.recv()
    print(msg)


if __name__ == "__main__":
    # initWebSocket_1()
    initWebSocket_2()
