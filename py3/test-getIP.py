from urllib2 import urlopen
import socket
import uuid
import struct

# 內網IP


def get_LAN_IP():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip


# 外網IP
def get_Internet_IP():
    my_ip = urlopen('http://ifconfig.me/ip').read()
    return my_ip


# 設備UUID：1c:1b:0d:aa:15:b2
def get_UUID():
    mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
    return ":".join([mac[e:e+2] for e in range(0, 11, 2)])


# win和liunx的ipconfig
def get_ipconfig():
    '''
    @summary: return the MAC address of the computer
    '''
    import sys
    import os
    mac = None
    if sys.platform == "win32":
        for line in os.popen("ipconfig /all"):
            print line
            if line.lstrip().startswith("Physical Address"):
                mac = line.split(":")[1].strip().replace("-", ":")
                break
    else:
        for line in os.popen("/sbin/ifconfig"):
            if 'Ether' in line:
                mac = line.split()[4]
                break
    return mac


print get_LAN_IP()
print get_Internet_IP()
print get_UUID()
print get_ipconfig()
