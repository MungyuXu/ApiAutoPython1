import unittest


def test02():
    return "这是baidu下的test02"

def test03():
    return "这是baidu下的test03"

class UnitTestClass(unittest.TestCase):
    def setUp(self) :
        print("啊啊啊啊啊啊啊啊啊")
    def testtest02(self):
        print("test02的unit方法")
        u'''这是测试用例的中文描述'''
        # self.assertEqual("这是baidu下的test02")

    def testtest03(self):
        print("百度test02下的test03")
        self.assertEqual(1,2)