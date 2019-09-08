import unittest
import yaml
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

with open("../settings.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)
ymlfile.close()


def login_decorator(func):
    def login_to_website(*args, **kwargs):
        driver = args[0].driver
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


class HomePageTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=cfg['selenium']['Chrome']['driver_path'])
        self.driver.get(cfg['website']['homepage'])

    def search_from_home_page(self):
        driver = self.driver
        self.assertIn("My Store", driver.title)
        elem = driver.find_element_by_id("search_query_top")
        elem.send_keys("CHIFFON")
        elem.send_keys(Keys.RETURN)
        products = driver.find_elements_by_class_name("product-container")
        assert len(products) == 2

    @login_decorator
    def test_search_from_home_page_as_logged_user(self):
        self.search_from_home_page()

    @anonymous_decorator
    def test_search_from_home_page_as_guest_user(self):
        self.search_from_home_page()

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(warnings='ignore')
