name=input("请输入您的名字：")
ID = input("请输入您的身份证号：")
age=input("请输入您的年龄：")
sex=input("请输入您的性别：")
high=input("请输入您的身高：")
weight=input("请输入您的体重：")

info='''
-------------------个人信息---------------
姓名：{name}
身份证号：{ID}
年龄：{age}岁
性别：{sex}
身高：{high}cm
体重：{weight}kg
------------------------------------------
'''
print(info.format(name=name,ID=ID,age=age,sex=sex,high=high,weight=weight ))