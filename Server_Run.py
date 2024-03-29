from Server import Server

class Server_Run(Server):
    def __init__(self):
        """ コンストラクタ """
        self.user_addr = None
        super().__init__()  # 継承元からオーバーライド

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
                    self.type_input(data, addr)
                elif (put_type == "output"):
                    self.type_output(data, addr)
            else:
                # 新規登録
                self.new_registration(username, addr, put_type)
                pass

    def type_input(self, data, addr):
        """ 入力app側の処理 """
        if (data["registerd"] == False):  # user名が被った
            self.username_dupplicate(data, addr)
            return
        name = data["username"]
        comment = data["comment"]
        if (comment == "end" or comment == "logout"):
            super().logout_process(name)
            return
        # chat
        self.chat(name, comment)

        # 出力appにchatの内容を反映する
        for dest_addr in self.user_addr.get_addr(name, "output"):
            data = super().create_packet(name, True, comment)
            super().send_packet(data, dest_addr)

    def username_dupplicate(self, name):
        """ 入力appが被ってしまった、入力appは複数存在してはいけないため """
        comment = f"@{name} has already dupplicated."
        addr = self.user_addr(name)

        # 該当入力appにそのuser名は使えないと伝達
        another_data = super().create_packet(name, comment=comment)
        super().send_packet(another_data, addr)

    def chat(name, comment):
        """ chat """
        print(f"{name}: {comment}")

    def type_output(self, data, addr):
        """ 出力app側の処理 """
        name = data["username"]
        if (data["registerd"] == False):
            self.user_addr.set_addr(name, type_output=addr)
            print(f"@{name}'s input/output are connected.")
        else:
            pass  # 何もしない

    def new_registration(self, name, addr, put_type):
        """ userの新規登録 """
        self.user_addr.create_user_dict(name)
        if (put_type == "input"):
            self.user_addr.set_addr(name, type_input=addr)
            print(f"@{name} login as input app.")
        elif (put_type == "output"):
            self.user_addr.set_addr(name, type_output=addr)
            print(f"@{name} login as output app.")

if __name__ == "__main__":
    server = Server_Run()
    server.run()
