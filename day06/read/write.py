'''
w+:覆盖原来的内容
wa、a+:不覆盖原来的   在原来的内容后面添加
'''

# file  就是当前a.txt文件的句柄，把柄， open(文件名，读写模式，编码集)
file = open("a.txt","a+",encoding="utf-8")

#写入数据
file.write("\n\t鹅鹅鹅")

#关闭资源
file.close()