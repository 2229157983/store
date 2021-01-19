from work.AgeException import AgeException
class Person:
    __age=None

    def __init__(self,age):
        self.__age=age

    def setAge(self,age):
        self.__age=age
    def getAge(self):
        return self.__age

    def age(self,age):
        if age.isdigit():
            age=int(age)
            print("年龄为：",age)
        else:
            raise AgeException("输入非法！")


try:
    p=Person(12)
    p.age("cxx")
except Exception as error:
    print(error)
