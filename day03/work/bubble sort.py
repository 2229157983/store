a=[5,2,4,7,9,1,3,5,4,0,6,1,3]
for i in range(len(a)-1):    #只需len(a)-1次排序即结束，i代表每一轮比较
    for j in range(1,len(a)-i):  #i为当前所在的轮数，j表示要遍历的元素
        if a[j-1] > a[j]:
            l=a[j-1]        #数据交换
            a[j - 1]=a[j]
            a[j]=l
print("a=",a)