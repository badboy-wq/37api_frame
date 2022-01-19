import base64
import hashlib
import os
import random
import time
import rsa
import yaml
from commons.requests_util import RequestsUtil
from commons.yaml_util import read_extract_yaml, get_object_path

class Test:

    #获得随机时间
    def get_random_time(self):
        return str(int(time.time()))[1:6]

    # 读取extract.yaml文件中的值
    def read_extract_data(self, key):
        with open(get_object_path() + "/extract.yaml", encoding='utf-8') as f:
            value = yaml.load(f, Loader=yaml.FullLoader)
            return value[key]

    # 读取config.yaml
    def read_config(self, one_node, two_node):
        with open(get_object_path() + "/config.yaml", encoding='utf-8') as f:
            value = yaml.load(f, Loader=yaml.FullLoader)
            return value[one_node][two_node]

    #MD5加密
    def md5(self,args):
        #以指定的编码格式编码字符串
        utf8_str = str(args).encode("utf-8")
        #md5加密（哈希算法）
        md5_str =  hashlib.md5(utf8_str).hexdigest()
        return md5_str.upper()

    # BASE64加密
    def bs64(self, args):
        # 以指定的编码格式编码字符串
        utf8_str = str(args).encode("utf-8")
        # base64加密
        base64_str = base64.b64encode(utf8_str).decode('utf-8')
        return base64_str.upper()

    #RSA双钥加密方式
    #生成公钥和私钥写入到指定的pem文件
    # def create_key(self):
    #     #根据秘钥长度生成公钥和私钥
    #     (public_key,private_key) = rsa.newkeys(1024)
    #     #保存公钥
    #     with open("public.pem","w+") as f:
    #         f.write(public_key.save_pkcs1().decode())
    #     # 保存私钥
    #     with open("private.pem", "w+") as f:
    #         f.write(private_key.save_pkcs1().decode())

    #通过公钥加密
    def public_key_jiami(self,args):
        #导入公钥
        with open("public.pem") as f:
            pubkey = rsa.PublicKey.load_pkcs1(f.read().encode())
        #加密
        byte_str = rsa.encrypt(str(args).encode("utf-8"),pubkey)
        print(byte_str)
        #把二进制转化成字符串格式
        miwen = base64.b64encode(byte_str).decode("utf-8")
        return miwen

    #通过私钥解密
    # def private_key_jiemi(self,args):
    #     # 导入私钥
    #     with open("private.pem") as f:
    #         prikey = rsa.PrivateKey.load_pkcs1(f.read().encode())
    #     #把字符串转换成二进制格式
    #     byte_str = base64.b64decode(args)
    #     #解密
    #     mingwen = rsa.decrypt(byte_str,prikey).decode()
    #     return mingwen

    #Sign签名
    def signs(self,yaml_path):
        last_url = ""
        last_data = {}
        with open(os.getcwd()+yaml_path,encoding='utf-8') as f:
            yaml_value = yaml.load(f,Loader=yaml.FullLoader)
            for caseinfo in yaml_value:
                caseinfo_keys = caseinfo.keys()
                # 判断一级关键字是否包括有:name,request,valiedate
                if "request" in caseinfo_keys:
                    # 判断url
                    if "url" in caseinfo['request'].keys():
                        last_url=caseinfo['request']['url']
                    # 判断参数
                    req = caseinfo['request']
                    for key,value in req.items():
                        if key in ['params','data','json']:
                            for p_key,p_value in req[key].items():
                                last_data[p_key] = p_value
        last_url = last_url[last_url.index("?")+1:len(last_url)]
        #把last_url的字符串格式加到last_data字典
        lis = last_url.split("&")
        for a in lis:
            last_data[a[0:a.index("=")]] = a[a.index("=")+1:len(a)]
        print(last_data)
        #热加载替换
        last_data = RequestsUtil(self).replace_value(last_data)
        print(last_data)
        #字典根据key的asccii码排序
        new_dict = self.dict_asscii_sort(last_data)
        print(new_dict)
        #第二步：(2)把参数名和参数的值用=连接成字符串，多个参数之间用&连接。a=2&b=1&c=3
        new_str = ""
        for key,value in new_dict.items():
            new_str = new_str+key+"="+value+"&"
        print(new_str)
        #第三到第五步
        appid = "wx8a9de038e93f77ab"
        appsecret = "8326fc915928dee3165720c910effb86"
        nonce = str(random.randint(1000000000,9999999999))
        timestamp = str(time.time())
        all_str = appid+appsecret+new_str+nonce+timestamp
        #第六步
        sign_str = self.md5(all_str)
        return sign_str

    def dict_asscii_sort(self,dict_str):
        dict_key = dict(dict_str).keys()
        l = list(dict_key)
        l.sort()
        new_dict = {}
        for key in l:
            new_dict[key] = dict_str[key]
        return new_dict



