#14-周俊
list = ["01","张三","9759","02","李四","9984","03","王五","9459"]
for i in range(len(list)):
    print(list[i],end=" ")
    if (i-2)%3==0:
        print("")


