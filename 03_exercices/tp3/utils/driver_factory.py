"""
Config du driver Chrome - tout ce qu'il faut pour lancer les tests.
Une seule place pour configurer le navigateur, pas de duplication.
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import logging

logger = logging.getLogger(__name__)


def create_driver(
    headless: bool = False,
    disable_notifications: bool = True,
    disable_images: bool = False,
    width: int = 1920,
    height: int = 1080,
    start_maximized: bool = True
) -> webdriver.Chrome:
    """
    Lance un driver Chrome comme tu le veux.
    headless=True -> pas de fenêtre, headless=False -> avec fenêtre
    """
    options = Options()
    
    if headless:
        options.add_argument("--headless=new")
    
    if disable_notifications:
        prefs = {"profile.default_content_setting_values.notifications": 2}
        options.add_experimental_option("prefs", prefs)
    
    if disable_images:
        prefs = prefs or {}
        prefs["profile.managed_default_content_settings.images"] = 2
        options.add_experimental_option("prefs", prefs)
    
    if start_maximized and not headless:
        options.add_argument("--start-maximized")
    elif not start_maximized and width and height:
        options.add_argument(f"--window-size={width},{height}")
    
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    
    driver = webdriver.Chrome(options=options)
    logger.info(f"Driver lancé (headless={headless})")
    
    return driver


def close_driver(driver: webdriver.Chrome) -> None:
    """Ferme le driver proprement."""
    if driver:
        driver.quit()
        logger.info("Driver fermé")
