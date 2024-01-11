import sys
import socket
import json
from Packet import Packet
from Server import Server
from User_Addresses import User_Addresses

class Server_Run(Server):
    def __init__(self):
        """ コンストラクタ """
        self.pckt = None
        self.sock = None
        super().__init__()  # 継承元からオーバーライド
        self.user_addr = User_Addresses()

    def run(self):
        """ 実行 """
        while (True):
            data, client_addr = super().recieve_packet()  # パケットの受信
            try:
                self.analyze(data, client_addr)
                return  # debug
            except KeyboardInterrupt:
                super().close("stop program at [run]")

    def analyze(self, data, addr):
        """ 受信したデータを解析、適切に処理を振り分ける """
        if (data["app"] != "client"):
            pass  # 何もしない
        else:
            username = data["username"]
            put_type = data["type"]
            if (self.user_addr.name_exists(username)):  # 既に登録されている
                if (put_type == "input"):
                    self.type_input(data)
                    pass
                elif (put_type == "output"):
                    pass
            else:
                # 新規登録
                self.new_registation(username, addr, put_type)
                pass

    def type_input(self, data):
        """ 入力app側の処理 """
        username = data["username"]
        if (data["registerd"] == False):  # user名が被った
            self.username_dupplicate(username)
        else:
            comment = data["comment"]

            if (comment == "end" or comment == "logout"):
                self.logout_process(username)
                return

            # chat
            print(f"{username}: {comment}")
            pass

    def username_dupplicate(self, name):
        """ 入力appが被ってしまった、入力appは複数存在してはいけないため """
        comment = f"@{name} has already dupplicated."
        addr = self.user_addr(name)

        # 該当入力appにそのuser名は使えないと伝達
        another_data = super().create_packet(name, comment=comment)
        super().send_packet(another_data, addr)

    def logout_process(self, username):
        comment = "end"
        data = super().create_packet(username, True, comment)

        # addr
        client_addrs = self.user_addrs[username]
        cl_in_addr, cl_out_addrs = client_addrs  # 入力appと出力appに分ける

        # 出力appに終了処理を指示
        for addr in cl_out_addrs:
            super().send_packet(data, addr)

    def new_registation(self, name, addr, put_type):
        self.user_addr.create_user_dict(name)
        if (put_type == "input"):
            self.user_addr.set_addr(name, type_input=addr)
        elif (put_type == "output"):
            self.user_addr.set_addr(name, type_output=addr)

if __name__ == "__main__":
    server = Server_Run()
    server.run()
