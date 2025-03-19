import sys
sys.stdout = open(1, 'w', encoding='utf-8')  # Redirect output to the correct stream
print("✅ Test execution started!")

from selenium import webdriver
import path_config #Nu uita sa modifici path-ul in fisierul path_config.py cu folderul proiectului tau
import unittest
from page.about_page import AboutPage as AP


class ProductTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.aboutPage = AP(self.driver)

    def test_title(self):
        self.aboutPage.goToAbout()
        self.aboutPage.verifyTitle()

    def test_aboutNav(self):
        self.aboutPage.goToAbout()
        expectedNavItems = ["Grupul eMAG", "eMAG Teams", "Sustenabilitate", "Media"]
        self.aboutPage.verifyNavigation(expectedNavItems)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()    
