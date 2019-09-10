#!/usr/bin/env python


def login_decorator(func):
    def login_to_website(*args, **kwargs):
        driver = args[0].driver
        cfg = args[0].config
        current_url = driver.current_url
        login_buttons = driver.find_elements_by_class_name('login')
        if len(login_buttons) > 0:
            login_buttons[0].click()
            inp_email = driver.find_element_by_id('email')
            inp_pass = driver.find_element_by_id('passwd')
            btn_login = driver.find_element_by_id('SubmitLogin')
            inp_email.send_keys(cfg['website']['login'])
            inp_pass.send_keys(cfg['website']['pass'])
            btn_login.click()
            driver.get(current_url)
        func(*args, **kwargs)
    return login_to_website


def anonymous_decorator(func):
    def logout_from_website(*args, **kwargs):
        driver = args[0].driver
        current_url = driver.current_url
        logout_buttons = driver.find_elements_by_class_name('logout')
        if len(logout_buttons) > 0:
            logout_buttons[0].click()
            driver.get(current_url)
        func(*args, **kwargs)
    return logout_from_website