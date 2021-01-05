#range(起始，结束，跳数)
'''for i in range(0,11,2):
    print(i)'''

'''for i in range(0,5):
    for j in range(0,i+1):
        print("*",end="")     #end=""  不换行
    print()'''

#九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print(j,"x",i,"=",(j*i),"\t",end="")
    print()