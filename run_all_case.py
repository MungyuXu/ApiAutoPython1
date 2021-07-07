import unittest
# case_dir:这个是待执行用例的目录。
# pattern：这个是匹配脚本名称的规则，test*.py 意思是匹配 test 开头的所有脚本。
# top_level_dir：这个是顶层目录的名称，一般默认等于 None 就行了

# discover 加载到的用例是一个 list 集合，需要重新写入到一个 list 对象 testcase 里，
# 这样就可以用 unittest 里面的 TextTestRunner 这里类的 run 方法去执行。
# discover方法筛选出来的用例，循环添加到测试套件中
# for test_suit in discover:
#     for test_case in test_suit:
#         # 添加用例到testcase
#         testcase.addTests(test_case)

def all_case():
    #待执行用例的目录
    case_dir="D:\\workspace\\ApiAutoPython\\case"
    testcase=unittest.TestSuite()
    discover=unittest.defaultTestLoader.discover(case_dir,pattern="test*.py",top_level_dir=None)
    testcase.addTests(discover)#直接加载discover
    print("!!!!")
    print(testcase)
    return testcase

if __name__=="__main__":
    #返回实例
    runner=unittest.TextTestRunner()
    #run所有用例，执行unittest里面的所有用例
    runner.run(all_case())