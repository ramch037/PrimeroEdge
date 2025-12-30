import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class DashBoardPage:
    def __init__(self, driver):
        self.driver = driver

        self.region_selection_element = (By.ID, 'ctl00_HeaderBanner_btnDistrictName')
        self.realm_selector = (By.ID, 'ctl00_UserContentArea_RealmRegionSelector1_RealmDropDownList_Input')
        self.central_selector = (By.XPATH, '//div[@id="ctl00_UserContentArea_RealmRegionSelector1_RealmDropDownList_DropDown"]/div/ul/li[text()="Central"]')
        self.submit_button = (By.ID, "ctl00_UserContentArea_RealmRegionSelector1_SubmitButton")
        self.workspace_text = (By.ID, 'ctl00_HorizontalBar_HorizontalBarLbl')


    def select_region(self):
        self.driver.find_element(*self.region_selection_element).click()
        self.driver.find_element(*self.realm_selector).click()
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.visibility_of_element_located(self.central_selector))
        self.driver.find_element(*self.central_selector).click()
        self.driver.find_element(*self.submit_button).click()


    def assert_on_dashboard(self, text):
        workspace_text = self.driver.find_element(*self.workspace_text).text
        assert workspace_text == text
        print("Successfully logged in and on dashboard")
