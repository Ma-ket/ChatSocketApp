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
        self.confirm_username_to_server(name)
        pass

    def confirm_username_to_server(name):
        """ サーバに名前の重複があるか確認する """
        self.request_username(name)
        self.recieve_response_username()

    def request_username(self, name):
        """ サーバに名前の重複があるかの問い合わせ """
        data = super().create_packet(name, False)
        super().send_packet(data, SERVER_ADDR)

    def recieve_response_username(self):
        """ サーバから名前の重複があるかの結果を受け取る """
        while True:
            data, addr = super().recieve_packet()
            if (data["app"] != "server"):
                continue  # 何もしない
            else:
                if (data["registered"] == False):
                    comment = data["comment"]
                    super().close(f"error: {comment}")
                else:
                    print("recieved the packet successfully from server!")
                    return

    def post_to_chat(self, name):
        comment = super().input_comment(name)
        if (comment == "end" or comment == "logout"):
            super().close("end this program.")
        else:
            data = super().create_packet(name, True, comment)
            super().send_packet(data, SERVER_ADDR)
            print("#### packetの送信完了 ####")

if __name__ == "__main__":
    client = Client_Input()
    client.run()
