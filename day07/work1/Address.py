class Address():
    __country = ""
    __province = ""
    __street = ""
    __door = ""

    def setCountry(self):
        country = input("国家：")
        self.__country = country

    def getCountry(self):
        return self.__country

    def setProvince(self):
        province = input("省份：")
        self.__province = province

    def getProvince(self):
        return self.__province

    def setStreet(self):
        street = input("街道：")
        self.__street = street

    def getStreet(self):
        return self.__street

    def setDoor(self):
        door = input("门牌号：")
        self.__door = door

    def getDoor(self):
        return self.__door








