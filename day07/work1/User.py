import time,random
from work1.Address import Address
class User():
    __account = ""
    __username = ""
    __password = ""
    __money = 0.0
    __time = time.asctime(time.localtime(time.time()))
    __bank_name = "中国工商银行昌平支行"

    def getAccount(self):
        li = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
        string = ""
        for i in range(8):
            string = string + li[int(random.random() * len(li))]
        self.__account = string
        return self.__account

    def setUsername(self):
        username = input("请输入姓名：")
        self.__username = username

    def getUsername(self):
        return self.__username

    def setPassword(self):
        password = input("请输入密码：")
        if len(password) > 6:
            print("输入过长")
        else:
            if password.isdigit():
                self.__password = password
            else:
                print("输入非法！")

    def getPassword(self):
        return self.__password

    def setMoney(self):
        money = int(input("请输入余额："))
        if money < 0:
            print("输入非法！")
        else:
            self.__money = money

    def getMoney(self):
        return self.__money

    def getTime(self):
        return self.__time

    def getBank_name(self):
        return self.__bank_name

    def address(self):
        adress = Address()
        adress.setCountry()
        adress.setProvince()
        adress.setStreet()
        adress.setDoor()
        a = adress.getCountry()
        b = adress.getProvince()
        c = adress.getStreet()
        d = adress.getDoor()
        str = a + " " + b + " "  + c + " "  + d
        return str