from time import sleep
import sys
import os

sys.path.append(os.path.abspath('./'))

from selenium.webdriver.common.keys import Keys
from base_package import driver_factory, login_fs
from common import unit_package

print(os.path.dirname(__file__))

driver = driver_factory.ElectronFactory()
driver.implicitly_wait(5)

case_name = ".ant-input.caseName"
app_type = "(//div[@class='ant-select-selector'])[1]/span/input"
creat_case_btn = ".ant-btn.ant-btn-primary"
person_name = "//*[@class='mark']/../input[1]"
next_btn = ".ant-btn.submit.ant-btn-primary>span"
go_get = ".ant-btn.ant-btn-primary>span"
qq = "//p[text()='QQ']/../label/span/input"
get_phone_info_btn = "#root > div > div.sc-fzonZV.fjLydT > div.content > div.sc-fznBtT.ccaska > section > div > " \
                     "div.phone-box > div.add-phone > div > button "
get_data_btn = "#root > div > div.sc-fzonZV.fjLydT > div.content > div.sc-fznBtT.ccaska > section > div > " \
               "div.finish-btn > button "


def new_cases():
    login_fs.login(driver)
    sleep(2)
    driver.find_element_by_css_selector(case_name).send_keys('test')
    sleep(2)
    driver.find_element_by_xpath(app_type).send_keys('截屏')
    driver.find_element_by_xpath(app_type).send_keys(Keys.ENTER)
    driver.find_element_by_xpath(app_type).send_keys('QQ')
    driver.find_element_by_xpath(app_type).send_keys(Keys.ENTER)
    sleep(1)
    unit_package.exe_script_click(driver, creat_case_btn)
    sleep(1)
    driver.find_element_by_xpath(person_name).send_keys('123')
    unit_package.exe_script_click(driver, next_btn)
    sleep(2)
    driver.find_element_by_xpath(qq).send_keys(Keys.SPACE)
    unit_package.exe_script_click(driver, go_get)
    sleep(2)
    unit_package.exe_script_click(driver, get_phone_info_btn)
    sleep(8)
    unit_package.exe_script_click(driver, get_data_btn)


if __name__ == '__main__':
    new_cases()
