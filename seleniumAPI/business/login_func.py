from commonlib.common import Common


class Login(Common):
    def login(self,user,pwd):

        #跳转到一号店
        self.open_url("http://www.yhd.com")

        #定位到登录按钮进行点击
        self.click("class_name","hd_login_link")

        #定位并输入数据
        self.input_date("id","un",user)

        #定位输入密码
        self.input_date("id","pwd",pwd)

        #点击登录
        self.click("id","login_button")

if __name__ == '__main__':
    loginobj=Login()
    loginobj.login("hack_ai_buster","1qaz2wsx#EDC")