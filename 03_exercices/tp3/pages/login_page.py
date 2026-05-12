"""
Page de login du site.
"""

from selenium.webdriver.common.by import By
from .base_page import BasePage
import logging

logger = logging.getLogger(__name__)


class LoginPage(BasePage):
    """Page pour se connecter."""
    
    # Localisateurs
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")
    
    def __init__(self, driver):
        """Initialise la page."""
        super().__init__(driver, base_url="https://www.saucedemo.com")
    
    def load(self) -> None:
        """Ouvre la page de login."""
        self.navigate_to_page("")
        logger.info("Page de login ouverte")
    
    def login(self, username: str, password: str) -> None:
        """
        Se connecte avec les identifiants donnés.
        """
        logger.info(f"Connexion avec: {username}")
        self.send_keys_to_element(self.USERNAME_INPUT, username)
        self.send_keys_to_element(self.PASSWORD_INPUT, password)
        self.click_element(self.LOGIN_BUTTON)
    
    def is_login_page(self) -> bool:
        """Vérifie qu'on est sur la page de login."""
        return self.is_element_displayed(self.LOGIN_BUTTON)
    
    def get_error_message(self) -> str:
        """Récupère le message d'erreur."""
        try:
            error_text = self.get_text(self.ERROR_MESSAGE)
            logger.info(f"Erreur: {error_text}")
            return error_text
        except:
            return ""
