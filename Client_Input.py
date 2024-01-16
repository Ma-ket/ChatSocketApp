import sys
import json
from Client import Client
from Packet import Packet

class Client_Input(Client):
    SERVER_ADDR = ("127.0.0.1", 8090)
    
    def __init__(self):
        """ コンストラクタ """
        super().__init__()
        self.pckt = Packet("client", "input")

    def run(self):
        """ 実行 """
        name = super().input_username()
        print(name)
        pass
        
    def request_username(self, name):
        """ サーバに名前の重複があるか確認する """
        pass



if __name__ == "__main__":
    client = Client_Input()
    client.run()
