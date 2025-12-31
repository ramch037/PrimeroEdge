from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class ManageUsersPage:
    def __init__(self, driver):
        self.driver = driver

        #elements
        self.user_add_button = (By.ID, 'ctl00_UserContentArea_ucUserSearch_ltbnAddUser')
        self.search_user_username_textbox = (By.ID, 'ctl00_UserContentArea_ucUserSearch_UsersRadGrid_ctl00_ctl02_ctl02_FilterTextBox_UserName')

    def click_user_add_button(self):
        ele = self.driver.find_element(*self.user_add_button)
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.element_to_be_clickable(ele))
        ele.click()

    def type_in_and_press_enter_to_search_user_username_textbox(self, username):
        ele = self.driver.find_element(*self.search_user_username_textbox)
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.element_to_be_clickable(ele))
        ele.send_keys(username)
        ele.send_keys(Keys.ENTER)
