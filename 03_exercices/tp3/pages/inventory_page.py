"""
Page avec la liste des produits.
"""

from selenium.webdriver.common.by import By
from .base_page import BasePage
import logging

logger = logging.getLogger(__name__)


class InventoryPage(BasePage):
    """Page du catalogue de produits."""
    
    # Localisateurs
    INVENTORY_CONTAINER = (By.CLASS_NAME, "inventory_list")
    PRODUCT_ITEMS = (By.CLASS_NAME, "inventory_item")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".inventory_item_name")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".inventory_item_price")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "[data-test^='add-to-cart']")
    REMOVE_BUTTON = (By.CSS_SELECTOR, "[data-test^='remove']")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    
    def __init__(self, driver):
        """Initialise la page."""
        super().__init__(driver, base_url="https://www.saucedemo.com")
    
    def is_inventory_displayed(self) -> bool:
        """Vérifie qu'on est sur le catalogue."""
        return self.is_element_displayed(self.INVENTORY_CONTAINER)
    
    def get_product_count(self) -> int:
        """Compte les produits affichés."""
        products = self.find_elements(self.PRODUCT_ITEMS)
        count = len(products)
        logger.info(f"{count} produits")
        return count
    
    def add_product_to_cart(self, product_index: int = 0) -> None:
        """
        Ajoute un produit au panier (par position dans la liste).
        """
        products = self.find_elements(self.PRODUCT_ITEMS)
        if product_index < len(products):
            product = products[product_index]
            add_btn = product.find_element(By.CSS_SELECTOR, "[data-test^='add-to-cart']")
            add_btn.click()
            logger.info(f"Produit ajouté au panier")
        else:
            logger.warning(f"Produit {product_index} pas found")
    
    def add_product_by_name(self, product_name: str) -> None:
        """
        Ajoute un produit au panier (par nom).
        """
        products = self.find_elements(self.PRODUCT_ITEMS)
        for product in products:
            try:
                name_element = product.find_element(By.CSS_SELECTOR, ".inventory_item_name")
                if product_name.lower() in name_element.text.lower():
                    add_btn = product.find_element(By.CSS_SELECTOR, "[data-test^='add-to-cart']")
                    add_btn.click()
                    logger.info(f"'{product_name}' ajouté au panier")
                    return
            except:
                continue
        logger.warning(f"'{product_name}' pas trouvé")
    
    def remove_product_from_cart(self, product_index: int = 0) -> None:
        """
        Retire un produit du panier.
        """
        products = self.find_elements(self.PRODUCT_ITEMS)
        if product_index < len(products):
            product = products[product_index]
            remove_btn = product.find_element(By.CSS_SELECTOR, "[data-test^='remove']")
            remove_btn.click()
            logger.info(f"Produit retiré du panier")
        else:
            logger.warning(f"Produit {product_index} pas found")
    
    def get_cart_badge_count(self) -> int:
        """Compte les articles dans le badge du panier."""
        try:
            badge_text = self.get_text(self.CART_BADGE)
            count = int(badge_text)
            logger.info(f"{count} articles dans le panier")
            return count
        except:
            logger.info("Panier vide")
            return 0
    
    def go_to_cart(self) -> None:
        """Va vers le panier."""
        self.click_element(self.CART_LINK)
        logger.info("Vers le panier")
    
    def open_menu(self) -> None:
        """Ouvre le menu."""
        self.click_element(self.MENU_BUTTON)
        logger.info("Menu ouvert")
    
    def logout(self) -> None:
        """Se déconnecte."""
        self.open_menu()
        self.click_element(self.LOGOUT_LINK)
        logger.info("Déconnecté")
    
    def get_product_names(self) -> list:
        """Récupère les noms de tous les produits."""
        products = self.find_elements(self.PRODUCT_ITEMS)
        names = []
        for product in products:
            try:
                name = product.find_element(By.CSS_SELECTOR, ".inventory_item_name").text
                names.append(name)
            except:
                continue
        logger.info(f"{len(names)} produits récupérés")
        return names
    
    def get_product_prices(self) -> list:
        """Récupère les prix de tous les produits."""
        products = self.find_elements(self.PRODUCT_ITEMS)
        prices = []
        for product in products:
            try:
                price = product.find_element(By.CSS_SELECTOR, ".inventory_item_price").text
                prices.append(price)
            except:
                continue
        logger.info(f"{len(prices)} prix récupérés")
        return prices
