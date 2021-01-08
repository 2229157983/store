'''
#定义一个列表并赋初值
list1 = [3,53,"abc",2.5]
list2=list1
print(list1)
print(list2) #list2存的是list2的地址

#列表引用
print(list1[2])
list1[1]="def"
print(list1)

#赋初值方法（字符串  range  元组）
list3=list(range(10,20))
list4=list('abc')
print(list3)
print(list4)
#元组
truple = (10,20,30)
list5 = list(truple)
print(list5)

#列表遍历
#while
i=0
while i<len(list1):
    print(list1[i])
    i+=1

#for
for i in list1:
    print(i)
'''

# #末尾增加新元素
# list1=[1,2,3,4]
# list1.append(10)
# print(list1)
# #末尾增加多个元素
# list2=[4,5,6]
# list3=[8,9,0]
# list1.append(list2)
# list3.extend(list2)
# print("list1=",list1)
# print("list3=",list3)
# #指定位置加元素
# list2.insert(2,'a')
# list2.insert(3,6)
# print(list2)
# #查找
# n=list2.index(6)
# print(n)
# #统计出现的次数
# num=list2.count(6)
# print(num)
# #删除元素 1 del
# print("list1=",list1)
# del list1[2]
# print("list1=",list1)
# #删除元素 2 pop
# print("list1=",list1)
# list1.pop(2)
# print("list1=",list1)
# #删除元素 3 remove
# list4=[1,2,"a",3,"a",4,"a",5,]
# print("list4=",list4)
# while 'a' in list4:
#     list4.remove("a")
#print("list4=",list4)

# #分片操作
# list1= [1,2,3,4]
# list1[2:]=[5,6,7]
# print(list1)
# list1[2:2]=[3,4]
# print(list1)
# list1[0:2]=[0,0]
# print(list1)

#排序
#实现冒泡排序 从大到小
list=[7,1,6,5,4,9,2]
list.sort()
print(list)
list.reverse()
print(list)