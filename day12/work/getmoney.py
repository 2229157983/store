from work.NotSufficient import NotSufficient
class Getmoney:
    def getmoney(self):
        money=int(input("请输入您要取得金额："))
        if money <= 3000 and money>0:
            print("取款成功！")
        elif money<0:
            print("输入非法！")
        elif money==0:
            print("取款金额不可为0！")
        else:
            raise NotSufficient("余额不足")
g=Getmoney()
try:
    g.getmoney()
except Exception as error:
        print(error)
