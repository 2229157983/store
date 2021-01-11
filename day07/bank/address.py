class Address:
    __country=""
    __province=""
    __street=""
    __door=""

    def setCountry(self,country):
        self.__country=country
    def getCountry(self):
        return self.__country

    def setProvince(self,provice):
        self.__province=provice
    def getProvince(self):
        return self.__province

    def setStreet(self,street):
        self.__street=street
    def getStreet(self):
        return self.__street

    def setDoor(self,door):
        self.__door=door
    def getDoor(self):
        return self.__door

    def p(self):
        print(self.__country,self.__province,self.__street,self.__door)