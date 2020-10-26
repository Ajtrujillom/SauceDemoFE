from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from pages.loginPage import LoginPage
from pages.productsPage import ProductsPage
from tests.baseTest import BaseTest


class ProductTest(BaseTest):

    def setUp(self):
        self.driver = super().getBrowser()
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()
        LoginPage(self.driver).loginStep()

    def test_03_LogOut(self):
        login_page = LoginPage(self.driver)
        products_page = ProductsPage(self.driver)
        products_page.clickMenubtn()
        products_page.clickLogoutbtn()
        self.assertTrue(login_page.isUsernameInputVisible())
