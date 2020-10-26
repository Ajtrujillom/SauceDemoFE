import unittest
from selenium import webdriver
from pages.loginPage import LoginPage
from webdriver_manager.chrome import ChromeDriverManager

from tests.baseTest import BaseTest

class InvalidLoginTest(BaseTest):
    def setUp(self):
        self.driver = super().getBrowser()
        self.driver.implicitly_wait(10)  # seconds
        self.driver.get("https://www.saucedemo.com/")

    def test_02_Invalid_login(self):
        loginPage = LoginPage(self.driver)
        loginPage.fillUsernameInput(super().dataProvider["invalid_username"])
        loginPage.fillPassword(super().dataProvider["valid_password"])
        loginPage.clickLoginbtn()
        self.assertTrue(loginPage.isErrorMsgVisible())

if __name__ == '__main__':
 unittest.main()