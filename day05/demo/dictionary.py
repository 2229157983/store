provinces={
    "010":"北京",
    "020":"上海",
    "030":"广州",
    "040":"深圳"
}
#1.如何取数据
value=provinces["010"]

#2.添加050：天津
provinces["050"]="天津"

#3.如何遍历数据
keys=provinces.keys()   #获取字典中的所有键
for key in keys:     #遍历每一个键
    print(key,"=",provinces[key])   #打印：  键=值

#4.010迁到安徽，修改010对应北京改成安徽
provinces["010"]="安徽"#直接修改数据即可，字典会直接进行覆盖数据
print(provinces)