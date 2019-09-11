#!/usr/bin/env python

import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import settings
from helpers import auth
from helpers import selectors


class CriticalPathTest(unittest.TestCase):
    """ Covers most important functions of the internet store.
    1. Registration.
    2. Login.
    3. Search.
    4. Shopping Cart.
    5. Checkout.
    6. View order status."""
    @auth.anonymous_decorator
    def test_register_user(self):
        driver = self.driver
        signin_button = driver.find_element_by_class_name("login")
        signin_button.click()

        email_input = driver.find_element_by_id("email_create")
        create_customer_button = driver.find_element_by_id("SubmitCreate")

        email_input.send_keys(self.new_customer['email'])
        create_customer_button.click()

        firstname_input = driver.find_element_by_id("customer_firstname")
        lastname_input = driver.find_element_by_id("customer_lastname")
        password_input = driver.find_element_by_id("passwd")
        billing_firstname_input = driver.find_element_by_id("firstname")
        billing_lastname_input = driver.find_element_by_id("lastname")
        billing_address_input = driver.find_element_by_id("address1")
        city_input = driver.find_element_by_id("city")
        state_select = driver.find_element_by_xpath("//select[@id='id_state']/option[text()='{}']".format(self.new_customer['state']))
        zip_input = driver.find_element_by_id("postcode")
        mobile_input = driver.find_element_by_id("phone_mobile")
        submit_button = driver.find_element_by_id("submitAccount")

        firstname_input.send_keys(self.new_customer['firstname'])
        lastname_input.send_keys(self.new_customer['lastname'])
        password_input.send_keys(self.new_customer['passwd'])
        billing_firstname_input.send_keys(self.new_customer['firstname'])
        billing_lastname_input.send_keys(self.new_customer['lastname'])
        billing_address_input.send_keys(self.new_customer['address'])
        city_input.send_keys(self.new_customer['city'])
        state_select.click()
        zip_input.send_keys(self.new_customer['zip'])
        mobile_input.send_keys(self.new_customer['mobile'])

        submit_button.click()

        my_personal_information_link = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="center_column"]/div/div[1]/ul/li[4]/a'))
        )

        my_personal_information_link.click()
        firstname_input = driver.find_element_by_id("firstname")
        lastname_input = driver.find_element_by_id("lastname")
        self.config['website']['email'] = self.new_customer['email']
        self.config['website']['passwd'] = self.new_customer['passwd']
        assert firstname_input.value == self.new_customer['firstname']
        assert lastname_input.value == self.new_customer['lastname']

    @auth.logged_customer
    def test_search_items_and_add_to_cart(self):
        pass

    @auth.logged_customer
    def test_checkout(self):
        pass

    @auth.logged_customer
    def verify_order(self):
        pass

    def setUp(self):
        self.config = settings.config
        self.timestamp = time.time()
        self.new_customer = self.config['website']['new_customer']
        self.new_customer['email'] = self.new_customer['email_pattern'].format(self.timestamp)
        self.driver = webdriver.Chrome(executable_path=self.config['selenium']['Chrome']['driver_path'])
        self.driver.get(self.config['website']['homepage'])
        self.wait = WebDriverWait(self.driver, 10)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(warnings='ignore')
