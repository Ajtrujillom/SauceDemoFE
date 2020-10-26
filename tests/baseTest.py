import json
import unittest

import HtmlTestRunner
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class BaseTest(unittest.TestCase):
    #calling data provider
    with open("tests/data.json", "r") as read_file:
        dataProvider = json.load(read_file)
    def getBrowser(self):
        browser=self.dataProvider["browser"]
        if browser == "chrome":
            return webdriver.Chrome(ChromeDriverManager().install())
        if browser == "firefox":
            return webdriver.Firefox(executable_path=GeckoDriverManager().install())
        else:
            return webdriver.Chrome(ChromeDriverManager().install())

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

    if __name__ == '__main__':
        unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))
