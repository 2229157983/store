import random
#让系统产生一个随机数
num=int(random.random()*100)#0-100
i=0#游戏的计数器
while True:#让用户无限次的猜
    a=int(input("请输入您猜的数："))#输入猜的数字
    i=i+1
    if a>num:#判断猜的数字与随机数的大小关系
        print("大了！")
    elif a<num:
        print("小了！")
    else:
        print("恭喜，猜中了，本次随机数为：",num,"您本次猜了",i,"次")
        break#跳出循环
