import sys
import socket
import json
from Packet import Packet
from Server import Server

class Server_Run(Server):
    def __init__(self):
        """ コンストラクタ """
        self.pckt = None
        self.sock = None
        super().__init__()  # 継承元からオーバーライド
        self.user_addrs = dict()  # userのaddrを管理する変数　dict(tuple(clin, list(clouts)))

    def run(self):
        """ 実行 """
        while (True):
            data, client_addr = super().recieve_packet()  # パケットの受信
            try:
                self.analyze(data, client_addr)
                return
            except KeyboardInterrupt:
                super().close("stop program at [run]")

    def analyze(self, data, addr):
        """ 受信したデータを解析、適切に処理を振り分ける """
        if (data["app"] != "client"):
            pass  # 何もしない
        else:
            username = data["username"]
            if (username in self.user_addrs):  # 既に登録されている
                if (data["type"] == "input"):
                    self.type_input(dataa, addr)
                elif (data["type"] == "output"):
                    pass
            pass

    def type_input(self, data, addr):
        if (data["registerd"] == False):  # user名が被った
            self.username_dupplicate(data, addr)
        else:
            comment = data["comment"]

            if (comment == "end" or comment == "logout"):
                self.logout_process(username)

            # chat
            print(f"{username}: {comment}")
            # 出力appが存在するかどうか
            if ((destaddr := self.user_addrs[username][1]) is not None):  # 存在する
                # 出力appに送信
                self.pckt.set_packetdata(name=username, comment=comment)
        pass

    def username_dupplicate(self, data):
        """ 入力appが被ってしまった、入力appは複数存在してはいけないため """
        username = data["username"]
        comment = f"@{username} has already dupplicated."

        # 該当入力appにそのuser名は使えないと伝達
        another_data = super().create_packet(username, comment=comment)
        super().send_packet(another_data, addr)

    def logout_process(self, username):
        username = data["username"]
        comment = "end"
        data = super().create_packet(username, True, comment)

        # addr
        client_addrs = self.user_addrs[username]
        cl_in_addr, cl_out_addrs = client_addrs  # 入力appと出力appに分ける

        # 出力appに終了処理を指示
        for addr in cl_out_addrs:
            super().send_packet(data, addr)

if __name__ == "__main__":
    server = Server_Run()
    server.run()
