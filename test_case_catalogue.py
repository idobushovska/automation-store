#!/usr/bin/env python

import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import settings


class CatalogueTest(unittest.TestCase):

    def test_page_header_one(self):
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

    def test_page_header_two(self):
        logo_image = self.driver.find_element_by_xpath('//*[@id="header_logo"]/a/img')
        assert logo_image.get_attribute('src') == 'http://automationpractice.com/img/logo.jpg'
        assert self.driver.find_element_by_id('search_query_top').get_attribute('placeholder') == 'Search'
        cart_button = self.driver.find_element_by_xpath('//*[@id="header"]/div[3]/div/div/div[3]/div/a')
        assert cart_button.get_attribute('href') == 'http://automationpractice.com/index.php?controller=order'
        assert cart_button.get_attribute('title') == 'View my shopping cart'
        assert cart_button.find_element_by_xpath('//*[@id="header"]/div[3]/div/div/div[3]/div/a/b').text == 'Cart'
        assert cart_button.find_element_by_xpath('//*[@id="header"]/div[3]/div/div/div[3]/div/a/span[5]').text == '(empty)'

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

    def test_header_cart_navigation(self):
        cart_button= self.driver.find_element_by_xpath('//*[@id="header"]/div[3]/div/div/div[3]/div/a')
        cart_button.click()
        cart_page_title = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="cart_title"]')))
        assert cart_page_title.text == 'SHOPPING-CART SUMMARY'


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

    def test_page_footer(self):
        copyright_link =  self.driver.find_element_by_xpath('//*[@id="footer"]/div/section[4]/div/a')
        assert copyright_link.get_attribute('href') == 'http://www.prestashop.com/'

    def test_footer_category(self):
        category_menu = self.driver.find_element_by_xpath('//*[@id="footer"]/div/section[2]')
        assert category_menu.find_element_by_xpath('//*[@id="footer"]/div/section[2]/h4') == 'Categories'
        women_menu = category_menu.find_element_by_xpath('//*[@id="footer"]/div/section[2]/div/div/ul/li/a')
        assert women_menu.get_attribute('href') =='http://automationpractice.com/index.php?id_category=3&controller=category'
        assert women_menu.text == 'Women'

    def test_footer_women_navigation(self):
        women_menu = self.driver.find_element_by_xpath('//*[@id="footer"]/div/section[2]/div/div/ul/li/a')
        women_menu.click()
        women_menu_selected = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="categories_block_left"]/h2')))
        assert women_menu_selected.text == 'Women'

    def test_footer_information(self):
        information_menu = self.driver.find_element_by_xpath('//*[@id="block_various_links_footer"]')
        assert information_menu.find_element_by_xpath('//*[@id="block_various_links_footer"]/h4') == 'Information'


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
