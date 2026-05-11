"""
Factory (fabrique) de driver Chrome partagé pour TP2.
Centralise la configuration du driver pour tous les tests.
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def create_chrome_driver(headless=False, maximize=True):
    """Créer un driver Chrome configuré pour TP2 avec les options standards."""
    options = Options()
    if not headless:
        options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-infobars")
    prefs = {
        "profile.password_manager_leak_detection": False,
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
    }
    options.add_experimental_option("prefs", prefs)
    if headless:
        options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    if maximize:
        driver.maximize_window()
    return driver
