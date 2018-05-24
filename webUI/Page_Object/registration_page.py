from selenium.webdriver.common.by import By
from Common.selenium_tools import selenium_webdriver


class registration_page(selenium_webdriver):
    username_loc = (By.ID, 'username')
    password_loc = (By.ID, "pwd")
    pwdRepeat_loc = (By.ID, "pwdRepeat")
    mobile_phone_loc = (By.ID, "mobile_phone")
    registsubmit_loc = (By.ID, "registsubmit")

    def send_username(self, username):
        ele=self.find_element(self.username_loc)
        ele.clear()
        ele.send_keys(username)

    def send_password(self, password):
        ele=self.find_element(self.password_loc)
        ele.clear()
        ele.send_keys(password)

    def send_pwdRepeat(self, pwdRepeat):
        ele=self.find_element(self.pwdRepeat_loc)
        ele.clear()
        ele.send_keys(pwdRepeat)

    def send_mobile_phone(self, mobile_phone):
        ele=self.find_element(self.mobile_phone_loc)
        ele.clear()
        ele.send_keys(mobile_phone)

    def registsubmit(self):
        self.find_element(self.username_loc).click()

    def submit_register_button(self):
        self.find_element(self.registsubmit_loc).click()
