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
    """ Covers most important functions of the internet store.
    1. Registration.
    2. Login.
    3. Search.
    4. Shopping Cart.
    5. Checkout.
    6. View order status."""

    @auth.anonymous
    def test_register_user(self):
        driver = self.driver
        signin_button = driver.find_element_by_class_name("login")
        signin_button.click()

        email_input = self.wait.until(
            EC.visibility_of_element_located((By.ID, 'email_create'))
        )

        create_customer_button = self.wait.until(
            EC.element_to_be_clickable((By.ID, 'SubmitCreate'))
        )

        email_input.send_keys(self.new_customer['email'])

        create_customer_button.click()

        firstname_input = self.wait.until(
            EC.visibility_of_element_located((By.ID, 'customer_firstname'))
        )
        lastname_input = driver.find_element_by_id("customer_lastname")
        password_input = driver.find_element_by_id("passwd")
        billing_firstname_input = driver.find_element_by_id("firstname")
        billing_lastname_input = driver.find_element_by_id("lastname")
        billing_address_input = driver.find_element_by_id("address1")
        city_input = driver.find_element_by_id("city")
        state_select = Select(driver.find_element_by_id('id_state'))
        zip_input = driver.find_element_by_id("postcode")
        mobile_input = driver.find_element_by_id("phone_mobile")

        firstname_input.send_keys(self.new_customer['firstname'])
        lastname_input.send_keys(self.new_customer['lastname'])
        password_input.send_keys(self.new_customer['passwd'])
        billing_firstname_input.send_keys(self.new_customer['firstname'])
        billing_lastname_input.send_keys(self.new_customer['lastname'])
        billing_address_input.send_keys(self.new_customer['address'])
        city_input.send_keys(self.new_customer['city'])
        state_select.select_by_visible_text(self.new_customer['state'])
        zip_input.send_keys(self.new_customer['zip'])
        mobile_input.send_keys(self.new_customer['mobile'])

        submit_button = self.wait.until(
            EC.element_to_be_clickable((By.ID, 'submitAccount'))
        )
        submit_button.click()

        my_personal_information_link = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="center_column"]/div/div[1]/ul/li[4]/a'))
        )

        my_personal_information_link.click()
        firstname_input = self.wait.until(
            EC.visibility_of_element_located((By.ID, 'firstname'))
        )
        lastname_input = driver.find_element_by_id("lastname")
        assert firstname_input.get_attribute('value') == self.new_customer['firstname']
        assert lastname_input.get_attribute('value') == self.new_customer['lastname']

    @auth.logged_customer
    def test_search_items_and_add_to_cart(self):
        driver = self.driver
        wait = self.wait

        products = actions.search(driver, "summer")
        actions.add_product_to_cart(driver, wait, products[0])

        products = actions.search(driver, "short")
        actions.add_product_to_cart(driver, wait, products[0])

        quantity_items_in_cart_span = self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'ajax_cart_quantity'))
        )
        assert quantity_items_in_cart_span.text == '2'

    @auth.logged_customer
    def test_checkout(self):
        driver = self.driver
        wait = self.wait
        products = selectors.get_all_products_on_page(driver)
        actions.add_product_to_cart(driver, wait, products[0])
        checkout_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="header"]/div[3]/div/div/div[3]/div/a'))
        )
        checkout_button.click()

        proceed_to_address_button = self.wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'standard-checkout'))
        )
        proceed_to_address_button.click()

        proceed_to_shipping_button = self.wait.until(
            EC.element_to_be_clickable((By.NAME, 'processAddress'))
        )
        proceed_to_shipping_button.click()

        agree_to_shipping_checkbox = self.wait.until(
            EC.visibility_of_element_located((By.ID, 'uniform-cgv'))
        )
        agree_to_shipping_checkbox.click()

        proceed_to_payment_button = self.wait.until(
            EC.element_to_be_clickable((By.NAME, 'processCarrier'))
        )
        proceed_to_payment_button.click()

        pay_by_bankwire_button = self.wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'bankwire'))
        )
        pay_by_bankwire_button.click()

        complete_order_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="cart_navigation"]/button'))
        )
        complete_order_button.click()

        confirmation_title = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="center_column"]/div/p/strong'))
        )

        assert confirmation_title.text == 'Your order on My Store is complete.'

        confirmation_message = self.driver.find_element_by_xpath('//*[@id="center_column"]/div')
        order_number = re.findall("[0-9A-Z]{9}", confirmation_message.text)[0]

        assert len(order_number) == 9
        self.order_number = order_number

    @auth.logged_customer
    def test_verify_order(self):
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
