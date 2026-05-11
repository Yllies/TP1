## Exercice 6 : Localiser des Éléments avec CSS
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
# 1. Ouvrez le navigateur
driver = webdriver.Chrome()
try:
    # 2. Accédez à https://practicesoftwaretesting.com/
    driver.get("https://practicesoftwaretesting.com/")
    
    # 3. Attendez que les produits se chargent
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a.card"))
    )
    
    # 4. Localisez les cartes produit en utilisant le sélecteur CSS `a.card`
    product_cards = driver.find_elements(By.CSS_SELECTOR, "a.card")
    
    # 5. Localisez les titres de produits en utilisant le sélecteur CSS `.card-title`
    product_titles = driver.find_elements(By.CSS_SELECTOR, ".card-title")
    
    # 6. Vérifiez que tous les éléments sont visibles
    for card in product_cards:
        assert card.is_displayed(), "Une carte produit n'est pas visible"
    
    for title in product_titles:
        assert title.is_displayed(), "Un titre de produit n'est pas visible"
    
    # 7. Comptez le nombre total de cartes produit
    total_cards = len(product_cards)
    print(f"Nombre total de cartes produit: {total_cards}")
finally:
    # 8. Fermez le navigateur
    driver.quit()
    print("Navigateur fermé.")