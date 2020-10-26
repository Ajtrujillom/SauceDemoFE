from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from pages.loginPage import LoginPage
from pages.productsPage import ProductsPage
from tests.baseTest import BaseTest
from pages.shoppingcartPage import ShoppingCartPage


class ShopingCartTest(BaseTest):

    def setUp(self):
        self.driver = super().getBrowser()
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()
        LoginPage(self.driver).loginStep()

    def test_04_Navigate(self):
        shopping_page = ShoppingCartPage(self.driver)
        shopping_page.clickShoppingCartbtn()
        self.assertTrue(shopping_page.isYourCartHeaderVisible())

    def test_05_add_single_item(self):
        products_page = ProductsPage(self.driver)
        shopping_page = ShoppingCartPage(self.driver)
        item_name=super().dataProvider["items"][0]
        products_page.addItemByName(item_name)
        shopping_page.clickShoppingCartbtn()
        self.assertEqual(item_name, shopping_page.searchItemByName(item_name), 'Items does not match')

    def test_06_add_multiple_items(self):
        products_page = ProductsPage(self.driver)
        shopping_page = ShoppingCartPage(self.driver)
        for item_name in super().dataProvider["items"]:
            products_page.addItemByName(item_name)
        shopping_page.clickShoppingCartbtn()
        for item_added in super().dataProvider["items"]:
            self.assertEqual(item_added, shopping_page.searchItemByName(item_added), "Items Does not Match")



