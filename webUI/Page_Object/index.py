from selenium.webdriver.common.by import By
from Common.selenium_tools import selenium_webdriver


class index(selenium_webdriver):
    register_button_loc = (By.XPATH, "//a[@class='link-regist']")

    def click_register_button(self):
        self.find_element(self.register_button_loc).click()
