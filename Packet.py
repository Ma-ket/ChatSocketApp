class Packet:
    _app = None
    _name = None
    _type = None
    _registered = False
    _comment = None

    def __init__(self, app, put_type=None):
        self._app = app
        self._type = put_type

    def set_packetdata(self, name=None, registered=False, comment=None):
        """ パケットの設定 """
        self._name = self._name if (name is None) else name
        self._registered = registered
        self._comment = comment

    def get_packetdata(self):
        """ パケットの取得 """
        data = {
            "app" : self._app,
            "user_name" :self._name,
            "type" : self._type,
            "registered" : self._registered,
            "comment" : self._comment
        }
        return data
