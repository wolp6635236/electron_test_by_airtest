# -*-coding:utf-8-*-
from selenium import webdriver


class BasePage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.driver.implicitly_wait(5)

    def get_ele_by_xpath(self, xpath):
        return self.driver.find_element_by_xpath(xpath=xpath)

    def get_ele_by_css(self, css):
        return self.driver.find_element_by_css_selector(css_selector=css)

    def exe_script_click(self, ele):
        return self.driver.execute_script("document.querySelector('{}').click()".format(ele))
