from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from page_login import LoginPage


class HeaderPage:
    def __init__(self, driver):
        self.driver = driver

        #elements
        self.hamburger_icon = (By.XPATH , '//img[@alt="Minimize Menu"]')
        self.settings_button = (By.ID, 'ctl00_HeaderBanner_anchorsystemTextBoard')
        self.ellipsis_button = (By.XPATH, '//img[@title="More"]')
        self.logout_button = (By.XPATH, '//img[@class="LogoutIcon"]')

    #methods..Actions
    def click_hamburger_icon(self):
        self.driver.find_element(*self.hamburger_icon).click()

    def click_settings_button(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located(self.settings_button))
        self.driver.find_element(*self.settings_button).click()

    def click_ellipsis_button(self):
        self.driver.find_element(*self.ellipsis_button).click()

    def click_logout_button(self):
        self.driver.find_element(*self.logout_button).click()
        login_page = LoginPage(self.driver)
        return login_page