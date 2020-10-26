from selenium.webdriver.common.by import By


class ShoppingCartPage:
    SHOPPING_CART_CSS = (By.CSS_SELECTOR, "a.shopping_cart_link")
    CHECKOUT_BTN_CSS = (By.CSS_SELECTOR, "a.btn_action")
    CONTINUE_SHOPPING_CSS = (By.CSS_SELECTOR, "a.btn_secondary")



    def __init__(self, driver):
        self.driver = driver

    def clickShoppingCartbtn(self):
        click_shoppingcart = self.driver.find_element(*self.SHOPPING_CART_CSS)
        click_shoppingcart.click()

    def clickCheckoutBtn(self):
        click_checkout_btn = self.driver.find_element(*self.CHECKOUT_BTN_CSS)
        click_checkout_btn.click()

    def isYourCartHeaderVisible(self):
        return self.driver.find_element(By.CSS_SELECTOR, "div.subheader").is_displayed()

    def searchItemByName(self,item_name):
        item=self.driver.find_element(By.XPATH,".//div[text()='"+item_name+"']")
        return item.text

