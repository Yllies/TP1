"""
Tests pour Sauce Demo - scénarios d'achat.
"""

import sys
import os

# Ajouter le répertoire parent au chemin pour les imports
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

from utils.driver_factory import create_driver, close_driver
from utils.logger_config import setup_logger
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from selenium.webdriver.common.by import By

logger = setup_logger("tp3_test")

# Identifiants de test valides
VALID_USER = "standard_user"
VALID_PASSWORD = "secret_sauce"
INVALID_USER = "invalid_user"
INVALID_PASSWORD = "wrong_password"


def test_scenario_1_login_success():
    """Test: connexion avec bons identifiants."""
    logger.info("-" * 50)
    logger.info("TEST 1: Connexion valide")
    logger.info("-" * 50)
    
    driver = None
    try:
        driver = create_driver(headless=False, disable_notifications=True)
        
        login_page = LoginPage(driver)
        login_page.load()
        login_page.login(VALID_USER, VALID_PASSWORD)
        
        import time
        time.sleep(2)
        inventory_page = InventoryPage(driver)
        assert inventory_page.is_inventory_displayed(), "Catalog pas visible"
        
        logger.info("Test 1 OK - Connexion réussie")
        
    except AssertionError as e:
        logger.error(f"Test 1 FAIL: {e}")
        if driver:
            inventory_page.screenshot("test_1_fail")
        raise
    except Exception as e:
        logger.error(f"Test 1 ERROR: {e}")
        if driver:
            inventory_page.screenshot("test_1_error")
        raise
    finally:
        close_driver(driver)


def test_scenario_2_login_invalid():
    """Test: connexion avec mauvais identifiants."""
    logger.info("-" * 50)
    logger.info("TEST 2: Connexion invalide")
    logger.info("-" * 50)
    
    driver = None
    try:
        driver = create_driver(headless=False, disable_notifications=True)
        
        login_page = LoginPage(driver)
        login_page.load()
        login_page.login(INVALID_USER, INVALID_PASSWORD)
        
        import time
        time.sleep(1)
        
        assert login_page.is_login_page(), "Devrait rester sur login"
        
        error_msg = login_page.get_error_message()
        assert error_msg, "Message d'erreur requis"
        
        logger.info("Test 2 OK - Erreur correctement gérée")
        
    except AssertionError as e:
        logger.error(f"Test 2 FAIL: {e}")
        if driver:
            login_page.screenshot("test_2_fail")
        raise
    finally:
        close_driver(driver)


def test_scenario_3_add_products_to_cart():
    """Test: ajouter des produits au panier."""
    logger.info("-" * 50)
    logger.info("TEST 3: Ajout de produits")
    logger.info("-" * 50)
    
    driver = None
    try:
        driver = create_driver(headless=False, disable_notifications=True)
        
        login_page = LoginPage(driver)
        login_page.load()
        login_page.login(VALID_USER, VALID_PASSWORD)
        
        import time
        time.sleep(2)
        
        inventory_page = InventoryPage(driver)
        assert inventory_page.is_inventory_displayed(), "Catalog pas visible"
        
        product_count = inventory_page.get_product_count()
        logger.info(f"{product_count} produits dispo")
        
        inventory_page.add_product_to_cart(0)
        inventory_page.add_product_to_cart(1)
        
        time.sleep(1)
        
        cart_count = inventory_page.get_cart_badge_count()
        assert cart_count == 2, f"Badge devrait montrer 2, mais affiche {cart_count}"
        
        logger.info("Test 3 OK - Produits ajoutés")
        
    except AssertionError as e:
        logger.error(f"Test 3 FAIL: {e}")
        if driver:
            inventory_page.screenshot("test_3_fail")
        raise
    finally:
        close_driver(driver)


