import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class HomePageTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='../../bin/chromedriver')

    def test_open_home_page(self):
        driver = self.driver
        driver.get("http://automationpractice.com/index.php")
        self.assertIn("My Store", driver.title)
        elem = driver.find_element_by_id("search_query_top")
        elem.send_keys("CHIFFON")
        elem.send_keys(Keys.RETURN)
        products = driver.find_elements_by_class_name("product-container")
        assert len(products) == 2

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
