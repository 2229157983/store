f=open("baidu_x_system.log","r+",encoding="utf-8")

#读取所有行
lines=f.readlines()
ips=[]
#对每一行进行切割
for line in lines:
    items=line.split(" ")
    ips.append(items[0])

for index,ip in enumerate(ips):
    if ip in ips[0:index]:
        continue#终止当前循环，并继续下一轮循环
    num=ips.count(ip)
    print(ip,"出现了",num,"次")
f.close()