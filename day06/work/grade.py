'''file = open("scores.txt","r",encoding="utf-8")
scores=file.readlines()
file.close()
final=[]
for i in scores:
    data=i.split()
    sum=0
    for score in data[1:]:
        sum=sum+int(score)
        result=data[0]+str(sum)+"\n"
    final.append(result)
read=open("result.txt","w",encoding="utf-8")
read.writelines(final)
read.close()'''

f = open("scores.txt", "r+", encoding="utf-8")
database = {} # "罗恩"：{56,12,36}

lines = f.readlines()# ["罗恩 56 12 36","哈利 52 45 63 10"，......]
for line in lines:
    ites = line.replace("\n","").split(" ") # ["罗恩",56,12,36]
    database[ites[0]] = ites[1:]    # [start:end]  会从start角标开始提取到end结束

for i in database:
    sum = 0
    values = database[i] # ["56","12","36"]
    for value in values:
        sum = sum + int(value)
    print(i , "总分为：",sum)

f.close()