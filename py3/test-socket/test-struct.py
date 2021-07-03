import struct

byte_fmt = '!ci'

print(struct.calcsize(byte_fmt))
buff = struct.pack(byte_fmt, 1, 9)
print(len(buff))
un_buff = struct.unpack(byte_fmt, buff)

print(buff)
# print(int.from_bytes(un_buff[0],'big'))
