import unittest
import time
import ddt
from Common.read_test_data import read_txt
from Business.registration import Registration


@ddt.ddt
class registrationcase(unittest.TestCase, Registration):
    def setUp(self):
        self.driver = self.get_browser()
        self.driver.implicitly_wait(10)
        pass

    def tearDown(self):
        self.driver.quit()
        pass

    @ddt.unpack
    @ddt.data(*read_txt('Test_Data/registration_data'))
    def test_registration(self, username, password, pwdRepeat, mobile_phone, asserttpye):
        """
            1.首页点击免费注册按钮
            2.注册页面输入username
            3.输入密码
            4.再次输入密码
            5.输入手机号
            6.点击提交注册
            7.断言验证是否注册成功
            8.退出浏览器
            """
        self.driver.get("http://www.liwenli.com/dsc/")
        self.registration(username, password, pwdRepeat, mobile_phone)
        time.sleep(2)
        self.addImage()
        if asserttpye == 1:
            ele = self.driver.find_element_by_id('username-error').text
            self.assertEqual('用户名已经存在,请重新输入', ele, '断言用户名已经存在,请重新输入')
        elif asserttpye == 2:
            ele = self.driver.find_element_by_id('mobile_phone-error').text
            self.assertEqual('手机已存在,请重新输入', ele, '断言手机已存在,请重新输入')
        elif asserttpye == 3:
            ele = self.driver.find_element_by_xpath("//div[@id='ECS_MEMBERZONE']/span").text
            self.assertEqual('您好  ', ele.text, "断言注册成功跳转首页")

        time.sleep(1)
        self.addImage()
