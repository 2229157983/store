class OldPhone:
    __brand=None
    number=None
    '''def __init__(self,brand):
        self.__brand=brand'''

    def setBrand(self,brand):
        self.__brand=brand
    def getBrand(self):
        return self.__brand

    def call(self,brand,):
        print(brand,"手机正在给",self.number,"打电话")

class NewPhone(OldPhone):
    def call(self,brand):
        print("语音拨号中...")
        super().call(brand)
        print("品牌为：",brand,"的手机很好用")


phone=NewPhone()
phone.number="18533333333"
phone.call("诺基亚")
