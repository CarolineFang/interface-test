import unittest
from business.login_func import Login
import HTMLTestRunner

class Testcase(unittest.TestCase):
    def setUp(self):
        print("setup...")


    def test_001(self):
        log=Login()
        log.login("hack_ai_buster","1qaz2wsx#EDC")
        correct_info=log.get_text("class_name","hd_login_name")
        self.assertEquals("hack_ai_buster",correct_info)

    def test_002(self):
        log=Login()
        log.login("error_info","")
        data=log.get_text("id",'error_tips')
        self.assertEquals("请输入密码",data)

    def test_003(self):
        log=Login()
        log.login(",")
        data=log.get_text("id",'error_tips')
        self.assertEquals("请输入账号和密码",data)

    def test_004(self):
        log=Login()
        log.login("error_info","")
        data=log.get_text("id",'error_tips')
        self.assertEquals("请输入你的密码",data)

    def tearDown(self):
        print("teardown...")

if __name__ == '__main__':
    mysuit=unittest.TestSuite()
    case_list=["test_001","test_002","test_003","test_004"]
    for case in case_list:
        mysuit.addTest(Testcase(case))
        unittest.TextTestRunner(verbosity=2).run(mysuit)