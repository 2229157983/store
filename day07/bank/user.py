class User():
    __account=0
    __name=""
    __password=0
    __num=0
    __time=""
    __address = ""
    __bankname=""

    def setAccount(self,account):
        self.__account=account
    def getAccount(self):
        return self.__account

    def setName(self,name):
        self.__name=name
    def getName(self):
        return self.__name

    def setAddress(self,address):
        self.__address=address
    def getAddress(self):
        return self.__address

    def setPassword(self,password):
        self.__password=password
    def getPassword(self):
        return self.__password

    def setNum(self,num):
        self.__num=num
    def getNum(self):
        return self.__num

    def setTime(self,time):
        self.__time=time
    def getTime(self):
        return self.__time

    def setBankname(self,bankname):
        self.__bankname=bankname
    def getBankname(self):
        return self.__bankname

    def P(self):
        print(
            "账号：",self.__account,
            "姓名：",self.__name,
            "密码：",self.__password,
            "地址：",self.__address.getCountry(),self.__address.getProvince(),self.__address.getStreet(),self.__address.getDoor(),
            "存款余额：",self.__num,
            "注册时间：",self.__time,
            "开户行名称：",self.__bankname
        )
