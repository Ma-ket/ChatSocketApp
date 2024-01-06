import sys
import socket
import json
from Packet import Packet

class Client:
    self._pckt = None
    self._sock = None

    def __init__(self):
        self._pckt = Packet("client", None)
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def input_username(pckt):
        """ user名の入力 """
        user_name = input(f"user name: ")
        print(user_name)
        return user_name

    def create_packet(self, username, registered=False, comment=None):
        """ パケットの作成 """
        self._pckt.set_packetdata(username, registered, comment)
        data = self._pckt.get_packetdata()
        return data

    def send_packet(self, data, addr):
        """ パケットの送信 """
        data = json.dumps(data)
        send_len = self._sock.sendto(data.encode('utf-8'), addr)
        return send_len

    def recieve_packet(self, size):
        data, addr = self._sock.recvfrom(size)
        data = json.loads(data.encode('utf-8'))
        return data, addr

    def close(commnet=""):
        """ 終了処理 """
        self._sock.close()
        sys.exit(commnet)




