class Cup:
    __high=0
    __cupbage=0
    __color=""
    __texture=""

    def setHigh(self,high):
        if high<=0:
            print("高度不能小于等于0！")
        else:
            self.__high=high
    def getHigh(self):
        return self.__high

    def setCupbage(self,cupbage):
        if cupbage<=0:
            print("容积不能小于等于0！")
        else:
            self.__cupbage=cupbage
    def getCupbage(self):
        return self.__cupbage

    def setColor(self,color):
        self.__color=color
    def getColor(self):
        return self.__color

    def setTexture(self,texture):
        self.__texture=texture
    def getTexture(self):
        return self.__texture

    def deposit(self):
        print("高为",self.__high,"容积为",self.__cupbage,"的",self.__color,"杯子存放着液体")

