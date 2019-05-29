import unittest
from ddt import ddt,data
from common import do_excel
from common.http_requests import HttpRquests
from common import do_mysql
from common import logger
from common import contants

logger = logger.get_logger(__name__)
@ddt #装饰测试类
class RegisterTest(unittest.TestCase):
    excel = do_excel.DoExcel(contants.shouzhu_case_file,'register')
    cases = excel.get_case()

    @classmethod #装饰成类方法
    def setUpClass(cls):
        logger.info("准备测试前置")
        cls.http_request = HttpRquests()
        cls.mysql = do_mysql.DoMysql()

    # def setUp(self):
    #     self.http_request = HttpRequests2()

    @data(*cases)  #装饰测试方法，接收可迭代数据,cases为实例,
    def test_register(self,case):
        logger.info("开始测试：{0}".format(case.title))

        if case.data.find("register_mobile") > -1:
            sql = "select max(mobilePhone) from aixun_shouzhu.user"
            phone = self.mysql.fetch_one(sql)[0]
            new_phone = int(phone)+1
            print("新手机号码：",new_phone)
            case.data = case.data.replace('register_mobile',str(new_phone))
            # 替换参数值,replace替换新的字符串，重新返回一个新的字符串

        resp = self.http_request.request(case.method,case.url,case.data)
        try:
            self.assertEqual(case.expected,resp.text)
            self.excel.write_result(case.case_id+1,resp.text,'PASS')
        except AssertionError as e:
            self.excel.write_result(case.case_id+1,resp.text,'FAIL')
            logger.error("报错了：{}".format(e))
            raise e
        logger.info('测试结束：{0}'.format(case.title))

    @classmethod
    def tearDownClass(cls):
        cls.http_request.close()
    # def tearDown(self):
    #     self.http_request.close()


