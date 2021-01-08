dict1={'num':'30406180123','name':'张俊杰','age':18}
dict2=dict([('num','30406180123'),('name','张俊杰'),('age',18)])
# dict3=dict(num='30406180123',name='张俊杰',age=18)
# dict4=dict(zip(['num','name','age'],['30406180123','张俊杰',18]))
# dict5=dict.fromkeys(['num','name','age'],18)
# print(dict1)
# print(dict2)
# print(dict3)
# print(dict4)
# print(dict5)
#
# dict1['num']='30406180105'
# print(dict1['num'])
# print(dict1)
# print(dict1.get('age'))
#
#
# #添加键值
# dict1['sex']='male'
# print(dict1)
#
# # 字典复制3种方法1.直接复制   2.浅复制  3.深复制
# #1.直接复制
# dict7=dict1
# # 2.浅复制
# dict6=dict.copy(dict1)
# print(dict6)
# # 3.深复制



#遍历字典
print(dict2)
for name,value in dict2.items():
    print(name,"---",value)

for name in dict2.keys():
    print(name)