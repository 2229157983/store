# 10-赵成
import time
print("==========执行开始==========")
for i in range(0,11):
    a = 10 * i
    b = "▌▌" * i
    c = "••" * (10-i)
    print("{:^3}%[{}->{}]".format(a,b,c))
    time.sleep(1)
print("==========执行结束=========")
