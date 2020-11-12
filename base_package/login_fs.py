from common.unit_package import exe_script_click


username = "(//input)[1]"
username_text = "demo-data04"
password = "(//input)[2]"
password_text = "a1234567"
login_btn = "#root > div > div.sc-AxgMl.cVmQYF > div > div.login-form > button"
new_case = "(//div[@class='nav-box'])[1]"


def login(driver):
    driver.find_element_by_xpath(username).send_keys(username_text)
    driver.find_element_by_xpath(password).send_keys(password_text)
    exe_script_click(driver, login_btn)
    driver.find_element_by_xpath(new_case).click()


