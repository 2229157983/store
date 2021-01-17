class Person:
    age=None
    name=None
    sex=None
class Worker(Person):
    def work(self):
        print(self.name,"在城南工地干活")

'''work=Worker()
work.name="李四"
work.work()'''

class Student(Person):
    id=None
    def study(self):
        print("学号为",self.id,"的",self.name,"正在学习！")


class Sing(Person):
    def sing(self):
        print(self.name,"正在唱歌！")


s=Student()
s.name="小红"
s.id="55555"
s.study()

c=Sing()
c.name="小刚"
c.sing()

