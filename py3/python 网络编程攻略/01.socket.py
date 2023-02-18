import socket

host_name = socket.gethostname()
ip = socket.gethostbyname(host_name)
print("主机名：", host_name)
print("IP：", ip)
