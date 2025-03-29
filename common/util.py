import os, platform


class Util(object):

    # 判断当前环境为windows或者linux
    @staticmethod
    def get_root_path():
        if platform.system() == "Windows":
            root_path = "D:\\home\\firefly\\extend"
        else:
            root_path = "/Library/code/"
        return root_path

    # 根据"=="拆分
    @staticmethod
    def split_data(str_data):
        name, value = str_data.split("==")
        return name, value


util_data = Util()

if __name__ == '__main__':
    # 演示 示例
    print(util_data.split_data("id==kw"))




