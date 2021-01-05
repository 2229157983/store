'''List = [1,4,7,5,8,2,1,3,4,5,9,7,6,1,10]
dict={}
for key in List:
    dict[key]=dict.get(key,0)+1
print(dict)'''

list = [1, 4, 7, 5, 8, 2, 1, 3, 4, 5, 9, 7, 6, 1, 10]
for i in range(1, 11):
    times = 0
    for j in range(0, len(list)):
        if i == list[j]:
            times = times + 1
    print(i, "出现了", times, "次")