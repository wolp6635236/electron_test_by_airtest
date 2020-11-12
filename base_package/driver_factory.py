# -*-coding:utf-8-*-
import os
from selenium import webdriver

from config_path import config_path

app_path = u"C:\\Program Files\\kuaicai\\电信网络诈骗案件勘查分析系统\\电信网络诈骗案件勘查分析系统.exe"
driver_path = config_path(os.path.join("lib", "chromedriver.exe"))
print(driver_path)


def ElectronFactory():
    location = app_path
    options = webdriver.ChromeOptions()
    options.binary_location = location
    driver = webdriver.Chrome(executable_path=driver_path, options=options)
    return driver


if __name__ == '__main__':
    ElectronFactory()
