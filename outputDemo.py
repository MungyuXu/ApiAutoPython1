import unittest
# 生成 html 报告

def all_case():
    #待执行用例的目录
    case_dir="D:\\workspace\\ApiAutoPython\\case"
    testcase=unittest.TestSuite()
    discover=unittest.defaultTestLoader.discover(case_dir,pattern="test*.py",top_level_dir=None)
    testcase.addTests(discover)#直接加载discover
    print("!!!!---")
    print(testcase)
    return testcase

if __name__=="__main__":
    import  HTMLTestRunner
    report_path= "d:\\workspace\\ApiAutoPython\\report\\result.html"
    fp=open(report_path,"wb")
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title="xmy的自动化测试报告",description=u"xmy的用例执行情况：")

    runner.run(all_case())
    fp.close()