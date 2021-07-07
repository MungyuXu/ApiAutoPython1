import unittest
#class是定义一个测试的类，并继承 unittest.TestCase 这个类
class IntegerArithmeticTestCase(unittest.TestCase):
    #测试用例名称要test开头
    # 前置
    def setUp(self) :
        print('hhhhh')
        # pass

    # 后置
    def tearDown(self) :
        print(11111)

    def testAdd(self):  # test method names begin with 'test',每行self要对齐不然会报错
        self.assertEqual((1 + 2), 3)
        #断言
        self.assertEqual(0 + 1, 2)
    def testMultiply(self):
        self.assertEqual((0 * 10), 0)
        self.assertEqual((5 * 8), 40)
        #自定义错误信息
        self.assertEqual(1,2,msg="失败原因!!!!%d!=%d"%(1,2))