import os, platform


class Util(object):

    # 判断当前环境为windows或者linux
    @staticmethod
    def get_current_system():
        if platform.system() == "Windows":
            current_system = "windows"
        else:
            current_system = "linux/unix/mac"
        return current_system

    # 根据"=="拆分
    @staticmethod
    def split_data(str_data):
        name, value = str_data.split("==")
        return name, value


util = Util()

if __name__ == '__main__':
    # 演示 示例
    print(util.split_data("id==kw"))
    print(util.get_current_system())




