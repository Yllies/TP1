"""
Script de test autonome sans framework
"""
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage
from pages.dropdown_page import DropdownPage
from pages.add_remove_page import AddRemovePage

USERNAME = "tomsmith"
PASSWORD = "SuperSecretPassword!"


def create_driver(headless=False):
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    prefs = {
        "profile.password_manager_leak_detection": False,
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
    }
    options.add_experimental_option("prefs", prefs)
    if headless:
        options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    return driver


def run_test(test_name, func):
    print(f"RUNNING: {test_name}")
    func()
    print(f"PASS: {test_name}\n")


def test_01_login_page_opens(driver):
    login_page = LoginPage(driver)
    login_page.open()
    assert login_page.is_login_page(), "La page de login n'est pas affichée"


def test_02_login_success(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(USERNAME, PASSWORD)
    time.sleep(2)
    assert login_page.is_success_message_displayed(), "Le message de succès n'est pas affiché"


def test_03_logout_button_visible(driver):
    login_page = LoginPage(driver)
    assert login_page.is_logout_button_visible(), "Le bouton logout n'est pas visible"


def test_04_logout(driver):
    login_page = LoginPage(driver)
    login_page.click_logout()
    time.sleep(1)
    assert login_page.is_login_page(), "La page de login n'est pas affichée après logout"


def test_05_dropdown_present(driver):
    dropdown_page = DropdownPage(driver)
    dropdown_page.open()
    assert dropdown_page.is_dropdown_present(), "La liste déroulante n'est pas présente"


def test_06_select_option_1(driver):
    dropdown_page = DropdownPage(driver)
    dropdown_page.select_option_by_text("Option 1")
    assert dropdown_page.is_option_selected("Option 1"), "Option 1 n'est pas sélectionnée"


def test_07_select_option_2(driver):
    dropdown_page = DropdownPage(driver)
    dropdown_page.select_option_by_text("Option 2")
    assert dropdown_page.is_option_selected("Option 2"), "Option 2 n'est pas sélectionnée"


def test_08_add_elements(driver):
    add_remove_page = AddRemovePage(driver)
    add_remove_page.open()
    add_remove_page.add_elements(3)
    time.sleep(1)
    assert add_remove_page.are_delete_buttons_visible(3), "3 boutons Delete ne sont pas présents"


def test_09_delete_one_element(driver):
    add_remove_page = AddRemovePage(driver)
    add_remove_page.delete_first_element()
    time.sleep(0.5)
    assert add_remove_page.are_delete_buttons_visible(2), "Il n'y a pas 2 boutons Delete"


def test_10_delete_all_elements(driver):
    add_remove_page = AddRemovePage(driver)
    add_remove_page.delete_all_elements()
    time.sleep(0.5)
    assert add_remove_page.are_all_elements_deleted(), "Il reste des boutons Delete"


def main():
    driver = get_chrome_driver(headless=False, maximize=True)
    try:
        tests = [
            ("Login page opens", test_01_login_page_opens),
            ("Login success", test_02_login_success),
            ("Logout button visible", test_03_logout_button_visible),
            ("Logout works", test_04_logout),
            ("Dropdown present", test_05_dropdown_present),
            ("Select Option 1", test_06_select_option_1),
            ("Select Option 2", test_07_select_option_2),
            ("Add 3 elements", test_08_add_elements),
            ("Delete one element", test_09_delete_one_element),
            ("Delete all elements", test_10_delete_all_elements),
        ]

        for name, test_func in tests:
            run_test(name, lambda func=test_func: func(driver))

        print("ALL TESTS COMPLETED")
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
