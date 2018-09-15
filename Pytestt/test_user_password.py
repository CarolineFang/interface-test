import pytest
import json

class TestUserPassword(object):
    @pytest.fixture
    def users(self):
        return json.loads(open('./users.dev.json', 'r').read()) # 读取当前路径下的users.dev.json文件，返回的结果是dict

    def test_user_password(self, users):
        # 遍历每条user数据
        for user in users:
            passwd = user['password']
            assert len(passwd) >= 6
            msg = "user %s has a weak password" %(user['name'])
            assert passwd != 'password', msg
            assert passwd != 'password123', msg            #3个assert是递进关系，前1个assert断言失败后，后面的assert是不会运行的，因此重要的assert放到前