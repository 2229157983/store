#  计算器    14-周俊
num1=float(input("请输入第一个数："))
num2=float(input("请输入第二个数："))
oper=input("请输入运算符：")
list=["+","-","*","/"]
if oper in list:
    if oper==list[0]:
        result=num1+num2
    elif oper==list[1]:
        result = num1-num2
    elif oper==list[2]:
        result=num1*num2
    else:
        result=num1/num2
    print("{}{}{}={}".format(num1,oper,num2,result))
else:
    print("输入的运算符错误！")