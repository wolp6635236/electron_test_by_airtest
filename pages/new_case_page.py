from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage

new_case = "(//div[@class='nav-box'])[1]"
case_name = ".ant-input.caseName"
app_type = "(//div[@class='ant-select-selector'])[1]/span/input"
creat_case_btn = ".ant-btn.ant-btn-primary"
person_name = "//*[@class='mark']/../input[1]"
next_btn = ".ant-btn.submit.ant-btn-primary>span"
qq = "//p[text()='{}']/../label/span/input"
go_get = ".ant-btn.ant-btn-primary>span"
get_phone_info_btn = "#root > div > div.sc-fzqyOu.iYPalA > div.content > div.sc-fznNTe.fnbSrb > section > div > " \
                     "div.phone-box > div.add-phone > div > button "

get_data_btn = "#root > div > div.sc-fzqyOu.iYPalA > div.content > div.sc-fznNTe.fnbSrb > section > div > " \
               "div.finish-btn > button "
start_qq_btn = ".ant-btn.ant-btn-primary>span"
cant_connect_ele = "body > div:nth-child(6) > div > div.ant-modal-wrap > div > div.ant-modal-content > div > div > " \
                   "div.ant-modal-confirm-body > div "


class NewCasePage(BasePage):

    def from_new_case_ele(self):
        return self.get_ele_by_xpath(new_case)

    def from_case_name_ele(self):
        return self.get_ele_by_css(case_name)

    def from_app_type_ele(self):
        return self.get_ele_by_xpath(app_type)

    def from_creat_case_btn_ele(self):
        return self.exe_script_click(creat_case_btn)

    def from_person_name_ele(self):
        return self.get_ele_by_xpath(person_name)

    def from_next_btn_ele(self):
        return self.exe_script_click(next_btn)

    def from_app_type_click_ele(self, app):
        return self.get_ele_by_xpath(qq.format(app))

    def from_go_get_ele(self):
        return self.exe_script_click(go_get)

    def from_get_phone_info_btn_ele(self):
        return self.exe_script_click(get_phone_info_btn)

    def from_get_data_btn(self):
        return self.exe_script_click(get_data_btn)

    def from_start_qq_btn(self):
        return self.exe_script_click(start_qq_btn)

    def crete_case(self, case_names, case_type, person_name_text, app):
        self.from_new_case_ele().click()
        sleep(2)
        self.from_case_name_ele().send_keys(case_names)
        sleep(2)
        for i in case_type:
            self.from_app_type_ele().send_keys(i)
            self.from_app_type_ele().send_keys(Keys.ENTER)
        self.from_creat_case_btn_ele()
        sleep(3)
        self.from_person_name_ele().send_keys(person_name_text)
        sleep(1)
        self.from_next_btn_ele()
        sleep(2)
        for i in app:
            self.from_app_type_click_ele(i).send_keys(Keys.SPACE)
        self.from_go_get_ele()
        sleep(2)
        self.from_get_phone_info_btn_ele()
        try:
            element = WebDriverWait(self.driver, 12).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, cant_connect_ele)))
            print('手机未连接')
            return '##执行错误##:手机未连接'
        except Exception as e:
            print('@#', e)
        self.from_get_data_btn()
        sleep(10)
        self.from_start_qq_btn()
        return '启动qq成功'
