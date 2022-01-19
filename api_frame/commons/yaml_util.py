import os

import yaml


#获取项目根目录
def get_object_path():
    return os.path.abspath(os.getcwd().split("commons")[0])

#读取extract.yaml
def read_extract_yaml(key):
    with open(get_object_path()+"/extract.yaml",encoding='utf-8') as f:
        value = yaml.load(f,Loader=yaml.FullLoader)
        return value[key]

#写入extract.yaml
def write_extract_yaml(data):
    with open(get_object_path()+"/extract.yaml",encoding='utf-8',mode="a") as f:
        yaml.dump(data=data,stream=f,allow_unicode=True)

#清空extract.yaml
def clear_extract_yaml():
    with open(get_object_path()+"/extract.yaml",encoding='utf-8',mode="w") as f:
        f.truncate()

#读取config.yaml
def read_config_yaml(one_node,two_node):
    with open(get_object_path()+"/config.yaml",encoding='utf-8') as f:
        value = yaml.load(f,Loader=yaml.FullLoader)
        return value[one_node][two_node]

#读取数据的yaml
def read_data_yaml(yaml_path):
    with open(get_object_path()+yaml_path,encoding='utf-8') as f:
        value = yaml.load(f,Loader=yaml.FullLoader)
        return value