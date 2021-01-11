from bank.address import Address
from bank.user import User
b=User()
b.setName("张三")
b.setAccount("88888888")
b.setNum(2000)
b.setBankname("中国工商银行的昌平支行")
b.setPassword(123456)
b.setTime("2021-01-01")

address  = Address()
address.setCountry("中国")
address.setProvince("河北")
address.setStreet("衡水")
address.setDoor("001")
b.setAddress(address)

b.P()
