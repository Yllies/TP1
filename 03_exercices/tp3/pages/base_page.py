"""
Page de base avec les méthodes qu'on va réutiliser un peu partout.
"""

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import logging
from datetime import datetime

logger = logging.getLogger(__name__)


class BasePage:
    """Tout ce qu'il faut pour manipuler une page du site."""
    
    def __init__(self, driver: webdriver.Chrome, base_url: str = "https://www.saucedemo.com"):
        """
        Initialise une page avec le driver.
        """
        self.driver = driver
        self.base_url = base_url
        self.wait = WebDriverWait(driver, timeout=10)
        self.actions = ActionChains(driver)
    
    def navigate_to(self, url: str) -> None:
        """Va sur une URL."""
        self.driver.get(url)
        logger.info(f"Accès à {url}")
    
    def navigate_to_page(self, path: str = "") -> None:
        """Va sur une page relative."""
        full_url = f"{self.base_url}{path}"
        self.navigate_to(full_url)
    
    def wait_for_element(self, locator: tuple, timeout: int = 10):
        """Attends qu'un élément apparaisse."""
        wait = WebDriverWait(self.driver, timeout=timeout)
        return wait.until(EC.visibility_of_element_located(locator))
    
    def wait_for_clickable(self, locator: tuple, timeout: int = 10):
        """Attends qu'on puisse cliquer sur un élément."""
        wait = WebDriverWait(self.driver, timeout=timeout)
        return wait.until(EC.element_to_be_clickable(locator))
    
    def find_element(self, locator: tuple):
        """Cherche un élément."""
        return self.driver.find_element(*locator)
    
    def find_elements(self, locator: tuple):
        """Cherche plusieurs éléments."""
        return self.driver.find_elements(*locator)
    
    def click_element(self, locator: tuple) -> None:
        """Clique sur un élément."""
        element = self.wait_for_clickable(locator)
        element.click()
        logger.info(f"Clic sur {locator}")
    
    def send_keys_to_element(self, locator: tuple, keys: str) -> None:
        """Tape du texte dans un élément."""
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(keys)
        logger.info(f"Texte saisi: '{keys}'")
    
    def get_text(self, locator: tuple) -> str:
        """Récupère le texte d'un élément."""
        element = self.wait_for_element(locator)
        return element.text
    
    def get_attribute(self, locator: tuple, attribute: str) -> str:
        """Récupère un attribut d'un élément."""
        element = self.wait_for_element(locator)
        return element.get_attribute(attribute)
    
    def is_element_displayed(self, locator: tuple) -> bool:
        """Vérifie si un élément est visible."""
        try:
            element = self.find_element(locator)
            return element.is_displayed()
        except:
            return False
    
    def screenshot(self, filename: str = None) -> str:
        """
        Prend une capture d'écran.
        """
        if not filename:
            filename = f"screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        filepath = f"screenshots/{filename}.png"
        self.driver.save_screenshot(filepath)
        logger.info(f"Capture: {filepath}")
        return filepath
    
    def scroll_to_element(self, locator: tuple) -> None:
        """Défile jusqu'à un élément."""
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        logger.info(f"Scroll jusqu'à {locator}")
