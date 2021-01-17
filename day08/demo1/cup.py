'''
高，容积，颜色，材质
能存放液体
类:
    类名：首字母大写
类的标准写法：2.0
    封装 + 构造方法 + get/setxxx方法
构造方法：能快速的构建一个对象
    构造方法的参数（就是所有的属性）
'''
class Cup:
    __high = None
    __contain = None
    __color = None
    __quanlity =  None

    def __init__(self,high,contain,color,quanlity): #  构造方法：帮助我们来快速的构建对象
        print("hello!")
        # print(high,contain,color,quanlity)
        self.__high = high
        self.__contain = contain
        self.__color = color
        self.__quanlity = quanlity

    def setHigh(self,high):
        self.__high = high

    def getHigh(self):
        return self.__high

    def setContain(self,contain):
        self.__contain =  contain

    def getContain(self):
        return self.__contain

    def setColor(self,color):
        self.__color = color

    def getColor(self):
        return self.__color

    def setQuanlity(self,quanlity):
        self.__quanlity = quanlity

    def getQuanlity(self):
        return self.__quanlity

    def saveLiquid(self,quan):
        print(self.__high,"高度的",self.__color,"颜色的杯子能存储",self.__contain,"升的",quan,"水！")

cup = Cup(10,0.5,"颜色","glass")

print(cup.getColor(),cup.getQuanlity(),cup.getContain(),cup.getHigh())








