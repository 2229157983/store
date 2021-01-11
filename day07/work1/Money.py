class Money():
    __database = {}
    bank_name = "中国工商银行昌平支行"

    def getDatabase(self):
        return self.__database

    def setDatabase(self,database):
        self.__database = database