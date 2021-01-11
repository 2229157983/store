#将a.txt文件复制一份到    D:\b.txt
read=open("a.txt","r+",encoding="utf-8")
write=open("D:\\b.txt","w+",encoding="utf-8")

#1.读取所有数据
data=read.read()#2.将读取的数据写入新的文件里
write.write(data)



#3.关闭资源
read.close()
write.write()