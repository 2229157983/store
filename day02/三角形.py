a=float(input("请输入三角形第一条边："))
b=float(input("请输入三角形第二条边："))
c=float(input("请输入三角形第三条边："))
if a>0 and b>0 and c>0 and a+b>c and a+c>b and b+c>a:
    if a==b==c:
        print("构成等边三角形")
    elif a==b or a==c or b==c:
        print("构成等腰三角形")
    else:
        print("构成普通三角形")
else:
    print("不能构成三角形")
