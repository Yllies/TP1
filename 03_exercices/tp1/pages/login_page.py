"""
Page Object pour la page de login
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    """Page Object pour l'authentification"""
    
    # Locators
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    LOGOUT_BUTTON = (By.LINK_TEXT, "Logout")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".flash.success")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".flash.error")
    PAGE_TITLE = (By.TAG_NAME, "h1")
    
    BASE_URL = "https://the-internet.herokuapp.com/login"
    
    def open(self):
        """Ouvrir la page de login"""
        self.navigate_to(self.BASE_URL)
    
    def is_login_page(self):
        """Vérifier que c'est bien la page de login"""
        url = self.get_current_url()
        # Vérifier l'URL et/ou les éléments de la page
        if "login" in url:
            return True
        # Fallback: vérifier la présence des champs de login
        return self.element_exists(self.USERNAME_INPUT) or self.element_exists(self.PASSWORD_INPUT)
    
    def enter_username(self, username):
        """Saisir le nom d'utilisateur"""
        self.send_keys(self.USERNAME_INPUT, username)
    
    def enter_password(self, password):
        """Saisir le mot de passe"""
        self.send_keys(self.PASSWORD_INPUT, password)
    
    def click_login(self):
        """Cliquer sur le bouton de connexion"""
        self.click_element(self.LOGIN_BUTTON)
    
    def login(self, username, password):
        """
        Effectuer la connexion complète
        
        Args:
            username: nom d'utilisateur
            password: mot de passe
        """
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
    
    def is_success_message_displayed(self):
        """Vérifier que le message de succès est affiché"""
        return self.element_exists(self.SUCCESS_MESSAGE)
    
    def get_success_message(self):
        """Récupérer le texte du message de succès"""
        return self.get_text(self.SUCCESS_MESSAGE)
    
    def is_logout_button_visible(self):
        """Vérifier que le bouton logout est visible"""
        return self.element_exists(self.LOGOUT_BUTTON)
    
    def click_logout(self):
        """Cliquer sur le bouton logout"""
        self.click_element(self.LOGOUT_BUTTON)
    
    def is_error_message_displayed(self):
        """Vérifier qu'un message d'erreur est affiché"""
        return self.element_exists(self.ERROR_MESSAGE)
