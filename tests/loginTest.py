import unittest

import HtmlTestRunner
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pages.loginPage import LoginPage
from pages.productsPage import ProductsPage
from tests.baseTest import BaseTest


class LoginTest(BaseTest):

 def setUp(self):
   self.driver = super().getBrowser()
   self.driver.implicitly_wait(15)
   self.driver.maximize_window()
   LoginPage(self.driver).loginStep()

 def test_01_login(self):
      products_page=ProductsPage(self.driver)
      self.assertTrue(products_page.isProductHeaderVisible())

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))


