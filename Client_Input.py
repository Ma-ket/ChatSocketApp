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

        self.request_username(name)
        self.response_username()
        pass

    def request_username(self, name):
        """ サーバに名前の重複があるか確認する """
        data = super().create_packet(name)
        super().send_packet(data, SERVER_ADDR)

    def response_username(self):
        while True:
            data, addr = super().recieve_packet()
            if (data["app"] != "server"):
                pass
            else:
                if (data["registered"] == False):
                    comment = data["comment"]
                    super().close(f"error: {comment}")
                else:
                    print("recieved the packet successfully from server!")
                    return 0


if __name__ == "__main__":
    client = Client_Input()
    client.run()
