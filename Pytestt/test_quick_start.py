def reverse(string):
    return string[::-1]

def test_reverse():
    string = "good"
    assert reverse(string) == "doog"           #定义了名为reverse(string)的全局函数，作用是把string反转并返回。比如输入”abc”会反转成”cba”

    another_string = "itest"
    assert reverse(another_string) == "tseti"         #定义了名为test_reverse()的函数，包含了2个断言，用来测试reverse()方法的正确性