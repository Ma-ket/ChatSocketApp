from Client import Client
from Packet import Packet

class Client_Output(Client):
    SERVER_ADDR = ("127.0.0.1", 8090)

    def __init__(self):
        """ コンストラクタ """
        super().__init__()
        self.pckt = Packet("client", "output")

    def run(self):
        """ 実行 """
        name = super().input_username()
        self.registration_request(name)
        pass

    def registration_request(self, name):
        """ 登録の要求、認証 """
        data = super().create_packet(name)
        super().send_packet(data, SERVER_ADDR)
        print("#### packetの送信完了 ####")


if __name__ == "__main__":
    client = Client_Output()
    client.run()
