from data_login import test_login_data
from page_dashboard import DashBoardPage
from page_header import HeaderPage
from page_login import LoginPage


def test_login_and_logout_from_header(setup_teardown_):
    driver = setup_teardown_
    login_page = LoginPage(driver)
    login_page.login(*test_login_data[0]["valid login credentials"][0:2])

    dashboard_page = DashBoardPage(driver)
    dashboard_page.assert_on_dashboard(test_login_data[0]["valid login credentials"][2])

    header_page = HeaderPage(driver)
    header_page.click_ellipsis_button()
    login_page = header_page.click_logout_button()
    login_page.get_incorrect_credentials_error_message_and_logout_success_text("You have been successfully logged out of PrimeroEdge.")
