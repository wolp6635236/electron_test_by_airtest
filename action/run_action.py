import os
from time import sleep

from airtest_script.airtest_t import start_qq_by_mobile, login, adb_shell, backups, confirm_backups, \
    confirm_backups_for_pc
from config_path import config_path
from pages.login_page import LoginPage
from pages.new_case_page import NewCasePage
path = os.path.dirname(os.path.dirname(__file__))
print(path)

adb_path = config_path(os.path.join("lib", "adb.exe"))

cp_image = adb_path + ' push {}/airtest_script/image/IMG_20200705_104501.jpg /sdcard/DCIM/Screenshots/'.format(path)
print(cp_image)
delete_image = adb_path + " shell su -c 'rm /sdcard/DCIM/Screenshots/*'"


class RunAction:
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(10)
        self.message = None

    def test_case(self, username_text, password_text, case_name, monitor_name, app_type):
        login_page = LoginPage(driver=self.driver)
        text = login_page.login(username_text, password_text)
        new_case_page = NewCasePage(driver=self.driver)
        return new_case_page.crete_case(case_name, app_type, monitor_name, app_type)

    def login_qq(self):
        try:
            login()
            adb_shell(delete_image)
            adb_shell(cp_image)
            sleep(2)
            start_qq_by_mobile()
            sleep(4)
            backups()
            sleep(1)
            confirm_backups()
            confirm_backups_for_pc()
            self.message = '备份成功'
        except Exception as e:
            print(e)
            self.message = str(e)
        return self.message


if __name__ == '__main__':
    ra = RunAction('driver')
    # ra.test_case()
    ra.login_qq()
