list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
'''list.reverse()
print("list=",list)'''
for i in range(0,len(list)):
    for j in range(0,i+1):
        c=list[j]
        list[j]=list[i]
        list[i]=c
print("list=",list)