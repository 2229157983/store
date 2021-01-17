from demo1.Address import Address
from demo1.User import User
# 1.将四个地址信息存到地址对象里
add  =  Address("中国","安徽","幸福大道","s001")

# 2.创建用户对象
# 3.将地址对象存到用户对象里
user = User("jason",add)  # user -> address = add.country

# 4.展示
print(user.username)
print(user.address.country)
print(user.address.province)










