from common.unit_package import exe_script_click
from pages.base_page import BasePage

username = "(//input)[1]"
password = "(//input)[2]"
login_btn = "#root > div > div.sc-AxgMl.cVmQYF > div > div.login-form > button"
new_case = "(//div[@class='nav-box'])[1]"


class LoginPage(BasePage):

    def from_username(self):
        return self.get_ele_by_xpath(username)

    def from_password(self):
        return self.get_ele_by_xpath(password)

    def from_new_case(self):
        return self.get_ele_by_xpath(new_case)

    def login(self, username_text, password_text):
        self.from_username().send_keys(username_text)
        self.from_password().send_keys(password_text)
        self.exe_script_click(login_btn)
        return self.from_new_case().text
