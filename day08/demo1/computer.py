'''
屏幕大小，价格，cpu型号，内存大小，待机时长），行为（打字，打游戏，看视频）

'''
class Computer:
    screenSize = None
    price = None
    cpuBrand = None
    memorySize = None
    bideTime = None

    def typeWord(self,text):
        print(self.cpuBrand, "型号的电脑正在打印:",text)

    def playGame(self,gameName):
        print("我正在使用电脑打",gameName)

    def watchVideo(self,video):
        print("我正在看：",video)





