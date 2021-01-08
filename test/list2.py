#sort原表改变
list=["a","bcd","b","ef","uhgnf"]
list.sort(key=len,reverse=True)
print(list)
list.sort(key=len,reverse=False)
print(list)



# sorted原表不变
list2=[1,8,5,9,4,7]
list3=sorted(list2,reverse=True)

list4=[]
print(list2)
print(list3)



#tuple 元组
tuple=(1,2,3,4)
print(tuple)
tuple1=()
#一个元素
tuple2=(1,)
#俩元素
tuple3=(1,2)
print(tuple1)
print(tuple2)
print(tuple3)



