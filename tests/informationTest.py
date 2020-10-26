import unittest

import HtmlTestRunner
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from pages.finalOrderPage import FinalOrderPage
from pages.loginPage import LoginPage
from pages.overviewPage import OverviewPage
from pages.productsPage import ProductsPage
from tests.baseTest import BaseTest
from pages.shoppingcartPage import ShoppingCartPage
from pages.informationPage import InformationPage


class InformationTest(BaseTest):


    def setUp(self):
        self.driver = super().getBrowser()
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()
        LoginPage(self.driver).loginStep()

    def fillInformationUser(self, first_name, last_name, zip_code):
        ProductsPage(self.driver).addItemByName(super().dataProvider["items"][0])
        ShoppingCartPage(self.driver).clickShoppingCartbtn()
        ShoppingCartPage(self.driver).clickCheckoutBtn()
        InformationPage(self.driver).fillfirstname(first_name)
        InformationPage(self.driver).fillLastname(last_name)
        InformationPage(self.driver).fillzipcode(zip_code)
        InformationPage(self.driver).clickContinueBtn()

    def test_07_Zip_Missing(self):
        information_page=InformationPage(self.driver)
        self.fillInformationUser(super().dataProvider["first_name"], super().dataProvider["last_name"], "")
        self.assertTrue(information_page.isErrorMsgVisible())

    def test_08_fill_information(self):
        overview_page=OverviewPage(self.driver)
        self.fillInformationUser(super().dataProvider["first_name"], super().dataProvider["last_name"], super().dataProvider["zip_code"])
        self.assertTrue(overview_page.isOverviewHeaderVisible())

    def test_09_validate_items(self):
        shopping_page=ShoppingCartPage(self.driver)
        item_name="Sauce Labs Backpack"
        self.fillInformationUser(super().dataProvider["first_name"], super().dataProvider["last_name"], super().dataProvider["zip_code"])
        self.assertEqual(item_name, shopping_page.searchItemByName(item_name), 'Items does not match')

    def test_10_complete_order(self):
        final_page=FinalOrderPage(self.driver)
        overview_page=OverviewPage(self.driver)
        self.fillInformationUser(super().dataProvider["first_name"], super().dataProvider["last_name"], super().dataProvider["zip_code"])
        overview_page.clickFinishBtn()
        self.assertTrue(final_page.is_thank_you_header_visible())

if __name__ == '__main__':
        #report and runner
        unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))