def test_scenario_4_view_cart_and_checkout():
    """Test: panier et paiement."""
    logger.info("-" * 50)
    logger.info("TEST 4: Panier et paiement")
    logger.info("-" * 50)
    
    driver = None
    try:
        driver = create_driver(headless=False, disable_notifications=True)
        
        # Login et ajouter des produits
        login_page = LoginPage(driver)
        login_page.load()
        login_page.login(VALID_USER, VALID_PASSWORD)
        
        import time
        time.sleep(2)
        
        inventory_page = InventoryPage(driver)
        inventory_page.add_product_by_name("Sauce Labs Backpack")
        time.sleep(1)
        
        inventory_page.go_to_cart()
        time.sleep(1)
        
        cart_page = CartPage(driver)
        assert cart_page.is_cart_displayed(), "Panier pas visible"
        
        items_count = cart_page.get_cart_items_count()
        assert items_count == 1, f"Devrait avoir 1 article, mais en a {items_count}"
        
        logger.info(f"{items_count} article dans le panier")
        
        cart_page.checkout()
        time.sleep(1)
        
        checkout_page = CheckoutPage(driver)
        assert checkout_page.is_checkout_form_displayed(), "Formulaire pas visible"
        
        checkout_page.fill_checkout_form("Jean", "Dupont", "75000")
        checkout_page.continue_to_overview()
        time.sleep(1)
        
        assert checkout_page.is_checkout_overview_displayed(), "Aperçu pas visible"
        
        logger.info("Test 4 OK - Panier et formulaire OK")
        
    except AssertionError as e:
        logger.error(f"Test 4 FAIL: {e}")
        if driver:
            checkout_page.screenshot("test_4_fail")
        raise
    finally:
        close_driver(driver)


def test_scenario_5_complete_purchase():
    """Test: achat complet."""
    logger.info("-" * 50)
    logger.info("TEST 5: Achat complet")
    logger.info("-" * 50)
    
    driver = None
    try:
        driver = create_driver(headless=False, disable_notifications=True)
        
        # Login
        login_page = LoginPage(driver)
        login_page.load()
        login_page.login(VALID_USER, VALID_PASSWORD)
        
        import time
        time.sleep(2)
        
        # Ajouter un produit
        inventory_page = InventoryPage(driver)
        inventory_page.add_product_to_cart(0)
        time.sleep(1)
        
        # Aller au panier
        inventory_page.go_to_cart()
        time.sleep(1)
        
        # Paiement
        cart_page = CartPage(driver)
        cart_page.checkout()
        time.sleep(1)
        
        checkout_page = CheckoutPage(driver)
        checkout_page.fill_checkout_form("Marie", "Martin", "69000")
        checkout_page.continue_to_overview()
        time.sleep(2)
        
        # Finaliser la commande
        checkout_page.finish_checkout()
        time.sleep(3)  # Plus de temps pour la page de confirmation
        
        # Vérifier la confirmation - attendre l'élément
        try:
            completion_element = checkout_page.wait_for_element(checkout_page.COMPLETE_CONTAINER, timeout=5)
            completion_msg = checkout_page.get_completion_message()
            logger.info(f"Confirmation OK")
            
            checkout_page.screenshot("test_5_success")
            
            logger.info("Test 5 OK - Achat complet")
        except:
            logger.info("Vérification via l'URL...")
            if "checkout-complete" in driver.current_url:
                logger.info("URL de confirmation OK")
                checkout_page.screenshot("test_5_success")
                logger.info("Test 5 OK - Confirmation URL")
            else:
                raise AssertionError("Page de confirmation pas atteinte")
        
    except AssertionError as e:
        logger.error(f"Test 5 FAIL: {e}")
        if driver:
            checkout_page.screenshot("test_5_fail")
        raise
    finally:
        close_driver(driver)


if __name__ == "__main__":
    logger.info("\n" + "-" * 50)
    logger.info("Tests Sauce Demo")
    logger.info("-" * 50 + "\n")
    
    tests = [
        ("Test 1", test_scenario_1_login_success),
        ("Test 2", test_scenario_2_login_invalid),
        ("Test 3", test_scenario_3_add_products_to_cart),
        ("Test 4", test_scenario_4_view_cart_and_checkout),
        ("Test 5", test_scenario_5_complete_purchase),
    ]
    
    passed = 0
    failed = 0
    
    for test_name, test_func in tests:
        try:
            test_func()
            passed += 1
        except Exception as e:
            failed += 1
            logger.error(f"{test_name} échoué\n")
    
    logger.info("\n" + "-" * 50)
    logger.info("Résumé")
    logger.info("-" * 50)
    logger.info(f"OK: {passed}")
    logger.info(f"KO: {failed}")
    logger.info(f"Total: {passed + failed}")
    logger.info("-" * 50 + "\n")
