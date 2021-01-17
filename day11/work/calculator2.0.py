class Calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self,Retain):
        return round(self.a + self.b ,Retain)
    def sub(self,Retain):
        return round(self.a - self.b,Retain)
    def mul(self,Retain):
        return round(self.a * self.b,Retain)
    def div(self,Retain):
        return round(self.a / self.b,Retain)

while True:
    get_num1 = input("请输入第一个数字：")
    opera = input("请输入运算符：")
    get_num2 = input("请输入第二个数字：")
    get_retain = input("请输入保留小数位数：")
    num1 = float(get_num1)
    num2 = float(get_num2)
    retain = int(get_retain)
    result = 0.00
    if opera == "+":
        result = Calculator(num1,num2).add(retain)
    elif opera == "-":
        result = Calculator(num1,num2).sub(retain)
    elif opera == "*":
        result = Calculator(num1,num2).mul(retain)
    else:
        result = Calculator(num1,num2).div(retain)
    print("输出结果是：",result)
