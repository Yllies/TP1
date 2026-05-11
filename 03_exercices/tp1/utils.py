"""
Utilitaires partagés pour TP1
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_chrome_driver(headless=False, maximize=True):
    """
    Créer et retourner un driver Chrome avec les options configurées
    
    Args:
        headless: exécuter en mode headless (sans interface)
        maximize: maximiser la fenêtre
    
    Returns:
        WebDriver Chrome configuré
    """
    options = Options()
    
    if not headless:
        options.add_argument("--start-maximized")
    
    options.add_argument("--disable-notifications")
    
    # Préférences pour désactiver les alertes de fuites de mot de passe
    prefs = {
        "profile.password_manager_leak_detection": False,
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    }
    options.add_experimental_option("prefs", prefs)
    
    if headless:
        options.add_argument("--headless")
    
    driver = webdriver.Chrome(options=options)
    
    if maximize:
        driver.maximize_window()
    
    return driver
