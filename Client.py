import sys
import socket
import json
from Packet import Packet

class Client:
    SIZE = 1024

    def __init__(self):
        self.pckt = Packet("client", None)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def input_username(self):
        """ user名の入力 """
        try:
            username = input(f"user name: ")
            print(username)
            return username
        except KeyboardInterrupt:
            self.close("stop program at [input_username]")

    def input_comment(username):
        try:
            comment = input(f"{username}: ")
            return comment
        except KeyboardInterrupt:
            self.close("stop program at [input_comment]")

    def create_packet(self, username, registered=False, comment=None):
        """ パケットの作成 """
        self.pckt.set_packetdata(username, registered, comment)
        data = self.pckt.get_packetdata()
        return data

    def send_packet(self, data, addr):
        """ パケットの送信 """
        data = json.dumps(data)
        send_len = self.sock.sendto(data.encode('utf-8'), addr)
        print("send the packet completely")
        return send_len

    def recieve_packet(self):
        """ パケットの受信 """
        try:
            data, addr = self.sock.recvfrom(SIZE)
            data = json.loads(data.encode('utf-8'))
            return data, addr
        except KeyboardInterrupt:
            self.close("stop program at [recieve_packet]")

    def close(message=""):
        """ 終了処理 """
        self.sock.close()
        sys.exit(message)




