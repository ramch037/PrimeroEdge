import pytest

from page_add_user import AddUserPage
from page_dashboard import DashBoardPage
from page_header import HeaderPage
from page_login import LoginPage
from page_manage_users import ManageUsersPage
from page_settings import SettingsPage
from data_login import test_login_data

def test_add_new_user(setup_teardown_):
    driver = setup_teardown_
    login_page = LoginPage(driver)
    dashboard_page = login_page.login(*test_login_data[0]["valid login credentials"][0:2])
    dashboard_page.select_region()

    header = HeaderPage(driver)
    header.click_settings_button()

    settings_page = SettingsPage(driver)
    settings_page.click_sites_and_users_button()
    settings_page.click_users_link()

    users_manage_page = ManageUsersPage(driver)
    users_manage_page.click_user_add_button()

    add_user_page = AddUserPage(driver)
    add_user_page.enter_user_details_mandatory("RamaKrish2906", "Ramakrishna", "Chimmili", "State")


def test_search_user_details(setup_teardown_):
    driver = setup_teardown_
    login_page = LoginPage(driver)
    login_page.login("cssupport", "password")

    dashboard_page = DashBoardPage(driver)
    dashboard_page.select_region()

    header = HeaderPage(driver)
    header.click_settings_button()

    settings_page = SettingsPage(driver)
    settings_page.click_sites_and_users_button()
    settings_page.click_users_link()

    users_manage_page = ManageUsersPage(driver)
    users_manage_page.type_in_and_press_enter_to_search_user_username_textbox("test12")




