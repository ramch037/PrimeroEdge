from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class SettingsPage:
    def __init__(self, driver):
        self.driver = driver

        #elements
        self.sites_and_users_button = (By.XPATH, '//span[text()="Sites and Users"]')
        self.users_link = (By.LINK_TEXT, 'Users')

    def click_sites_and_users_button(self):
        self.driver.find_element(*self.sites_and_users_button).click()

    def click_users_link(self):
        self.driver.find_element(*self.users_link).click()