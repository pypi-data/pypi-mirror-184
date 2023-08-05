

from jose import JWTError, jwt
import pickle
import requests, os
import uuid
import socket
from .settings import db_path, ALGORITHM, SECRET_KEY
import sqlite3, traceback
import json


'''
LoginDbPath 保存登录表位置参数
UrlDbPath 保存Url表格位置
UserName 为用户名字
Password 为用户密码
OcrTokenTxtPath 为保存OcrToken文件的路径
LoginTokenPath 未保存登录Token文件的路径
'''


class LoginClass:
    def __init__(self, LoginDbPath, UrlDbPath, UserName, Password, OcrTokenTxtPath, LoginTokenPath):
        self.version = "0.1.0"
        # # 默认字体颜色
        self.key = b"rongda518ceshi"
        self.save_code = 0
        # self.defaultUI()
        self.LoginDbPath = LoginDbPath
        self.urldb = UrlDbPath
        self.user_name = UserName
        self.password = Password
        self.OcrTokenTxtPath = OcrTokenTxtPath
        self.LoginTokenPath = LoginTokenPath

    def defaultUI(self):
        if os.path.isfile(self.LoginDbPath):
            conn = sqlite3.connect(self.LoginDbPath)
            cursor = conn.cursor()
            sql = 'select * from user'
            cursor.execute(sql)
            result = cursor.fetchall()[0]
            print(result)

    # 保存账号密码
    def save_password(self):
        if os.path.isfile(self.LoginDbPath):
            os.remove(self.LoginDbPath)
        # if not os.path.exists('./database'):
        #     os.mkdir('./database')
        db_file = self.LoginDbPath
        print(db_file)
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        # cursor.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
        try:
            cursor.execute(
                'create table user(name varchar(255) ,password varchar(260),token varchar(260), isremember int)')
            conn.commit()
            # print('INSERT INTO user (name,password,isremember) values ("{}","{}","{}"); '.format( self.user_name, self.password_Q.text(), self.save_code))
            cursor.execute(
                'INSERT INTO user (name,password,isremember) values ("{}","{}","{}"); '.format(self.user_name,
                                                                                               self.password, 1))
            conn.commit()
            cursor.close()
            conn.close()
        except:
            traceback.print_exc()
            conn.rollback()
            cursor.close()
            conn.close()

    # 获取URL连接
    def get_url(self, urlName):
        conn = sqlite3.connect(self.urldb)
        cursor = conn.cursor()
        sql = "select * from urldb where url_name = '{}'".format(urlName)
        cursor.execute(sql)
        g = cursor.fetchall()
        return g

    # 检查版本的函数
    def checkVersion(self):
        data = {
            "version": self.version
        }
        url = "http://39.107.28.207:10518/user/version"
        response = requests.post(url=url, data=json.dumps(data))

        if response.status_code != 200:
            return (False, "警告", "与服务器连接失败")
        else:
            status_v = response.json()["data"]["status_v"]
            if status_v == "10":
                return (True, "警告", "建议更新最新版本使用")

            if status_v == "1":
                token = response.json()["data"]["OCR_token"]
                self.savetoken(token)
                return (True, "警告", "建议更新最新版本使用")

            elif status_v == "-1":
                return (False, "警告", "版本信息错误")

            elif status_v == "11":
                return (False, "警告", "版本太旧！请更新后继续使用")

            elif status_v == "0":
                token = response.json()["data"]["OCR_token"]
                print("OCRtoken为：",token)
                self.savetoken(token)
                return (True)

            else:
                # QMessageBox.information(self, "警告", "未知情况", QMessageBox.Yes, QMessageBox.Yes)
                # set_btn_en()
                return (False, "警告", "未知情况")

    def savetoken(self, obj):
        f = open(self.OcrTokenTxtPath, "wb")
        pickle.dump(obj, f)
        del obj
        f.close()

    def checkUser(self):
        VersionStatus = self.checkVersion()
        print("这是输出检查版本的返回结果")
        print(VersionStatus)
        LoginStatus = ''
        if VersionStatus == True:
            LoginStatus = self.loginTest()
        elif VersionStatus[0]:
            LoginStatus = self.loginTest()
        self.save_password()
        if LoginStatus != "":
            return LoginStatus, "LoginStatus"
        else:
            return VersionStatus, "VersionStatus"

    def loginTest(self):
        # 获取输入的用户名，密码

        # 本地urldb的位置
        # self.urldb = os.path.join("./database", "url.db")
        if not os.path.exists(self.urldb):
            # set_btn_en()
            return ("警告", "保存Url信息的表不存在", False)
            # QMessageBox.information(self, "警告", "保存Url信息的表不存在", QMessageBox.Yes, QMessageBox.Yes)

        if not self.user_name:
            # set_btn_en()
            return ("警告", "请输入用户名", False)
            # QMessageBox.information(self, "警告", "请输入用户名", QMessageBox.Yes, QMessageBox.Yes)
            # return False

        # 判断密码长度
        if 0 < len(self.password) < 4 or len(self.password) > 16:
            # QMessageBox.information(self, "警告", "密码长度太短！密码为8-18位", QMessageBox.Yes, QMessageBox.Yes)
            # set_btn_en()
            return ("警告", "密码长度太短！密码为8-18位", False)
            # return False

        dbText = self.get_url("login_url")
        if dbText:
            url = dbText[0][1]
            try:
                to_encode = {"pass": self.password}
                self.password = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
            except:
                traceback.print_exc()
            mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
            hostname = socket.gethostname()
            # 获取IP
            ip = socket.gethostbyname(hostname)
            body = {
                "username": self.user_name,
                "password": self.password,
                "mac": mac,
                "ip": ip
            }
            try:
                # print(url)
                response = requests.post(url=url, data=json.dumps(body))
                # print(response)
                print(response.text)

                response = response.json()

            except:
                # QMessageBox.information(self, "警告", "服务器连接超时", QMessageBox.Yes, QMessageBox.Yes)
                # set_btn_en()
                return ("警告", "服务器连接超时", False)
                # return False
        else:
            # QMessageBox.information(self, "警告", "表中无登录的url", QMessageBox.Yes, QMessageBox.Yes)
            # set_btn_en()
            return ("警告", "表中无登录的url", False)
        # print(res)
        # 从数据库中获取用户的密码
        if "code" not in response:
            # QMessageBox.information(self, "警告", "与服务器连接超时", QMessageBox.Yes, QMessageBox.Yes)
            # set_btn_en()
            return ("警告", "与服务器连接超时", False)
        if response["code"] == 100201:
            # QMessageBox.information(self, "警告", "登陆失败", QMessageBox.Yes, QMessageBox.Yes)
            # set_btn_en()
            return ("警告", "登陆失败", False)

        if response["code"] == 100206:
            # QMessageBox.information(self, "警告", "密码错误", QMessageBox.Yes, QMessageBox.Yes)
            # set_btn_en()
            return ("警告", "密码错误", False)

        if response["code"] == 100204:
            # QMessageBox.information(self, "警告", "输入密码错误次数过多，账号暂时锁定，请30min再来登录", QMessageBox.Yes, QMessageBox.Yes)
            # set_btn_en()
            return ("警告", "输入密码错误次数过多，账号暂时锁定，请30min再来登录", False)

        if response["code"] == 100203:
            # QMessageBox.information(self, "警告", "产生token失败", QMessageBox.Yes, QMessageBox.Yes)
            # #set_btn_en()
            return ("警告", "产生token失败", False)

        if response["code"] == 100205:
            # QMessageBox.information(self, "警告", "用户不存在", QMessageBox.Yes, QMessageBox.Yes)
            # #set_btn_en()
            return ("警告", "用户不存在", False)

        if response["code"] == 200:
            token = response["data"]["token"]
            with open(self.LoginTokenPath, "w", encoding="utf8") as f:
                f.write(token)
            return ("登录成功", token, True)
            # self.GomMainWindow(token, self.user_name,self.password)




def LoginFun(LoginDbPath, UrlDbPath, UserName, Password, OcrTokenTxtPath, LoginTokenPath):
    # print("这里是输出文件位置")
    # print(LoginDbPath)
    login = LoginClass(LoginDbPath, UrlDbPath, UserName, Password, OcrTokenTxtPath, LoginTokenPath)
    CheckResult = login.checkUser()
    if CheckResult[0][0] == "登录成功":
        return ("登录成功!")
    else:
        return ("登录失败! 错误信息为：", CheckResult[0][1])







