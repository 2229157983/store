import random
shop=[
    ["IPhone 8p",1000],
    ["Mac loptop",12000],
    ["IWatch",500],
    ["lenovo PC",4000],
    ["辣条",10],
    ["洗衣粉",23.5]
]
#1.展示商城商品
'''for item,value in enumerate(shop):   #枚举enumerate(shop)
   # print(item,value)'''

def showShop():
    for index,value  in enumerate(shop):
        print(index,value)
#2.让用户输入自己的薪资
while True:
    salary=input("请初始化您的薪资：")
    if salary.isdigit():
        salary=int(salary)
        break
    else:
        print("请输入合适的薪资！")

mycart=[]
sum=0
total=0
#3.开始购物
while True:
    #3.1先展示商品
    print("------------------欢迎来到购物商城---------------------")
    showShop()
    print("-------------------------------------------")
    #3.2 请输入要买的商品的编号

    chose=input("请输入您要买的商品编号：")
    if chose.isdigit():#判断输入的是否为数字
        chose=int(chose)
        if chose>=len(shop):
            print("\033[41;20;1m您输入的商品不存在！\033[0m")
        else:
            if salary<shop[chose][1]:#如果钱不够
                print("\033[41;20;1m余额不足！\033[0m按Q退出")
            else:#正常买东西，添加到我的购物车，薪资减去相对应的商品金钱
                mycart.append(shop[chose])
                salary=salary-shop[chose][1]
                sum=sum+shop[chose][1]
                print("\033[32;20;1m购买成功，您的余额为：",salary,"\033[0m")
    elif chose=="Q"or chose=="q":
        break
    else:
        print("您的输入不合法！请重新输入")
if sum>=0 and sum<=5000:
    total=total+200
else:
    total=total+400
choice=["满1000减200", "满4000减800", "满10000减1800"]
print("-------------------欢迎下次光临--------------------")
print("您购买的商品有:")
for item in mycart:
    print(item)
#print("您的余额为：",salary)
print("您的优惠券为：",random.choice(choice))
dis=0
if random.choice(choice)=="满1000减200":
    dis=200
elif random.choice(choice)=="满4000减800":
    dis=800
elif random.choice(choice)=="满10000减1800":
    dis=1800
print("您本次消费金额为：",sum)
if sum>=dis:
    money=sum-dis
else:
    money=sum
print("您的应付金额为：",money)
print("您本次积分为：",total)



