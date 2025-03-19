from assertpy import assert_that, soft_assertions
from locator.locators import AboutLocators
from selenium.webdriver.support.wait import WebDriverWait


class AboutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def goToAbout(self):
        self.driver.get("https://about.emag.ro/")
        self.driver.maximize_window()
        
    def verifyTitle(self):
        aboutTitle = self.driver.title
        expectedTitle = "Bine ai venit la eMAG - Căutarea nu se oprește niciodată - eMAG"
        with soft_assertions():
            assert_that(aboutTitle).is_equal_to(expectedTitle)
            print(f"✅ Title verification passed! Found: '{aboutTitle}'")

    def getNavigationElements(self):
        navElements = self.driver.find_elements(*AboutLocators.aboutNav)
        return [item.text.strip() for item in navElements]
    
    def verifyNavigation(self, expected_items):
        aboutNav = self.getNavigationElements()
        print(f"🔹 Found navigation items: {aboutNav}")
        with soft_assertions():
            assert_that(aboutNav).contains_only(*expected_items)
            print("✅ Navigation bar verification passed!")