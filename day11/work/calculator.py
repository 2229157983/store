class Calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2

open='''
*****************************
*         计算器            *
*****************************
*1.加法运算                 *
*2.减法运算                 *
*3.乘法运算                 *
*4.除法运算                 *
*5.退出                     *
*****************************
'''
#加
def add():
    num1=input("请输入第一个数:")
    num2=input("请输入第二个数：")
    while True:
        if num1.isdigit() and num2.isdigit():
            num1 = int(num1)
            num2 = int(num2)
            break
        else:
            print("输入非法!请重新输入：")
            num1 = input("请输入第一个数:")
            num2 = input("请输入第二个数：")
    result=num1+num2
    print(num1,"+",num2,"=",result)
#减
def sub():
    num1 = input("请输入第一个数:")
    num2 = input("请输入第二个数：")
    while True:
        if num1.isdigit() and num2.isdigit():
            num1 = int(num1)
            num2 = int(num2)
            break
        else:
            print("输入非法!请重新输入：")
            num1 = input("请输入第一个数:")
            num2 = input("请输入第二个数：")
    result=num1-num2
    print(num1,"-",num2,"=",result)

#乘
def mul():
    num1 = input("请输入第一个数:")
    num2 = input("请输入第二个数：")
    while True:
        if num1.isdigit() and num2.isdigit():
            num1 = int(num1)
            num2 = int(num2)
            break
        else:
            print("输入非法!请重新输入：")
            num1 = input("请输入第一个数:")
            num2 = input("请输入第二个数：")
    result=num1*num2
    print(num1,"*",num2,"=",result)

#除
def div():
    num1 = input("请输入第一个数:")
    num2 = input("请输入第二个数：")
    if num1=='0':
            print("被除数不能为0")
    else:
        while True:
            if num1.isdigit() and num2.isdigit():
                num1 = int(num1)
                num2 = int(num2)
                break
            else:
                print("输入非法!请重新输入：")
                num1 = input("请输入第一个数:")
                num2 = input("请输入第二个数：")
        result = num1 / num2
        print(num1, "/", num2, "=", result)


while True:
    print(open)
    chose=input("请选择您要进行的运算：")
    if chose=='1':
        add()
    elif chose=='2':
        sub()
    elif chose=='3':
        mul()
    elif chose=='4':
        div()
    elif chose=='5':
        print("谢谢使用！")
        break
    else:
        print("您选择的运算暂未开发！")
