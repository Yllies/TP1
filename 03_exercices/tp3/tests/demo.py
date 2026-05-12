"""
Demo pour montrer le TP3 en action.
"""

import sys
import os

# Ajouter le répertoire parent au chemin
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

from utils.driver_factory import create_driver, close_driver
from utils.logger_config import setup_logger
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

logger = setup_logger("demo")


def demo_reusable_code():
    """Montre comment tout se réutilise sans duplication."""
    
    logger.info("\n" + "-" * 50)
    logger.info("Demo - TP3 en action")
    logger.info("-" * 50 + "\n")
    
    logger.info("1. Driver créé via factory (réutilisable)")
    driver = create_driver(headless=False, disable_notifications=True)
    
    try:
        logger.info("2. Page objects avec BasePage (pas de duplication)")
        
        login_page = LoginPage(driver)
        login_page.load()
        login_page.login("standard_user", "secret_sauce")
        
        import time
        time.sleep(2)
        
        inventory_page = InventoryPage(driver)
        
        logger.info("3. Infos récupérées:")
        logger.info(f"   Catalog visible: {inventory_page.is_inventory_displayed()}")
        logger.info(f"   Produits: {inventory_page.get_product_count()}")
        
        inventory_page.add_product_to_cart(0)
        time.sleep(1)
        
        logger.info(f"   Panier: {inventory_page.get_cart_badge_count()} articles")
        
        inventory_page.go_to_cart()
        time.sleep(1)
        
        cart_page = CartPage(driver)
        logger.info(f"   Articles visibles: {cart_page.get_cart_items_count()}")
        logger.info(f"   Noms: {cart_page.get_cart_item_names()}")
        
        logger.info("\nDemo OK")
        logger.info("\nRésumé:")
        logger.info("  • Driver factory: un seul endroit")
        logger.info("  • BasePage: méthodes réutilisables")
        logger.info("  • Page objects: encapsulation")
        logger.info("  • Zéro duplication\n")
        
    except Exception as e:
        logger.error(f"Erreur: {e}")
        inventory_page.screenshot("demo_error")
    finally:
        close_driver(driver)


if __name__ == "__main__":
    demo_reusable_code()
