class Person:
    __username=""#  __属性：表示私有属性，类外面无法直接看到属性名称
    __age=0
    __sex=""

    def setAge(self,age):
        if age>100 or age<0:
            print("输入的年龄不合法！")
        else:
            self.__age=age
    def getAge(self):
        return self.__age

    def setUsername(self,username):
        self.__username=username
    def getUsername(self):
        return self.__username

    def setSex(self,sex):
        self.__sex=sex
    def getSex(self):
        return self.__sex

    def eat(self):
        print(self.__username,"正在吃饭！")

    def study(self,hour):
        print(self.getUsername(),"正在学习，已经学习了",hour,"小时！")

'''
封装：
1.将属性隐藏：在属性前面加__,用于隐藏属性对外的暴露
2.提供一个方法用于间接赋值
    提供setXxx/getXxx用于赋值和获取数据
    
一个类写到一个文件
'''