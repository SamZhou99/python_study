# import socket
# # import time


# HOST = '127.0.0.1'
# POST = 8989

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind((HOST, POST))
# s.listen(1)

# while True:
#     conn, addr = s.accept()
#     print('客户端已链接 {}'.format(addr))
#     while True:
#         data = conn.recv(1024)
#         conn.sendall(data)
#         # break
#     # conn.close()
#     # break

# # s.close()



from dan_socket.server import DanServer


server = DanServer("127.0.0.1", 8888)

@server.event("on_message")
def message_received(client, message):
    print("Client {}: {}".format(client, message))

@server.event("on_new_connection")
def new_connection(client):
    print("[NEW] Client {}".format(client))
    client.send("HI\r\n")
    
@server.event("on_connection_closed")
def client_closed(client):
    print("[CLOSED] Client {}".format(client))


server.start()