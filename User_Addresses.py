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

    def create_user_dict(self, name):
        """ user_dictの枠を作る """
        type_input = None
        type_output = list()
        self.user_dict[name] = (type_input, type_output)

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
        tmp_inout = self.user_dict[name]
        if (put_type is None):  # 両方
            return tmo_inout
        tmp_in, tmp_outs = tmp_inout
        if (put_type == "input"):  # 入力appのaddrを返す
            return tmp_in
        if (put_type == "output"):  # 出力appのaddrを返す
            return tmp_outs
        return None




