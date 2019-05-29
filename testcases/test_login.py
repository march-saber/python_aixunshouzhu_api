import unittest
from ddt import ddt,data
from common import do_excel
from common.http_requests import HttpRquests
from common import logger
from common import contants
from common import context

logger = logger.get_logger(__name__)
@ddt #装饰测试类
class RegisterTest(unittest.TestCase):
    excel = do_excel.DoExcel(contants.shouzhu_case_file,'login')
    cases = excel.get_case()

    @classmethod #装饰成类方法
    def setUpClass(cls):
        logger.info("准备测试前置")
        cls.http_request = HttpRquests()
        # cls.mysql = do_mysql.DoMysql()

    # def setUp(self):
    #     self.http_request = HttpRequests2()

    @data(*cases)  #装饰测试方法，接收可迭代数据,cases为实例,
    def test_register(self,case):
        logger.info("开始测试：{0}".format(case.title))

        # case.data = eval(case.data) #转换成字典
        # print(type(case))
        # if case.data.__contains__('mobilephone') and case.data['mobilephone'] == 'normal_user':  #has_key判断键是否存在字典，存在返回Ture，否则返回false
        #     case.data['mobilephone'] = config.get('data','normal_user')  #那到配置文件里面的值赋值给mobilephone
        #
        # if case.data.__contains__('pwd') and case.data['pwd'] == 'normal_pwd':  #has_key判断键是否存在字典，存在返回Ture，否则返回false
        #     case.data['pwd'] = config.get('data','normal_pwd')  #那到配置文件里面的值赋值给pwd
        #
        # if  case.data.__contains__('memberId') and case.data['memberId'] == 'loan_member_id':  #has_key判断键是否存在字典，存在返回Ture，否则返回false
        #     case.data['memberId'] = config.get('data','loan_member_id')  #那到配置文件里面的值赋值给mobilephone
        # 在请求之前替换参数化的值

        case.data = context.replace(case.data)

        if case.data.find("unregistered_mobile") > -1:  #未注册实现
            sql = "select max(mobilePhone) from aixun_shouzhu.user"
            phone = self.mysql.fetch_one(sql)[0]
            new_phone = int(phone)+1
            print("新手机号码：",new_phone)
            case.data = case.data.replace('unregistered_mobile',str(new_phone))
            # 替换参数值,replace替换新的字符串，重新返回一个新的字符串

        resp = self.http_request.request(case.method,case.url,case.data)
        try:
            actual_statusMsg = resp.json()['statusMsg']
        except UnboundLocalError as e:
            logger.error("没有找到resp.json()['statusMsg']:{0}".format(e))
        try:
            self.assertEqual(case.expected,actual_statusMsg)
            self.excel.write_result(case.case_id+1,actual_statusMsg,'PASS')
        except AssertionError as e:
            self.excel.write_result(case.case_id+1,actual_statusMsg,'FAIL')
            logger.error("报错了：{}".format(e))
            raise e
        logger.info('测试结束：{0}'.format(case.title))

    @classmethod
    def tearDownClass(cls):
        cls.http_request.close()
    # def tearDown(self):
    #     self.http_request.close()


