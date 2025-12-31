import pytest

from page_dashboard import DashBoardPage
from page_login import LoginPage
from data_login import test_login_data

@pytest.mark.regression
def test_user_login_valid_credentials(setup_teardown_):
    driver = setup_teardown_
    login_page = LoginPage(driver)
    login_page.login(*test_login_data[0]["valid login credentials"][0:2])

    dashboard_page = DashBoardPage(driver)
    dashboard_page.assert_on_dashboard(test_login_data[0]["valid login credentials"][2])

def test_user_login_valid_username_invalid_password(setup_teardown_):
    driver = setup_teardown_
    login_page = LoginPage(driver)
    login_page.login(*test_login_data[1]["valid username but invalid password"][0:2])
    login_page.get_incorrect_credentials_error_message_and_logout_success_text(test_login_data[1]["valid username but invalid password"][2])

def test_user_login_invalid_username_valid_password(setup_teardown_):
    driver = setup_teardown_
    login_page = LoginPage(driver)
    login_page.login(*test_login_data[2]["invalid username but valid password"][0:2])
    login_page.get_incorrect_credentials_error_message_and_logout_success_text(test_login_data[2]["invalid username but valid password"][2])

def test_invalid_username_invalid_password(setup_teardown_):
    driver = setup_teardown_
    login_page = LoginPage(driver)
    login_page.login(*test_login_data[3]["invalid username and invalid password"][0:2])
    login_page.get_incorrect_credentials_error_message_and_logout_success_text(test_login_data[3]["invalid username and invalid password"][2])

def test_blank_username_blank_password(setup_teardown_):
    driver = setup_teardown_
    login_page = LoginPage(driver)
    login_page.login(*test_login_data[4]["blank username and blank password"][0:2])
    login_page.get_blank_credentials_help_message(test_login_data[4]["blank username and blank password"][2])

def test_valid_username_blank_password(setup_teardown_):
    driver = setup_teardown_
    login_page = LoginPage(driver)
    login_page.login(*test_login_data[5]["valid username and blank password"][0:2])
    login_page.get_blank_credentials_help_message(test_login_data[5]["valid username and blank password"][2])

def test_blank_username_valid_password(setup_teardown_):
    driver = setup_teardown_
    login_page = LoginPage(driver)
    login_page.login(*test_login_data[6]["blank username and valid password"][0:2])
    login_page.get_blank_credentials_help_message(test_login_data[6]["blank username and valid password"][2])
