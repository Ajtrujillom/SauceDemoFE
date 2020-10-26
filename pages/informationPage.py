from selenium.webdriver.common.by import By


class InformationPage():

    FIRST_NAME_TEXT_BOX = (By.CSS_SELECTOR, ".form_input#first-name")
    LAST_NAME_TEXT_BOX = (By.CSS_SELECTOR, ".form_input#last-name")
    ZIP_TEXT_BOX = (By.CSS_SELECTOR, ".form_input#postal-code")
    CONTINUE_BTN = (By.CSS_SELECTOR, ".btn_primary")
    ERROR_MSG = (By.CSS_SELECTOR, "h3[data-test='error']")

    def __init__(self, driver):
        self.driver = driver

    def fillfirstname(self, first_name):
        fill_first_name = self.driver.find_element(*self.FIRST_NAME_TEXT_BOX).send_keys(first_name)

    def fillLastname(self, last_name):
        fill_last_name = self.driver.find_element(*self.LAST_NAME_TEXT_BOX).send_keys(last_name)

    def fillzipcode(self, zip):
        fill_zip = self.driver.find_element(*self.ZIP_TEXT_BOX).send_keys(zip)

    def clickContinueBtn(self):
        click_continue_btn = self.driver.find_element(*self.CONTINUE_BTN)
        click_continue_btn.click()

    def isErrorMsgVisible(self):
        return self.driver.find_element(*self.ERROR_MSG).is_displayed()


