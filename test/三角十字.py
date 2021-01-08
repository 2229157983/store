# 三角十字 05-陈晓玲

print("{:^14s}".format("****这是一个图形****"))
for i in range(7):
    if i!=3:
        print("{:^17s}".format("Δ"))
    else:
        print("{:s}".format("Δ Δ Δ Δ Δ Δ Δ"))

print("*"*18)




sign="Δ"
one="\t"+sign+"\t\n"
print("这是一个图形")
print(one * 3+sign * 7 + "\n" + one * 3 + "*" * 20)