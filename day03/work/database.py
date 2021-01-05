names = [
    ["何登勇","56","男","106","IBM", 500 ,"50"],
    ["曹东雪","19","女","230","微软", 501 ,"60"],
    ["刘营营", "19", "女", "210", "Oracle", 600, "60"],
    ["李汉聪", "45", "男", "230", "Tencent", 700 , "10"]
]
sum=0
for i in range(0,len(names)):
    sum=sum+names[i][5]
print("平均成绩为：",sum/len(names))

age=0
for j in range(0,len(names)):
    age=age+int(names[j][1])
print("平均年龄为：",age/len(names))

li=["张佳伟","45","男","220","alibaba",500,"30"]
names.append(li)
print("names=",names)

men=0
women=0
for k in range(0,len(names)):
    if names[k][2]=='男':
        men=men+1
    else:
        women=women+1
print("男生的人数为：",men,"人","\n","女生的人数为：",women,"人")

num50=0
num60=0
num10=0
num30=0
for o in range(0,len(names)):
    if names[o][6]=='50':
        num50=num50+1
    elif names[o][6]=='60':
        num60=num60+1
    elif names[o][6]=='10':
        num10=num10+1
    else:
        num30=num30+1
print("部门编号为50的部门有",num50,"人")
print("部门编号为60的部门有",num60,"人")
print("部门编号为10的部门有",num10,"人")
print("部门编号为30的部门有",num30,"人")

