class Chef:
    __name = None
    __age = None

    def setName(self,name):
        self.__name = name

    def getName(self):
        return self.__name

    def setAge(self,age):
        self.__age = age

    def getAge(self):
        return self.__age

class Son(Chef):
    def cook(self):
        print(super().getName(),"在蒸饭！")

son=Son()
son.setName("李四")
son.cook()

class Sonn(Son):
    def cook(self):
        print(super().getAge(), "岁的", super().getName(), "在炒菜！")

sonn = Sonn()
sonn.setName("张三")
sonn.setAge(50)
print(sonn.getName())
print(sonn.getAge())
sonn.cook()