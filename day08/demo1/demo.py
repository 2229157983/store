li  = [1,0,2,4,5,3,0,1,9,6,9,8,4,20,21]
c = {}
def countNum(li):
    # 排重操作
    for index,num in enumerate(li):
        if num in li[0:index]:
            continue # 跳过
        count = li.count(num)
        c[num] = count
countNum(li)
print(c)












