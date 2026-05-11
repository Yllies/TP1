## Exercice 7 : Localiser des Éléments avec XPath


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
# 1. Ouvrez le navigateur
driver = webdriver.Chrome()
try:
    # 2. Accédez à https://practicesoftwaretesting.com/
    driver.get("https://practicesoftwaretesting.com/")
    
    # 3. Attendez que les produits se chargent
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "//a[contains(@class, 'card')]"))
    )
    
    # 4. Localisez les cartes produit en utilisant XPath avec `contains()` pour la classe
    product_cards = driver.find_elements(By.XPATH, "//a[contains(@class, 'card')]")
    
    # 5. Localisez les titres de produits en utilisant XPath (Testez différentes variations de XPath: position, not(), descendant)
    product_titles = driver.find_elements(By.XPATH, "//h5[@class='card-title']")
    
    # 6. Vérifiez que tous les éléments sont trouvés
    assert len(product_cards) > 0, "Aucune carte produit trouvée"
    assert len(product_titles) > 0, "Aucun titre de produit trouvé"
finally:
    # 7. Fermez le navigateur
    driver.quit()
    print("Navigateur fermé.")