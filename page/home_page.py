from assertpy import assert_that, soft_assertions
from locator.locators import HomeLocators
from selenium.webdriver.support.wait import WebDriverWait

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def goToHome(self):
        self.driver.get("https://emag.ro")
        self.driver.maximize_window()

    def verifyLogo(self):
        homeLogo = self.driver.find_element(*HomeLocators.homeLogo)
        with soft_assertions():
            assert_that(homeLogo).is_true()
            print("✅ Logo verification passed!")

    def verifyTitle(self):
        homeTitle = self.driver.title
        expectedTitle = "eMAG.ro - Căutarea nu se oprește niciodată"
        with soft_assertions():
            assert_that(homeTitle).is_equal_to(expectedTitle)
            print(f"✅ Title verification passed! Found: '{homeTitle}'")


