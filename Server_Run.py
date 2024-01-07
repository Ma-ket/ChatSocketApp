import sys
import socket
import json
from Packet import Packet
from Server import Server

class Server_Run(Server):
    SIZE = 1024

    def __init__(self):
        """ コンストラクタ """
        self.pckt = None
        self.sock = None
        super().__init__()  # 継承元からオーバーライド

    def run(self):
        while (True):
            # data, client_addr = super.
            print(self.pckt, self.sock)
            return

if __name__ == "__main__":
    server = Server_Run()
    server.run()
