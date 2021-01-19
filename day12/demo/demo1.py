li=[5,8,4,2,1,0,3]
def getNum(li,index):
    if index>=len(li):
        raise ArithmeticError("角标超出范围了")
    else:
        return li[index]

try:
    n=getNum(li,9)
    print(n)
except IndexError:
    print("您输入的角标不存在")
except IndentationError:
    print("其他异常")
except ArithmeticError:
    print("算术错误")
except Exception:
    print("父类异常")