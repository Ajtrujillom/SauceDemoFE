from selenium.webdriver.common.by import By


class FinalOrderPage:
    THANK_YOU_HEADER=(By.CSS_SELECTOR,"h2.complete-header")

    def __init__(self,driver):
        self.driver=driver

    def is_thank_you_header_visible(self):
        return self.driver.find_element(*self.THANK_YOU_HEADER).is_displayed()