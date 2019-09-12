#!/usr/bin/env python

import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import settings
from helpers import actions, auth, selectors


class HomePageTest(unittest.TestCase):

    @auth.logged_customer
    def test_search_from_home_page_as_customer(self):
        self.search_from_home_page(title="My Store",
                                   query="CHIFFON")

    @auth.anonymous
    def test_search_from_home_page_as_guest(self):
        self.search_from_home_page(title="My Store",
                                   query="CHIFFON")

    @auth.logged_customer
    def test_add_item_to_cart_from_homepage_as_customer(self):
        self.add_to_cart_from_home_page()

    @auth.anonymous
    def test_add_item_to_cart_from_homepage_as_guest(self):
        self.add_to_cart_from_home_page()

    @auth.logged_customer
    def test_quick_view_from_homepage_as_customer(self):
        self.open_quick_view(logged_in=True)

    @auth.anonymous
    def test_quick_view_from_homepage_as_guest(self):
        self.open_quick_view(logged_in=False)

    def setUp(self):
        self.config = settings.config
        self.driver = webdriver.Chrome(executable_path=self.config['selenium']['Chrome']['driver_path'])
        self.driver.get(self.config['website']['homepage'])
        self.wait = WebDriverWait(self.driver, 10)

    def search_from_home_page(self, title, query):
        driver = self.driver
        self.assertIn(title, driver.title)
        products = actions.search(driver, query)
        assert len(products) == 2

    def add_to_cart_from_home_page(self):
        product = selectors.get_all_products_on_page(self.driver)[0]
        actions.add_product_to_cart(self.driver, self.wait, product)

    def open_quick_view(self, logged_in=False):
        driver = self.driver
        product_element = selectors.get_all_products_on_page(driver)[1]
        hover_action = ActionChains(self.driver).move_to_element(product_element)
        hover_action.perform()
        quick_view_button = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="homefeatured"]/li[2]/div/div[1]/div/a[2]'))
        )
        quick_view_button.click()

        quick_view_iframe = self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "fancybox-iframe"))
        )
        driver.switch_to.frame(quick_view_iframe)

        wishlist_button = driver.find_element_by_id("wishlist_button")
        wishlist_button.click()
        message = self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "fancybox-error"))
        )
        if not logged_in:
            assert message.text == "You must be logged in to manage your wishlist."
        else:
            assert message.text == "Added to your wishlist."

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(warnings='ignore')
