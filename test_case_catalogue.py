#!/usr/bin/env python

import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import settings


class CriticalPathTest(unittest.TestCase):

    def test_page_header(self):
        image_xpath = '//*[@id="header"]/div[1]/div/div/a/img'
        header_image = self.driver.find_element_by_xpath(image_xpath)
        assert header_image.get_attribute('src') == 'http://automationpractice.com/modules/blockbanner/img/sale70.png'

    def test_category_submenus(self):
        pass

    def test_catalogue_filters(self):
        pass

    def test_information_menu(self):
        pass

    def test_specials_menu(self):
        pass

    def test_products_grid_view(self):
        pass

    def test_products_list_view(self):
        pass

    def test_add_to_cart(self):
        pass

    def test_compare_products(self):
        pass

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
