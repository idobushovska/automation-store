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

    def test_category_submenus(self):
        dresses_tab = self.driver.find_element_by_xpath('//*[@id="block_top_menu"]/ul/li[2]/a')
        assert dresses_tab.get_attribute(
            'href') == 'http://automationpractice.com/index.php?id_category=8&controller=category'
        assert dresses_tab.get_attribute('title') == 'Dresses'
        assert dresses_tab.text == 'DRESSES'
        assert self.driver.find_element_by_xpath('//*[@id="columns"]/div[1]').text == '> Women>Dresses'
        assert self.driver.find_element_by_xpath('//*[@id="center_column"]/div[1]/div/div/span').text == 'Dresses'
        dresses_banner_textline_one = "Find your favorites dresses from our wide choice of evening, casual or summer dresses!"
        dresses_banner_textline_two = "We offer dresses for every day, every style and every occasion."
        assert self.driver.find_element_by_xpath(
            '//*[@id="center_column"]/div[1]/div/div/div/p[1]').text == dresses_banner_textline_one
        assert self.driver.find_element_by_xpath(
            '//*[@id="center_column"]/div[1]/div/div/div/p[2]').text == dresses_banner_textline_two
        self.driver.find_element_by_xpath('//*[@id="block_top_menu"]/ul/li[1]/a').click()
        women_tab = self.driver.find_element_by_xpath('//*[@id="block_top_menu"]/ul/li[1]/a')
        assert women_tab.get_attribute('href') == 'http://automationpractice.com/index.php?id_category=3&controller=category'
        assert women_tab.get_attribute('title') == 'Women'
        assert women_tab.text == 'WOMEN'
        assert self.driver.find_element_by_xpath('//*[@id="columns"]/div[1]/span[2]').text == 'Women'
        assert self.driver.find_element_by_xpath('//*[@id="center_column"]/div[1]/div/div/span').text == 'Women'
        women_banner_heading = "You will find here all woman fashion collections."
        women_banner_textline_one = "This category includes all the basics of your wardrobe and much more:"
        women_banner_textline_two = "shoes, accessories, printed t-shirts, feminine dresses, women's jeans!"
        assert self.driver.find_element_by_xpath('//*[@id="center_column"]/div[1]/div/div/div/p[1]/strong').text == women_banner_heading
        assert self.driver.find_element_by_xpath('//*[@id="center_column"]/div[1]/div/div/div/p[2]').text == women_banner_textline_one
        assert self.driver.find_element_by_xpath('//*[@id="center_column"]/div[1]/div/div/div/p[3]').text == women_banner_textline_two
        self.driver.find_element_by_xpath('//*[@id="block_top_menu"]/ul/li[3]/a').click()
        tshirt_tab = self.driver.find_element_by_xpath('//*[@id="block_top_menu"]/ul/li[3]/a')
        assert tshirt_tab.get_attribute(
            'href') == 'http://automationpractice.com/index.php?id_category=5&controller=category'
        assert tshirt_tab.get_attribute('title') == 'T-shirts'
        assert tshirt_tab.text == 'T-SHIRTS'
        assert self.driver.find_element_by_xpath('//*[@id="columns"]/div[1]').text == '> Women>Tops>T-shirts'
        assert self.driver.find_element_by_xpath('//*[@id="center_column"]/div[1]/div/div/span').text == 'T-shirts'
        tshirt_banner_textline_one = "The must have of your wardrobe, take a look at our different colors,"
        tshirt_banner_textline_two = "shapes and style of our collection!"
        assert self.driver.find_element_by_xpath(
            '//*[@id="center_column"]/div[1]/div/div/div/p[1]').text == tshirt_banner_textline_one
        assert self.driver.find_element_by_xpath(
            '//*[@id="center_column"]/div[1]/div/div/div/p[2]').text == tshirt_banner_textline_two








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

    def test_newsletter(self):
        assert self.driver.find_element_by_xpath('//*[@id="newsletter_block_left"]/h4').text == 'Newsletter'
        email_field = self.driver.find_element_by_xpath('//*[@id="newsletter-input"]')
        assert email_field.get_attribute('value') == 'Enter your e-mail'
        email_field.send_keys('test1234@yopmail.com')
        assert self.driver.find_element_by_xpath('//*[@id="newsletter_block_left"]/div/form/div/button').click()
        newsletter_message = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="columns"]/p')))
        assert newsletter_message.text == 'Newsletter : You have successfully subscribed to this newsletter.'

    def test_follow(self):
        assert self.driver.find_element_by_xpath('//*[@id="social_block"]/h4').text == 'Follow us'
        social_links = self.driver.find_element_by_xpath('//*[@id="social_block"]/ul')
        facebook_link = social_links.find_element_by_class_name('facebook').find_element_by_tag_name('a')
        assert facebook_link.get_attribute('href') == 'https://www.facebook.com/groups/525066904174158/'
        twitter_link = social_links.find_element_by_class_name('twitter').find_element_by_tag_name('a')
        assert twitter_link.get_attribute('href') == 'https://twitter.com/seleniumfrmwrk'
        youtube_link = social_links.find_element_by_class_name('youtube').find_element_by_tag_name('a')
        assert youtube_link.get_attribute('href') == 'https://www.youtube.com/channel/UCHl59sI3SRjQ-qPcTrgt0tA'
        google_link = social_links.find_element_by_class_name('google-plus').find_element_by_tag_name('a')
        assert google_link.get_attribute('href') == 'https://plus.google.com/111979135243110831526/posts'


    def test_footer_store_info(self):
        copyright_link =  self.driver.find_element_by_xpath('//*[@id="footer"]/div/section[4]/div/a')
        assert copyright_link.get_attribute('href') == 'http://www.prestashop.com/'
        store_info = self.driver.find_element_by_xpath('//*[@id="block_contact_infos"]')
        assert store_info.find_element_by_tag_name('h4').text == 'Store information'
        assert store_info.find_element_by_xpath('//*[@id="block_contact_infos"]/div/ul/li[1]').text == 'Selenium Framework, Research Triangle Park, North Carolina, USA'
        assert store_info.find_element_by_xpath('//*[@id="block_contact_infos"]/div/ul/li[2]').text == 'Call us now: (347) 466-7432'
        email_element = store_info.find_element_by_xpath('//*[@id="block_contact_infos"]/div/ul/li[3]')
        assert email_element.text == 'Email: support@seleniumframework.com'
        assert email_element.find_element_by_tag_name('a').get_attribute('href') == 'mailto:%73%75%70%70%6f%72%74@%73%65%6c%65%6e%69%75%6d%66%72%61%6d%65%77%6f%72%6b.%63%6f%6d'

    def test_footer_category(self):
        category_menu = self.driver.find_element_by_xpath('//*[@id="footer"]/div/section[2]')
        assert category_menu.find_element_by_xpath('//*[@id="footer"]/div/section[2]/h4').text == 'Categories'
        women_menu = category_menu.find_element_by_xpath('//*[@id="footer"]/div/section[2]/div/div/ul/li/a')
        assert women_menu.get_attribute('href') =='http://automationpractice.com/index.php?id_category=3&controller=category'
        assert women_menu.text == 'Women'

    def test_footer_women_navigation(self):
        women_menu = self.driver.find_element_by_xpath('//*[@id="footer"]/div/section[2]/div/div/ul/li/a')
        women_menu.click()
        women_menu_selected = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="categories_block_left"]/h2')))
        assert women_menu_selected.text == 'WOMEN'

    def test_footer_information(self):
        information_menu = self.driver.find_element_by_xpath('//*[@id="block_various_links_footer"]')
        assert information_menu.find_element_by_xpath('//*[@id="block_various_links_footer"]/h4').text == 'Information'
        link_menu_1 = self.driver.find_element_by_xpath('//*[@id="block_various_links_footer"]/ul/li[1]/a')
        assert link_menu_1.text == 'Specials'
        assert link_menu_1.get_attribute('href') =='http://automationpractice.com/index.php?controller=prices-drop'
        link_menu_2 = self.driver.find_element_by_xpath('//*[@id="block_various_links_footer"]/ul/li[2]/a')
        assert link_menu_2.text == 'New products'
        assert link_menu_2.get_attribute('href') == 'http://automationpractice.com/index.php?controller=new-products'
        link_menu_3 = self.driver.find_element_by_xpath('//*[@id="block_various_links_footer"]/ul/li[3]/a')
        assert link_menu_3.text == 'Best sellers'
        assert link_menu_3.get_attribute('href') == 'http://automationpractice.com/index.php?controller=best-sales'
        link_menu_4 = self.driver.find_element_by_xpath('//*[@id="block_various_links_footer"]/ul/li[4]/a')
        assert link_menu_4.text == 'Our stores'
        assert link_menu_4.get_attribute('href') == 'http://automationpractice.com/index.php?controller=stores'
        link_menu_5 = self.driver.find_element_by_xpath('//*[@id="block_various_links_footer"]/ul/li[5]/a')
        assert link_menu_5.text == 'Contact us'
        assert link_menu_5.get_attribute('href') == 'http://automationpractice.com/index.php?controller=contact'
        link_menu_6 = self.driver.find_element_by_xpath('//*[@id="block_various_links_footer"]/ul/li[6]/a')
        assert link_menu_6.text == 'Terms and conditions of use'
        assert link_menu_6.get_attribute('href') == 'http://automationpractice.com/index.php?id_cms=3&controller=cms'
        link_menu_7 = self.driver.find_element_by_xpath('//*[@id="block_various_links_footer"]/ul/li[7]/a')
        assert link_menu_7.text == 'About us'
        assert link_menu_7.get_attribute('href') == 'http://automationpractice.com/index.php?id_cms=4&controller=cms'
        link_menu_8 = self.driver.find_element_by_xpath('//*[@id="block_various_links_footer"]/ul/li[8]/a')
        assert link_menu_8.text == 'Sitemap'
        assert link_menu_8.get_attribute('href') == 'http://automationpractice.com/index.php?controller=sitemap'

    def test_footer_myaccount(self):
        myaccount_menu = self.driver.find_element_by_xpath('//*[@id="footer"]/div/section[5]')
        myaccount_menu_header = myaccount_menu.find_element_by_xpath('//*[@id="footer"]/div/section[5]/h4/a')
        assert myaccount_menu_header.get_attribute('href') =='http://automationpractice.com/index.php?controller=my-account'
        assert myaccount_menu_header.text =='My account'
        link_menu_1 = self.driver.find_element_by_xpath('//*[@id="footer"]/div/section[5]/div/ul/li[1]/a')
        assert link_menu_1.text == 'My orders'
        assert link_menu_1.get_attribute('href') == 'http://automationpractice.com/index.php?controller=history'
        link_menu_2 = self.driver.find_element_by_xpath('//*[@id="footer"]/div/section[5]/div/ul/li[2]/a')
        assert link_menu_2.text == 'My credit slips'
        assert link_menu_2.get_attribute('href') == 'http://automationpractice.com/index.php?controller=order-slip'
        link_menu_3 = self.driver.find_element_by_xpath('//*[@id="footer"]/div/section[5]/div/ul/li[3]/a')
        assert link_menu_3.text == 'My addresses'
        assert link_menu_3.get_attribute('href') == 'http://automationpractice.com/index.php?controller=addresses'
        link_menu_4 = self.driver.find_element_by_xpath('//*[@id="footer"]/div/section[5]/div/ul/li[4]/a')
        assert link_menu_4.text == 'My personal info'
        assert link_menu_4.get_attribute('href') == 'http://automationpractice.com/index.php?controller=identity'

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
