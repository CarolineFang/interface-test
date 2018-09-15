import requests
import pytest

class TestV2exApi(object):
    domain = 'https://www.v2ex.com/'        #使用domain变量来参数化测试的地址，因为不同环境的地址可能不一样，使用domain变量之后只需要改动这个变量就可以切换测试环境了

    @pytest.mark.parametrize('name,node_id', [('python', 90), ('java', 63), ('go', 375), ('nodejs', 436)])
    def lang(self, request):
        return request.param            #每次都可以用request.param来访问本次传入fixture中的参数

    def test_node(self, lang):
        path = 'api/nodes/show.json?name=%s' % (lang)
        url = self.domain + path

        res = requests.get(url).json()
        assert res['name'] == lang
        assert 0       #使用assert(0)强制用例失败，这样可以看到每次fixture的参数值

    def test_node(self):
        path = 'api/nodes/show.json?name=python'
        url = self.domain + path
        res = requests.get(url).json()           #使用requests库来简化发送get请求并将返回值的json字符串转换成python字典
        assert res['id'] == 90              #断言id为90是因为测试数据是静态的，id不会发生变化
        assert res['name'] == 'python'