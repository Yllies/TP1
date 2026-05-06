# ## Exercice 7 : Localiser des Éléments avec XPath
# **Site**: practicesoftwaretesting.com
# **Compétences**: Utiliser les XPath
# **Instructions**:
# 1. Ouvrez le navigateur
# 2. Accédez à https://practicesoftwaretesting.com/
# 3. Attendez que les produits se chargent
# 4. Localisez les cartes produit en utilisant XPath avec `contains()` pour la classe
# 5. Localisez les titres de produits en utilisant XPath (Testez différentes variations de XPath: position, not(), descendant)
# 6. Vérifiez que tous les éléments sont trouvés
# 7. Fermez le navigateur
# **Validation**:
# - Tous les XPath fonctionnent
# - Les éléments sont correctement localisés
# - Les variantes de XPath fonctionnent


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_css_selectors():
    """
    Localise des éléments en utilisant des sélecteurs CSS sur un site e-commerce
    """
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        # Accéder au site
        driver.get("https://practicesoftwaretesting.com/")
        print("Navigation vers practicesoftwaretesting.com")

        # Attendre le chargement des produits
        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a.card")))
        print("Produits chargés")

        # Localiser les cartes produit avec CSS class selector
        product_cards = driver.find_elements(By.XPATH, "//div[contains(@class,'card-body')]")
        for e in product_cards:
            print(e.text)
        print(f"Cartes produit trouvées: {len(product_cards)}")
        assert len(product_cards) > 0, "Aucune carte produit trouvée"

        # Localiser les titres de produits avec CSS
        product_titles = driver.find_elements(By.XPATH, "//*[contains(@class,'card-title')]")
        for i, title in enumerate(product_titles[:3]):
            print(f"Produit {i+1}: {title.get_attribute('textContent').strip()}")

        # Variantes de XPath
        print("\nVariantes de XPath testées:")

        # XPath avec position
        first_card = driver.find_element(By.XPATH, "//div[contains(@class, 'card')][1]")
        print(f" Position [1]: Première carte trouvée")

        # XPath avec position et attribut
        cards_limited = driver.find_elements(By.XPATH, "(//div[contains(@class, 'card')])[position() <= 5]")
        print(f" Position [1-5]: {len(cards_limited)} cartes trouvées")

        # XPath avec not contains - find elements without "row"
        elements_no_row = driver.find_elements(By.XPATH, "//div[contains(@class, 'card') and not(contains(@class, 'row'))]")
        print(f"  XPath avec not(): {len(elements_no_row)} éléments trouvés")

        # XPath avec descendant - find cards that have titles
        cards_with_descendants = driver.find_elements(By.XPATH, "//div[contains(@class, 'card') and descendant::*[contains(@class, 'card-title')]]")
        print(f"  Descendant: {len(cards_with_descendants)} cartes avec titre")
        

        print("\nTest réussi!")
        return True

    except Exception as e:
        print(f"Erreur: {e}")
        return False

    finally:
        driver.quit()
        print("Navigateur fermé")

if __name__ == "__main__":
    test_css_selectors()
