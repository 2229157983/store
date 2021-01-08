#14-周俊
print("请输入10个数：")
list=list()
for i in range(10):
    list.append(int(input()))
list.sort(reverse=True)
print(list)