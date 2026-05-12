"""
Page du panier.
"""

from selenium.webdriver.common.by import By
from .base_page import BasePage
import logging

logger = logging.getLogger(__name__)


class CartPage(BasePage):
    """Page du panier d'achats."""
    
    # Localisateurs
    CART_ITEMS_CONTAINER = (By.CLASS_NAME, "cart_list")
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")
    ITEM_QUANTITY = (By.CLASS_NAME, "cart_quantity")
    REMOVE_BUTTON = (By.CSS_SELECTOR, "[data-test^='remove']")
    CONTINUE_SHOPPING = (By.ID, "continue-shopping")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    
    def __init__(self, driver):
        """Initialise la page."""
        super().__init__(driver, base_url="https://www.saucedemo.com")
    
    def is_cart_displayed(self) -> bool:
        """Vérifie qu'on est sur la page du panier."""
        return self.is_element_displayed(self.CART_ITEMS_CONTAINER)
    
    def get_cart_items_count(self) -> int:
        """Compte les articles du panier."""
        items = self.find_elements(self.CART_ITEMS)
        count = len(items)
        logger.info(f"{count} articles")
        return count
    
    def get_cart_item_names(self) -> list:
        """Récupère les noms des articles du panier."""
        items = self.find_elements(self.CART_ITEMS)
        names = []
        for item in items:
            try:
                name = item.find_element(By.CLASS_NAME, "inventory_item_name").text
                names.append(name)
            except:
                continue
        logger.info(f"{len(names)} noms récupérés")
        return names
    
    def get_total_price(self) -> str:
        """
        Récupère le sous-total du panier.
        """
        try:
            subtotal_label = self.find_elements(By.CSS_SELECTOR, ".summary_subtotal_label")
            if subtotal_label:
                text = subtotal_label[0].text
                price = text.split("$")[1] if "$" in text else text
                logger.info(f"Total: ${price}")
                return price
        except:
            logger.warning("Total pas trouvé")
        return ""
    
    def remove_item_from_cart(self, item_index: int = 0) -> None:
        """
        Retire un article du panier.
        """
        items = self.find_elements(self.CART_ITEMS)
        if item_index < len(items):
            item = items[item_index]
            remove_btn = item.find_element(By.CSS_SELECTOR, "[data-test^='remove']")
            remove_btn.click()
            logger.info(f"Article retiré")
        else:
            logger.warning(f"Article {item_index} pas found")
    
    def continue_shopping(self) -> None:
        """Retourne au catalogue."""
        self.click_element(self.CONTINUE_SHOPPING)
        logger.info("Retour au catalogue")
    
    def checkout(self) -> None:
        """Passe au paiement."""
        self.click_element(self.CHECKOUT_BUTTON)
        logger.info("Paiement lancé")
    
    def is_cart_empty(self) -> bool:
        """Vérifie si le panier est vide."""
        items = self.find_elements(self.CART_ITEMS)
        is_empty = len(items) == 0
        logger.info(f"Panier {'vide' if is_empty else 'non vide'}")
        return is_empty
