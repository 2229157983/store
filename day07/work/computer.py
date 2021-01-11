class Computer():
    __screen=0#屏幕大小
    __price=0#价格
    __cpu=""#cpu型号
    __memsize=0#内存大小
    __hours=0

    def setScreen(self,screen):
        self.__screen=screen
    def getScreen(self):
        return self.__screen

    def setPrice(self,price):
        self.__price=price
    def getPrice(self):
        return self.__price

    def setCpu(self,cpu):
        self.__cpu=cpu
    def getCpu(self):
        return self.__cpu

    def setMemsize(self,memsize):
        self.__memsize=memsize
    def getMemsize(self):
        return self.__memsize

    def setHours(self,hour):
        self.__hours=hour
    def getHours(self):
        return self.__hours

    def typewriting(self):
        print("价格为",self.__price,"的笔记本电脑打了",self.__hours,"小时字！")

    def game(self):
        print("屏幕大小为",self.__screen,"cpu型号为",self.__cpu,"的笔记本电脑打了",self.__hours,"小时游戏！")

    def video(self):
        print("内存大小为",self.__memsize,"的笔记本电脑一直在看视频")