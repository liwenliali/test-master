from Page_Object.registration_page import registration_page
from Page_Object.index import index


class Registration(index, registration_page):
    """
    1.首页点击免费注册按钮
    2.注册页面输入username
    3.输入密码
    4.再次输入密码
    5.输入手机号
    6.点击提交注册
    7.验证是否注册成功
    """

    def registration(self, username, password, pwdRepeat, mobile_phone):
        self.click_register_button()
        self.send_username(username)
        self.send_password(password)
        self.send_pwdRepeat(pwdRepeat)
        self.send_mobile_phone(mobile_phone)
        self.submit_register_button()
        pass
