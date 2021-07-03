from dan_socket.client import DanClient
import struct

client = DanClient("127.0.0.1", 8888)


@client.event("on_message")
def message_received(message):
    ba = bytearray(message, 'utf-8')
    print("\n")
    print(len(ba), struct.calcsize('!bhih12s'))
	tup = struct.unpack('!bhih12s', ba)
    print(tup, tup[4].decode("utf8"))
    print("\n")
    # print("Received from Server: {}".format(message))


@client.event("on_connection_closed")
def client_closed():
    print("Server disconnected")


client.start()
