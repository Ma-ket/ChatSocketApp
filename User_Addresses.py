import sys

class User_Addresses:
    def __init__(self):
        """ コンストラクタ """
        self.user_dict = dict()
        pass

    def name_exists(self, name):
        """ 辞書に名前があるかどうか """
        if (name in self.user_dict):
            return True
        return False

    def set_addr(self, name, type_input=None, type_output=[]):
        """ addrを登録する """
        tmp_inout = self.user_dict[name]
        tmp_in, tmp_outs = tmp_inout
        if (type_input is not None):
            self.user_dict[name] = (type_input, tmp_outs)
        if (type(type_output) is type(list())):
            tmp_outs = tmp_tuple[1]
            tmp_outs += type_output
            self.user_dict[name] = (tmp_in, tmp_outs)

    def get_addr(self, name, put_type=None):
        """ addrを返す """
        if (put_type is None):
            pass
        elif (put_type == "input"):
            self.put_type_in(name)
            pass
        elif (put_type == "output"):
            self.put_type_out(name)
            pass
        pass

    def put_type_in(self, name):
        """ 入力app側の処理 """
        pass

    def put_type_out(self, name):
        """ 出力app側の処理 """
        pass


