from Client import Client
from Packet import Packet

class Client_Output(Client):
    SERVER_ADDR = ("127.0.0.1", 8090)

    def __init__(self):
        """ コンストラクタ """
        super().__init__()
        self.pckt = Packet("client", "output")
        self.my_username = None

    def run(self):
        """ 実行 """
        name = super().input_username()
        self.registration_request(name)
        data, addr = self.wait_recieving_packet()
        self.my_username = name
        pass

    def registration_request(self, name):
        """ 登録の要求、認証 """
        data = super().create_packet(name)
        super().send_packet(data, self.SERVER_ADDR)
        print("#### packetの送信完了 ####")

    def wait_recieving_packet(self):
        """ chatの内容を受信するまで待機する """
        while True:
            data, addr = super().recieve_packet()
            self.analyze(data, addr)

    def analyze(self, data, addr):
        """ 使うかまだわからない """
        if (data["app"] != "server"):
            pass
        else:
            comment = data["comment"]
            if (comment in ["end", "logout"]):
                super().close("end of this program")
            elif (comment is None):
                pass
            else:
                name = data["username"]
                self.chat(name, comment)

    def chat(self, name, comment):
        if (name == self.my_username):
            print(f"me:{name}: {comment}")
        else:
            print(f"notme:{name}: {comment}")


if __name__ == "__main__":
    client = Client_Output()
    client.run()
