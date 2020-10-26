from selenium.webdriver.common.by import By


class OverviewPage:

    FINISH_BTN = (By.CSS_SELECTOR, "a.btn_action")

    def __init__(self, driver):
        self.driver = driver

    def clickFinishBtn(self):
        finish_btn = self.driver.find_element(*self.FINISH_BTN)
        finish_btn.click()

    def isOverviewHeaderVisible(self):
        return self.driver.find_element(By.CSS_SELECTOR,"div.subheader").is_displayed()


