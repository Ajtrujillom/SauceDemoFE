from telnetlib import EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from tests.baseTest import BaseTest


class LoginPage:
    USERNAME_INPUT=(By.CSS_SELECTOR, ".form_input#user-name")
    PASSWORD_INPUT=(By.CSS_SELECTOR, ".form_input#password")
    LOGIN_BTN=(By.CSS_SELECTOR, ".btn_action")
    ERROR_MSG=(By.CSS_SELECTOR,"h3[data-test='error']")


    def __init__(self, driver):
        self.driver = driver

    def fillUsernameInput(self,username):
        username_input=self.driver.find_element(*self.USERNAME_INPUT)
        username_input.send_keys(username)

    def fillPassword(self,password):
        password_input=self.driver.find_element(*self.PASSWORD_INPUT)
        password_input.send_keys(password)

    def clickLoginbtn(self):
        login_btn=self.driver.find_element(*self.LOGIN_BTN)
        login_btn.click()
    def isErrorMsgVisible(self):
        error_msg=self.driver.find_element(*self.ERROR_MSG)
        return error_msg.is_displayed()
    def isUsernameInputVisible(self):
        return self.driver.find_element(*self.USERNAME_INPUT).is_displayed()
    def loginStep(self):
        login_page = self
        login_page.driver.get(BaseTest.dataProvider["url"])
        login_page.fillUsernameInput(BaseTest.dataProvider["valid_username"])
        login_page.fillPassword(BaseTest.dataProvider["valid_password"])
        login_page.clickLoginbtn()





