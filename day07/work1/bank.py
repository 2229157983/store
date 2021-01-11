from work1.User import User
from work1.Money import Money
from work1.Interface import Interface

def inquire_bank(account, password):
    a = Money()
    database = a.getDatabase()
    if account in database:
        if password == database[account]["password"]:
            info = '''
                            ----------------账户信息----------------
                            账号：{account}
                            姓名：{username}
                            密码：{password}
                            地址信息：{adress}
                            余额：{money}
                            开户行名称：{bank_name}
                            开户时间：{time}
                            ----------------------------------------
                        '''
            print("以下是您的账户信息：")
            print(info.format(account=account,
                              username=database[account]["username"],
                              password=database[account]["password"],
                              adress=database[account]["address"],
                              money=database[account]["money"],
                              bank_name=database[account]["bank_name"],
                              time=database[account]["time"]))
        else:
            print("账号密码错误！")
    else:
        print("账号不存在！")

def inquire():
    account = input("请输入账号：")
    password = input("请输入密码：")
    inquire_bank(account, password)

def move_bank(account, account1, password, money):
    a = Money()
    database = a.getDatabase()
    if account in database:
        if account1 in database:
            if password == database[account]["password"]:
                if money > database[account]["money"]:
                    return 3
                else:
                    database[account]["money"] = database[account]["money"] - money
                    database[account1]["money"] = database[account1]["money"] + money
                    return 0
            else:
                return 2
        else:
            return 1
    else:
        print("账号不存在！")


def move():
    a = Money()
    account = input("请输入账号：")
    password = input("请输入密码：")
    account1 = input("请输入转入账号：")
    money = input("请输入转账金额：")
    while True:
        if money.isdigit():
            money = int(money)
            break
        else:
            print("输入非法重新输入：")
            money = input("请输入转账金额：")
    database = a.getDatabase()
    status = move_bank(account, account1, password, money)
    if status == 1:
        print("输入的转入账号不存在！")
    elif status == 2:
        print("账号密码错误！")
    elif status == 3:
        print("余额不足！")
    else:
        print("转账成功！您的余额为：",database[account]["money"])

def getmoney_bank(account, password):
    a = Money()
    database = a.getDatabase()
    if account in database:
        if password == database[account]["password"]:
            money = input("请输入金额：")
            while True:
                if money.isdigit():
                    money = int(money)
                    break
                else:
                    print("输入非法重新输入：")
                    money = input("请输入金额：")
            if money > database[account]["money"]:
                return 3
            else:
                database[account]["money"] = database[account]["money"] - money
                return 0
        else:
            return 2
    else:
        return 1



def getmoney():
    a = Money()
    account = input("请输入账号：")
    password = input("请输入密码：")
    database = a.getDatabase()
    status = getmoney_bank(account, password)
    if status == 1:
        print("账号不存在！")
    elif status == 2:
        print("账号或密码错误！")
    elif status == 3:
        print("余额不足！")
    else:
        print("取款成功！您的余额为：", database[account]["money"])

def save_bank(account, money):
    a = Money()
    database = a.getDatabase()
    database[account]["money"] = database[account]["money"] + money
    return True

def save():
    a = Money()
    account = input("请输入账号：")
    password = input("请输入密码：")
    database = a.getDatabase()
    if account in database:
        if password == database[account]["password"]:
            money = input("请输入金额：")
            while True:
                if money.isdigit():
                    money = int(money)
                    break
                else:
                    print("输入非法重新输入：")
                    money = input("请输入余额：")
            if save_bank(account, money):
                print("存款成功！您的余额为：",database[account]["money"])
        else:
            print("账号或密码错误！")
    else:
        print("账号不存在！")

def bank_addUser(account, username, password,  money, time, bank, address):
    a = Money()
    database = a.getDatabase()
    if len(database) >= 100:
        return 3
    elif account in database:
        return 2
    else:  # account : {username:username,password:password,.....}
        database[account] = {
            "username": username,
            "password": password,
            "address":address,
            "money": money,
            "bank_name": bank,
            "time":time
        }
        a.setDatabase(database)
        return 1

def addUser():
    a = User()
    b = Money()
    database = b.getDatabase()
    account = a.getAccount()
    a.setUsername()
    username = a.getUsername()
    a.setPassword()
    password = a.getPassword()
    print("下面输入地址：")
    adress = a.address()
    a.setMoney()
    money = a.getMoney()
    time = a.getTime()
    bank = a.getBank_name()
    status = bank_addUser(account, username, password, money, time, bank, adress)
    if status == 3:
        print("对不起，本银行用户库已满，请携带证件到其他银行办理！")
    elif status == 2:
        print("对不起，您的个人信息已存在！请稍后再试！")
    elif status == 1:
        info = '''
                ----------------开户信息----------------
                账号：{account}
                姓名：{username}
                密码：{password}
                地址信息：{adress}
                余额：{money}
                开户行名称：{bank_name}
                开户时间：{time}
                ----------------------------------------
            '''
        print("恭喜！开户成功！一下是您的开户信息：")

        # 获取银行的个人信息
        print(info.format(account=account,
                          username=database[account]["username"],
                          password=database[account]["password"],
                          adress=database[account]["address"],
                          money=database[account]["money"],
                          bank_name=database[account]["bank_name"],
                          time=database[account]["time"]))

while True:
    a = Interface()
    welcome = a.getWelcome()
    print(welcome)
    chose = input("请输入您的选项：")
    if chose == "1":
        addUser()
    elif chose == "2":
        save()
    elif chose == "3":
        getmoney()
    elif chose == "4":
        move()
    elif chose == "5":
        inquire()
    elif chose == "6":
        print("恭喜发财！不送！")
        break
    else:
        print("您输入的选项不存在！")

