import urllib.request
import urllib.parse
import json
#指定URL
url = "https://fanyi.baidu.com/sug"
#传送的数据
data ={
    'kw':'girl'
}
headers ={
    'accept-language': 'zh-CN,zh;q=0.9'
}
#对发送的数据进行编码
data  = urllib.parse.urlencode(data).encode('utf-8')
print(data)
#发送请求
req = urllib.request.Request(url,data=data,headers=headers)
#服务器根据要打开的文件做出响应
rsp = urllib.request.urlopen(req)

json_data = rsp.read().decode('utf-8')
#将json数据转换成字典
json_data = json.loads(json_data)
for i in json_data['data']:
    print(i['k'],":",i['v'])
#print(json_data)