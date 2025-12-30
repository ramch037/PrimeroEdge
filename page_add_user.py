from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class AddUserPage:
    def __init__(self, driver):
        self.driver = driver

        #elements
        self.username = (By.ID, 'ctl00_UserContentArea_ucUserSearch_ucUserDetails_UserNameTextBox')
        self.firstname = (By.ID, 'ctl00_UserContentArea_ucUserSearch_ucUserDetails_FirstnameTextBox')
        self.lastname = (By.ID, 'ctl00_UserContentArea_ucUserSearch_ucUserDetails_LastNameTextBox')
        self.user_status = (By.ID, 'ctl00_UserContentArea_ucUserSearch_ucUserDetails_UpdatePanel2')
        self.user_status_options = (By.XPATH,'//*[@id="ctl00_UserContentArea_ucUserSearch_ucUserDetails_rcbAccessLevel_DropDown"]/div[1]/ul/li[@class="rcbItem"]')

        #metods

    def enter_user_details_mandatory(self, username, firstname, lastname, option_to_select):
        wait = WebDriverWait(self.driver, 20)
        wait.until(expected_conditions.visibility_of_element_located(self.username))
        self.driver.find_element(*self.username).send_keys(username)
        self.driver.find_element(*self.firstname).send_keys(firstname)
        self.driver.find_element(*self.lastname).send_keys(lastname)
        self.driver.find_element(*self.user_status).click()
        wait.until(expected_conditions.visibility_of_element_located(self.user_status_options))
        options = self.driver.find_elements(*self.user_status_options)
        for option in options:
            if option.text == option_to_select:
                option.click()
                break


