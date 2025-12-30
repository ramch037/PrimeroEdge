from selenium.webdriver.common.by import By

from page_dashboard import DashBoardPage


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

        self.username = (By.XPATH, '//input[@id="UserNameTextBox"]')
        self.password = (By.ID, 'PasswordTextBox')
        self.sign_in_button = (By.ID, 'LoginButton')
        self.incorrect_credentials_error_message = (By.XPATH, '//div[@id="loginmessages"]/span')
        self.blank_credentials_help_message = (By.XPATH, '//div[@id="loginmessages"]/div')
        self.logout_success_message = (By.XPATH, '//span[@id="lblLogOut"]')

    def login(self, username, password):
        self.driver.find_element(*self.username).send_keys(username)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.sign_in_button).click()
        dashboard_page = DashBoardPage(self.driver)
        return dashboard_page

    def get_incorrect_credentials_error_message_and_logout_success_text(self, error_message_expected):
        error_message = self.driver.find_element(*self.incorrect_credentials_error_message).text
        assert error_message == error_message_expected

    def get_blank_credentials_help_message(self, help_message_expected):
        help_message = self.driver.find_element(*self.blank_credentials_help_message).text
        print(help_message)
        assert help_message_expected == help_message