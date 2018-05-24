"""Selenium 相关封装"""
from HTMLReport import logger, AddImage
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities


class selenium_webdriver(object):
    """Selenium 相关封装

    """

    def __init__(self, driver, base_url):
        self.base_url = base_url
        if driver:
            self.driver = driver
        else:
            self.driver = webdriver.Chrome()

    def get_browser(self):
        """获取浏览器

        :return: 浏览器对象
        """
        self.driver = webdriver.Chrome()
        # self.driver = webdriver.Remote(
        #     # 表示远程服务器的URL（HUB的URL），默认是：http://127.0.0.1:4444/wd/hub
        #     command_executor='http://127.0.0.1:4444/wd/hub',
        #     # 一种请求能力的字典，启动浏览器会话所需
        #     desired_capabilities=DesiredCapabilities.CHROME
        # )

        logger().info("打开浏览器：{}".format(self.driver.name))
        self.driver.implicitly_wait(10)
        logger().info("设置隐式等待 10 S")
        self.driver.maximize_window()
        logger().info("浏览器最大化")
        return self.driver

    def addImage(self):
        """添加截图到报告中"""
        AddImage(self.driver.get_screenshot_as_base64())

    def open(self, baseUrl, url):
        self.driver.get(baseUrl + url)

    def find_element(self, loc):
        """查找单个元素

        :param loc: 是一个元组 (by,value)
        :return: 元素对象
        """
        return self.driver.find_element(*loc)