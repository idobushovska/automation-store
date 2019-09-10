#!/usr/bin/env python


def get_all_products_on_page(driver):
    return driver.find_elements_by_class_name("product-container")