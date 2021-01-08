#   14-周俊
import urllib.request
# 指定url
url = 'http://www.baidu.com'
# 发送请求，服务器做出响应
rsp = urllib.request.urlopen(url)
# 读取响应数据
html = rsp.read()
# 将读取的数据进行解码
html = html.decode()
print(html)
