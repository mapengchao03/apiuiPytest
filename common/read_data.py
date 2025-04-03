import os, json, csv, yaml
from config import config


class ReadData(object):

    # 读取csv文件并转化为字典列表（csv文件需要有表头）
    # 需要入参 "csv文件全名"
    @staticmethod
    def read_csv(test_file):
        data = []
        csv_file = os.path.join(config.root_path, test_file)
        try:
            with open(csv_file, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                data = list(reader)
        except Exception as e:
            print(f"文件{csv_file},读取csv文件错误信息：{repr(e)}")
        finally:
            return data

    # 读取json文件
    # 需要入参 "json文件全名"
    @staticmethod
    def read_json(test_file):
        data = []
        json_file = os.path.join(config.root_path, test_file)
        try:
            with open(json_file, 'r', encoding='utf-8') as file:
                data = json.load(file)
        except Exception as e:
            print(f"文件{json_file},读取json文件错误信息：{repr(e)}")
        finally:
            return data

    # 读取yaml文件
    # 需要入参 "yaml文件全名"
    @staticmethod
    def read_yaml(test_file):
        data = []
        yaml_file = os.path.join(config.root_path, test_file)
        try:
            with open(yaml_file, 'r', encoding='utf-8') as file:
                data = yaml.safe_load(file)
        except Exception as e:
            print(f"文件{yaml_file},读取yaml文件错误信息：{repr(e)}")
        finally:
            return data

read_data = ReadData()

if __name__ == '__main__':
    # 演示 示例baidu_demo
    print(read_data.read_csv("data/ui/baidu_demo/test.csv"))
    for i in read_data.read_csv("data/ui/baidu_demo/test.csv"):
        print(i)
    print(read_data.read_yaml("data/ui/baidu_demo/test.yaml"))
    for k in read_data.read_yaml("data/ui/baidu_demo/test.yaml"):
        print(k)
    print(read_data.read_json("data/ui/baidu_demo/test.json"))
    print(type(read_data.read_json("data/ui/baidu_demo/test.json")))
    for i in read_data.read_json("data/ui/baidu_demo/test.json"):
        print(i)








