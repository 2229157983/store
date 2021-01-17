import time
class OldPhone:
    number=None
    def call(self,number1):
        print(self.number,"正在呼叫",number1,"来电归属地：河北，姓名：二狗子，铃声：凤凰传奇。。")
        for i in range(6):
            print(".",end="")
            time.sleep(1)

class NewPhone(OldPhone):

    def call(self,number1):
        super().call(number1)
        print("大头贴：野猪佩奇")

phone=NewPhone()
phone.number="13552648187"
phone.call("14683585477")