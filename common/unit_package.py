def exe_script_click(driver, ele):
    return driver.execute_script("document.querySelector('{}').click()".format(ele))
