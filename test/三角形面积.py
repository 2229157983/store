# 计算三角形的面积   05-陈晓玲
import math
a=float(input("请输入三角形第一条边："))
b=float(input("请输入三角形第二条边："))
c=float(input("请输入三角形第三条边："))
if a>0 and b>0 and c>0 and a+b>c and a+c>b and b+c>a:
    s=(a+b+c)/2
    area=math.sqrt(s*(s-a)*(s-b)*(s-c))
    print('三角形面积为：',area)
else:
    print('三角形不成立')