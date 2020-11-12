import unittest

from pages.login_page import LoginPage

from base_package import driver_factory


class LoginCase(unittest.TestCase):
    def setUp(self):
        self.driver = driver_factory.ElectronFactory()

    def test_login_success(self):
        username_text = "demo-data04"
        password_text = "a1234567"
        login_page = LoginPage(driver=self.driver)
        text = login_page.login(username_text, password_text)
        print(text)
        self.assertEqual('新增报案', text)

