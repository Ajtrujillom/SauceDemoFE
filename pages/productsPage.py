from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductsPage():
    PRODUCTS_HEADER = (By.CSS_SELECTOR, ".product_label")
    MENU_BTN = (By.CSS_SELECTOR, "div.bm-burger-button button")
    LOGOUT_BTN = (By.CSS_SELECTOR, "a#logout_sidebar_link")


    def __init__(self, driver):
        self.driver = driver

    def isProductHeaderVisible(self):
        products_header = self.driver.find_element(*self.PRODUCTS_HEADER)
        return products_header.is_displayed()

    def clickMenubtn(self):
        menu_btn = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.bm-burger-button button")))
        menu_btn.click()

    def clickLogoutbtn(self):
        logout_btn = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a#logout_sidebar_link")))
        logout_btn.click()
        # self.driver.find_element(*self.LOGOUT_BTN).logout_btn.click()

    def addItemByName(self,item_name):
        item=self.driver.find_element(By.XPATH,".//div[text()='"+item_name+"']/../../..//button")
        item.click()
