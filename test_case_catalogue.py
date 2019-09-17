#!/usr/bin/env python

import unittest
import time
from selenium import webdriver
import re
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
import settings
from helpers import auth, actions, selectors


class CriticalPathTest(unittest.TestCase):

    def test_page_header(self):
        pass

    def test_category_submenus(self):
        pass

    def test_catalogue_filters(self):
        pass

    def test_information_menu(self):
        pass

    def test_specials_menu(self):
        pass

    def test_prod_grid_view(self):
        pass

    def test_products_list_view(self):
        pass

    def test_adding_tocart(self):
        pass

    def test_compare_products(self):
        pass

    def test_page_footer(self):
        pass

    def setUp(self):
        self.config = settings.config
        self.timestamp = time.time()
        self.driver = webdriver.Chrome(executable_path=self.config['selenium']['Chrome']['driver_path'])
        self.driver.get(self.config['website']['homepage'])
        self.wait = WebDriverWait(self.driver, 10)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(warnings='ignore')
