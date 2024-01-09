import sys
import socket
import json
from Packet import Packet

class Server:
    SIZE = 1024

    def __init__(self):
        """ コンストラクタ """
        localaddr = ("127.0.0.1", 8090)
        self.pckt = Packet(app="server")
        self.sock = socket.socket(socket.AF_INET, type=socket.SOCK_DGRAM)
        self.sock.bind(localaddr)
        print(f"server addr: {localaddr[0]}, port: {localaddr[1]}")

    def run(self):
        """ 実行 """
        pass

    def analyze(self, data, addr):
        """ 受信したデータを解析、適切に処理を振り分ける """
        pass

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
            data, client_addr = self.sock.recvfrom(self.SIZE)
            data = json.loads(data.encode('utf-8'))
            return data, client_addr
        except KeyboardInterrupt:
            self.close("stop program at [recieve_packet]")

    def close(message=""):
        """ 終了処理 """
        self.sock.close()
        sys.exit(message)

if __name__ == "__main__":
    server = Server()
    server.run()
