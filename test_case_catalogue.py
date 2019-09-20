#!/usr/bin/env python

import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import settings


class CatalogueTest(unittest.TestCase):

    def test_page_header(self):
        banner_image_xpath = '//*[@id="header"]/div[1]/div/div/a/img'
        banner_image = self.driver.find_element_by_xpath(banner_image_xpath)
        assert banner_image.get_attribute('src') == 'http://automationpractice.com/modules/blockbanner/img/sale70.png'
        contact_phone = self.driver.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/nav/span/strong')
        assert contact_phone.text == '0123-456-789'
        contact_button = self.driver.find_element_by_xpath('//*[@id="contact-link"]/a')
        assert contact_button.get_attribute('href') == 'http://automationpractice.com/index.php?controller=contact'
        assert contact_button.get_attribute('title') == 'Contact Us'
        sign_in_button = self.driver.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/nav/div[1]/a')
        assert sign_in_button.get_attribute('href') == 'http://automationpractice.com/index.php?controller=my-account'
        logo_image = self.driver.find_element_by_xpath('//*[@id="header_logo"]/a/img')
        assert logo_image.get_attribute('src') == 'http://automationpractice.com/img/logo.jpg'
        assert self.driver.find_element_by_id('search_query_top').get_attribute('placeholder') == 'Search'
        # assert self.driver.find_element_by_xpath('//*[@id="searchbox"]/button/span').text == 'Search'

    def test_header_contact_us_navigation(self):
        contact_button = self.driver.find_element_by_xpath('//*[@id="contact-link"]/a')
        contact_button.click()
        contact_us_form_title = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="center_column"]/h1')))
        assert contact_us_form_title.text == 'CUSTOMER SERVICE - CONTACT US'


    def test_header_sign_in_navigation(self):
        sign_in_button = self.driver.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/nav/div[1]/a')
        sign_in_button.click()
        sign_in_form_title = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="login_form"]/h3')))
        assert sign_in_form_title.text == 'ALREADY REGISTERED?'

    @unittest.skip('skipped')
    def test_category_submenus(self):
        pass

    @unittest.skip('skipped')
    def test_catalogue_filters(self):
        pass

    @unittest.skip('skipped')
    def test_information_menu(self):
        pass

    @unittest.skip('skipped')
    def test_specials_menu(self):
        pass

    @unittest.skip('skipped')
    def test_products_grid_view(self):
        pass

    @unittest.skip('skipped')
    def test_products_list_view(self):
        pass

    @unittest.skip('skipped')
    def test_add_to_cart(self):
        pass

    @unittest.skip('skipped')
    def test_compare_products(self):
        pass

    @unittest.skip('skipped')
    def test_page_footer(self):
        pass

    def setUp(self):
        self.config = settings.config
        self.timestamp = time.time()
        self.driver = webdriver.Chrome(executable_path=self.config['selenium']['Chrome']['driver_path'])
        self.driver.get(self.config['website']['catalogue'])
        self.wait = WebDriverWait(self.driver, 10)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(warnings='ignore')
