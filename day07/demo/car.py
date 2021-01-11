class Car:#车这个类
    __num=0#轮胎属性
    __color=""#车身颜色属性
    __brand=""#车品牌属性

    def setNum(self,num):
        self.__num=num
    def getNum(self):
        return self.__num

    def setColor(self,color):
        self.__color=color
    def getColor(self):
        return self.__color

    def setBrand(self,brand):
        self.__brand=brand
    def getBrand(self):
        return self.__brand

    def run(self):#跑
        print(self.__color,"颜色的车，有",self.__num,"个轮子在大马路上跑")

    def push(self):
        print(self.__color, "颜色的车已经拉了50吨的货！！！")

'''#造车：创建对象
c=Car()
#给车添加属性，给属性赋值
c.run()
c.push()
#修改属性
c.num=5
c.run()'''