'''
编写一个注册验证程序，设定如下条件：
（1）用户名必须以下划线“_”开头，长度必须在3～30个字符之间；
（2）密码必须由下划线、数字和字母共同组成，不允许有其他符号，长度必须在8～16个字符之间。
'''
#14-周俊
username = input("请输入用户名:")
password = input("请输入密码:")
if username[0]!="_":
    print("输入的用户名不是以_开头")
elif len(username)<3 or len(username)>30:
    print("输入的用户名长度不在有效范围内")
elif len(password)<8 or len(password)>16:
    print("输入的密码长度不在有效范围内")
else:
    if password.find('_')!=-1:
        pw=password.replace('_','0')
        print(pw)
        if pw.isalnum()==False:
            print("输入的密码不能包含除下划线、数字和字母以外的其他字符！")
        else:
            print("注册成功！欢迎",username)
            print("密码为:",password)
    else:
            print("密码必须包含下划线")