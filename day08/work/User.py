import time
import random
from work.Address import Address
class User:
    __account = None
    __username = None
    __password = None
    __money = None
    __time = time.asctime(time.localtime(time.time()))
    __address = None
    __bankname = "中国工商银行昌平支行"

    '''def __init__(self,account,username,address,password,money,time,bankname):
        self.__account=account
        self.__username=username
        self.__address=address
        self.__password=password
        self.__bankname=bankname
        self.__money=money
        self.__time=time'''

    def getAccount(self):
        li = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
        string = ""
        for i in range(8):
            string = string + li[int(random.random() * len(li))]
        self.__account = string
        return self.__account

    def setUsername(self,username):
        self.__username=username
    def getUsername(self):
        return self.__username

    '''def setAddress(self,address):
        self.__address=address
    def getAddress(self):
        return self.__address'''

    def setPassword(self,password):
        if len(password) > 6:
            print("输入过长")
        else:
            if password.isdigit():
                self.__password = password
            else:
                print("输入非法！")
    def getPassword(self):
        return self.__password

    def setMoney(self,money):
        if money<0:
            print("输入非法！")
        else:
            self.__money=money
    def getMoney(self):
        return self.__money

    def setTime(self,time):
        self.__time=time
    def getTime(self):
        return self.__time

    def setBankname(self,bankname):
        self.__bankname=bankname
    def getBankname(self):
        return self.__bankname

    def address(self):
        add=Address()
        add.getCountry()
        add.getProvince()
        add.getStreet()
        add.getDoor()
        a=add.getCountry()
        b=add.getProvince()
        c=add.getStreet()
        d=add.getDoor()
        str = a+" "+b+" "+c+" "+d
        return str

    '''def P(self):
        print(
            "账号：",self.__account,
            "姓名：",self.__username,
            "密码：",self.__password,
            "地址：",self.__address,
            "存款余额：",self.__money,
            "注册时间：",self.__time,
            "开户行名称：",self.__bankname
        )'''







