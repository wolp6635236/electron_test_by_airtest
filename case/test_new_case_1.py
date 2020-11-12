import unittest
from time import sleep

from base_package import driver_factory
from pages.login_page import LoginPage
from pages.new_case_page import NewCasePage


class TestNewCase1(unittest.TestCase):
    def setUp(self):
        self.driver = driver_factory.ElectronFactory()
        username_text = "demo-data04"
        password_text = "a1234567"
        login_page = LoginPage(driver=self.driver)
        text = login_page.login(username_text, password_text)

    # def tearDown(self):
        # sleep(10000)

    def test_new_case_qq(self):
        new_case_page = NewCasePage(driver=self.driver)
        new_case_page.crete_case('你好', ['QQ'], '昨天夫', ['QQ', '支付宝', '音频'])


if __name__ == '__main__':
    unittest.main()
