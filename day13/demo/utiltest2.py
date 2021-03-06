import unittest
from demo.calc import Calculator


class testCalc2(unittest.TestCase):
    def testMul(self):  # 测试方法必须是TEST开头
        c = Calculator()
        # 测试数据
        a = 19
        b = 10
        s = 190 # 期望结果
        sum = c.mul(a, b)  # 实际结果
        self.assertEquals(s, sum)

    def testMul1(self):  # 测试方法必须是TEST开头
        c = Calculator()
        # 测试数据
        a = -19
        b = -10
        s = 190  # 期望结果
        sum = c.mul(a, b)  # 实际结果
        self.assertEquals(s, sum)

    def testMul2(self):  # 测试方法必须是TEST开头
        c = Calculator()
        # 测试数据
        a = -19
        b = 10
        s = -190  # 期望结果
        sum = c.mul(a, b)  # 实际结果
        self.assertEquals(s, sum)

    def testMul3(self):  # 测试方法必须是TEST开头
        c = Calculator()
        # 测试数据
        a = 19
        b = -10
        s = -190  # 期望结果
        sum = c.mul(a, b)  # 实际结果
        self.assertEquals(s, sum)