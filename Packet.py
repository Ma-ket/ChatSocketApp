class Packet:
    def __init__(self, app, put_type=None):
        """ コンストラクタ """
        self.app = app
        self.type = put_type

    def set_packetdata(self, name=None, registered=False, comment=None):
        """ パケットの設定 """
        self.name = self.name if (name is None) else name
        self.registered = registered
        self.comment = comment

    def get_packetdata(self):
        """ パケットの取得 """
        data = {
            "app" : self.app,
            "username" :self.name,
            "type" : self.type,
            "registered" : self.registered,
            "comment" : self.comment
        }
        return data

if __name__ == "__main__":
    p = Packet("client", "input")
    print(p)
