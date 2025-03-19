from selenium.webdriver.common.by import By

class HomeLocators:
    homeLogo = (By.XPATH, "//*[@id='masthead']/div/div/div[1]/a/img")
    homeTitle = (By.TAG_NAME, "title")

class AboutLocators:
    aboutNav = (By.CSS_SELECTOR, "div.center.column ul li a")
    aboutTitle = (By.TAG_NAME, "title")