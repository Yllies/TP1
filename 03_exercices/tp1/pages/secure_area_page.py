"""
Page Object pour la zone sécurisée après authentification
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SecureAreaPage(BasePage):
    """Page Object pour la zone sécurisée"""
    
    # Locators
    WELCOME_MESSAGE = (By.TAG_NAME, "h2")
    LOGOUT_BUTTON = (By.LINK_TEXT, "Logout")
    
    BASE_URL = "https://the-internet.herokuapp.com/secure"
    
    def is_secure_area_displayed(self):
        """Vérifier que la zone sécurisée est affichée"""
        return "secure" in self.get_current_url()
    
    def get_welcome_message(self):
        """Récupérer le message de bienvenue"""
        return self.get_text(self.WELCOME_MESSAGE)
    
    def is_welcome_message_displayed(self):
        """Vérifier que le message de bienvenue contient 'Welcome'"""
        message = self.get_welcome_message()
        return "Welcome" in message or "Secure Area" in message
    
    def is_logout_button_visible(self):
        """Vérifier que le bouton logout est visible"""
        return self.element_exists(self.LOGOUT_BUTTON)
    
    def click_logout(self):
        """Cliquer sur le bouton logout"""
        self.click_element(self.LOGOUT_BUTTON)
