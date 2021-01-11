sfz = input("请输入您的身份证件存放路径：")
read = open(sfz,"rb")
write = open("F:\pythonProject\day06\picture\python.jpg","wb")

data = read.read()
write.write(data)

read.close()
write.close()