#计算1-2+3-4+5-6+...-100    05-陈晓玲
s=0
c=0
for i in range(1,100,2):
    s=s+i
for a in range(2,101,2):
    c=c+a
print("计算结果为：",s-c)