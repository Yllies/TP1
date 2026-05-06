# ## Exercice 6 : Localiser des Éléments avec CSS
# **Site**: practicesoftwaretesting.com
# **Compétences**: Utiliser les sélecteurs CSS
# **Instructions**:
# 1. Ouvrez le navigateur
# 2. Accédez à https://practicesoftwaretesting.com/
# 3. Attendez que les produits se chargent
# 4. Localisez les cartes produit en utilisant le sélecteur CSS `a.card`
# 5. Localisez les titres de produits en utilisant le sélecteur CSS `.card-title`
# 6. Vérifiez que tous les éléments sont visibles
# 7. Comptez le nombre total de cartes produit
# 8. Fermez le navigateur
# **Validation**:
# - Tous les sélecteurs CSS fonctionnent
# - Les éléments sont trouvés
# - Le comptage est correct

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
        product_cards = driver.find_elements(By.CSS_SELECTOR, "a.card")
        print(f"Cartes produit trouvées: {len(product_cards)}")
        assert len(product_cards) > 0, "Aucune carte produit trouvée"

        # Localiser les titres de produits avec CSS
        product_titles = driver.find_elements(By.CSS_SELECTOR, ".card-title")
        print(f"Titres de produits trouvés: {len(product_titles)}")
        for i in range(min(3, len(product_titles))):
            title = driver.find_elements(By.CSS_SELECTOR, ".card-title")[i]
            print(f"  Produit {i+1}: {title.text}")

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

        