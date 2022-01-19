import base64
import hashlib

from flask import Flask, request

#初始化一个实例
app = Flask(__name__)

#MD5加密
def md5(args):
    return hashlib.md5(str(args).encode('utf-8')).hexdigest()

#Base64加密
def bs64(args):
    return base64.b64encode(str(args).encode("utf-8")).decode(encoding ="utf-8")

#模拟带参数的请求(md5加密的接口)
@app.route('/md5login',methods=['GET','POST'])
def md5login():
    username = request.values.get("username")
    password = request.values.get("password")
    print(username,password)
    if username==md5("admin").upper() and password==md5("123").upper():
        return {"message":"success"}
    else:
        return {"message":"fail"}

#模拟带参数的请求(base64加密的接口)
@app.route('/base64login',methods=['GET','POST'])
def base64login():
    username = request.values.get("username")
    password = request.values.get("password")
    print(username,password)
    print(bs64("admin").upper(),bs64("123").upper())
    print(username==bs64("admin").upper() and password==bs64("123").upper())
    if username==bs64("admin").upper() and password==bs64("123").upper():
        return {"message":"success"}
    else:
        return {"message":"fail"}

if __name__ == '__main__':
    app.run()