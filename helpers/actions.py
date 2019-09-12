#!/usr/bin/env python
from helpers import selectors
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def search(driver, query):
    search_input = driver.find_element_by_id("search_query_top")
    search_input.send_keys(query)
    search_input.send_keys(Keys.RETURN)
    products = selectors.get_all_products_on_page(driver)
    search_input = driver.find_element_by_id("search_query_top")
    search_input.clear()

    assert len(products) > 0
    return products


def add_product_to_cart(driver, wait, product):
    hover_action = ActionChains(driver).move_to_element(product)
    hover_action.perform()

    add_to_cart_button = wait.until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'ajax_add_to_cart_button'))
    )
    add_to_cart_button.click()

    wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "layer_cart_product"))
    )

    modal_message = driver.find_element_by_xpath('//*[@id="layer_cart"]/div[1]/div[1]/h2')
    assert modal_message.text == "Product successfully added to your shopping cart"

    continue_button = driver.find_element_by_class_name("continue")
    continue_button.click()