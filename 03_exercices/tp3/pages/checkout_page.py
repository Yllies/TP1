"""
Page de paiement.
"""

from selenium.webdriver.common.by import By
from .base_page import BasePage
import logging

logger = logging.getLogger(__name__)


class CheckoutPage(BasePage):
    """Page du paiement."""
    
    # Localisateurs - Étape 1: Informations personnelles
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    ZIP_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    CANCEL_BUTTON = (By.ID, "cancel")
    
    # Localisateurs - Étape 2: Aperçu
    CHECKOUT_SUMMARY = (By.CLASS_NAME, "summary_info")
    FINISH_BUTTON = (By.ID, "finish")
    
    # Localisateurs - Étape 3: Confirmation
    COMPLETE_CONTAINER = (By.CLASS_NAME, "complete-container")
    COMPLETE_MESSAGE = (By.CLASS_NAME, "complete-text")
    
    def __init__(self, driver):
        """Initialise la page."""
        super().__init__(driver, base_url="https://www.saucedemo.com")
    
    def fill_checkout_form(self, first_name: str, last_name: str, zip_code: str) -> None:
        """
        Remplit le formulaire de paiement.
        """
        logger.info(f"Formulaire: {first_name} {last_name}, {zip_code}")
        self.send_keys_to_element(self.FIRST_NAME_INPUT, first_name)
        self.send_keys_to_element(self.LAST_NAME_INPUT, last_name)
        self.send_keys_to_element(self.ZIP_CODE_INPUT, zip_code)
        logger.info(f"Formulaire rempli")
    
    def continue_to_overview(self) -> None:
        """Passe à l'aperçu."""
        self.click_element(self.CONTINUE_BUTTON)
        logger.info("Aperçu affiché")
    
    def is_checkout_form_displayed(self) -> bool:
        """Vérifie qu'on est sur le formulaire."""
        return self.is_element_displayed(self.FIRST_NAME_INPUT)
    
    def is_checkout_overview_displayed(self) -> bool:
        """Vérifie qu'on est sur l'aperçu."""
        return self.is_element_displayed(self.CHECKOUT_SUMMARY)
    
    def finish_checkout(self) -> None:
        """Finalise la commande."""
        self.click_element(self.FINISH_BUTTON)
        logger.info("Commande finalisée")
    
    def is_order_complete(self) -> bool:
        """Vérifie que la commande est complétée."""
        return self.is_element_displayed(self.COMPLETE_CONTAINER)
    
    def get_completion_message(self) -> str:
        """Récupère le message de fin."""
        try:
            message = self.get_text(self.COMPLETE_MESSAGE)
            logger.info(f"Message: {message}")
            return message
        except:
            logger.warning("Message pas found")
            return ""
    
    def cancel_checkout(self) -> None:
        """Annule le paiement."""
        self.click_element(self.CANCEL_BUTTON)
        logger.info("Paiement annulé")
