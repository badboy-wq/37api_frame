import random
import yaml
from commons.yaml_util import get_object_path

class DebugTalk:

    #获得随机数
    def get_random_number(self,min,max):
        rm = random.randint(int(min), int(max))
        return str(rm)

    #读取extract.yaml文件中的值
    def read_extract_data(self,key):
        with open(get_object_path() + "/extract.yaml", encoding='utf-8') as f:
            value = yaml.load(f, Loader=yaml.FullLoader)
            return value[key]

    # 读取config.yaml
    def read_config(self,one_node,two_node):
        with open(get_object_path() + "/config.yaml", encoding='utf-8') as f:
            value = yaml.load(f, Loader=yaml.FullLoader)
            return value[one_node][two_node]