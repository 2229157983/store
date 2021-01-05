scores=[90,85,75,72,63,10]
school=[
    [70,50,64,81,82,95],
    [10,20,36,85,75,12],
    [40,62,85,31,20],
    [90,10,120,36,102]
]
#求全校每个班级的总分
for i in range(0,len(school)):
    sum=0
    for j in range(0,len(school[i])):
        sum=sum+school[i][j]
    print((i+1),"班的总分为：",sum)

#对学校所有人求分数和
sum1=0
for i in range(0,len(school)):
    for j in range(0,len(school[i])):
        sum1=sum1+school[i][j]
print("全校分数总和为：",sum1)

#对所有分数进行求和
sum=0
for i in range(0,len(scores)):
    sum=sum+scores[i]
    avg=sum//len(scores)
print("分数总和为：",sum)
print("平均分为：",avg)