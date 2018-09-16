import  unittest
#1. 继承自unittest.TestCase
#2. case均以test开头

class Mytest(unittest.TestCase):
    #test fixture
    def setUp(self):              #每个用例开始
        print("start...")

    #test case
    def test_001(self):
        print("001")
       # self.assertEquals("1","1")            断言
    #test case
    def test_002(self):
        print("002")

    #test fixture
    def tearDown(self):           #每个用例结束
        print("end...")

class Mytest2(unittest.TestCase):

    #test case
    def test_201(self):
        print("201")

    #test case
    def test_202(self):
        print("202")
if __name__ == '__main__':
    # unittest.main()
    mysuite=unittest.TestSuite()
    mysuite.addTest(Mytest("test_001"))
    mysuite.addTest(Mytest2("test_202"))

    unittest.TextTestRunner(verbosity=2).run(mysuite)