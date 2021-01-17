class Money():
    __database={}
    bankname="中国工商银行昌平支行"

    def __init__(self,database):
        self.__database=database

    def setDatabase(self,database):
        self.__database=database

    def getDatabase(self):
        return self.__database