# 10-赵成
username = input("请输入用户名:")
password = input("请输入密码:")
if username[0]!="_":
    print("输入的用户名不是以_开头")
elif len(username)<3 or len(username)>30:
    print("输入的用户名长度不在3～30个字符之间")
elif len(password)<8 or len(password)>16:
    print("输入的密码长度不在8～16个字符之间")
else:
    if password.find('_')!=-1:
        pw=password.replace('_','0')
        print(pw)
        if pw.isalnum()==False:
            print("输入的密码不能包含除下划线、数字和字母以外的其他字符！")
        else:
            print("注册成功！欢迎",username)

    else:
            print("密码必须包含下划线")