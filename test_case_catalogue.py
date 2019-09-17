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



    def test_verify_order(self):
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
