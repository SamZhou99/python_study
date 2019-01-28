#!/usr/bin/python
# -*- coding: UTF-8 -*-

# from scapy.all import *

from scapy.sendrecv import sniff
from scapy.utils import wrpcap

# 这里是针对单网卡的机子，多网卡的可以在参数中指定网卡wrpcap("demo.pcap", dpkt)
# dpkt = sniff(count=100)
