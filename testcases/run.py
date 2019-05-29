import unittest
import HTMLTestRunnerNew
from common import contants
from testcases import test_register

# suite = unittest.TestSuite()
# loaderoader = unittest.TestLoader()
# suite.addTest(loaderoader.loadTestsFromModule(test_register))
discover = unittest.defaultTestLoader.discover(start_dir=contants.case_dir, pattern='test_*.py')  # discover查找目录下所有的文件

with open(contants.report_dir + '/report.html','wb+') as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                              title="爱讯守珠",
                                              description="爱讯守珠的测试case",
                                              tester="向仁煌")
    runner.run(discover)
