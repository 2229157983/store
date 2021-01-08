#14-周俊
month = int(input("请输入月份："))
spring = [3,4,5]
summer = [6,7,8]
autom = [9,10,11]
winter = [12,1,2]
if month in spring:
    print("%d月是春季"%month)
elif month in summer:
    print("%d月是夏季"%month)
elif month in autom:
    print("%d月是秋季"%month)
elif month in winter:
    print("%d月是冬季"%month)
else:
    print("请输入正确的月份")