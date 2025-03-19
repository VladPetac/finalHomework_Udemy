import sys
sys.stdout = open(1, 'w', encoding='utf-8')  # Redirect output to the correct stream
print("✅ Test execution started!")

from selenium import webdriver
import path_config #Nu uita sa modifici path-ul in fisierul path_config.py cu folderul proiectului tau
import unittest
from page.home_page import HomePage as HP

class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.homePage = HP(self.driver)

    def test_logo(self):
        self.homePage.goToHome()
        self.homePage.verifyLogo()


    def test_title(self):
        self.homePage.goToHome()
        self.homePage.verifyTitle()


    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()    
