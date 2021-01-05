a=[2,8,5,9,4,6,7,1]
#求所有数的和
sum=0
for i in range(len(a)):
    sum=sum+a[i]
print("总和为：",sum)

#求偶数的和 、奇数a[i]%2！==0
sum1=0
for i in range(len(a)):
    if a[i]%2==0:    #取余
        sum1=sum1+a[i]
print("偶数的和为：",sum1)

#求列表中最大值
i=0
for k in range(0,len(a)):
    if a[k]>i:
        i=a[k]
print("最大值为：",i)

print("最大值为:",max(a))