# ## Exercice 2 : Localiser un Élément par TAG_NAME

# **Site**: example.com
# **Compétences**: Localiser par TAG_NAME, extraire attributs

# **Instructions**:
# 1. Ouvrez le navigateur
# 2. Accédez à https://example.com
# 3. Trouvez le premier lien (tag "a") de la page
# 4. Vérifiez que c'est un lien (tag "a")
# 5. Vérifiez que le href est valide (non vide)
# 6. Affichez l'URL du lien
# 7. Fermez le navigateur

# **Validation**:
# - L'élément est trouvé
# - Le type d'élément est correct
# - L'URL est valide

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    driver.get("https://example.com")

    # trouver l'element lien de la page
    element = driver.find_element(By.CSS_SELECTOR,"a")
    print(f"Element trouve : {element.text}")

    # verifier que c'est un lien
    tag_name = element.tag_name
    assert tag_name == "a",f"l'element n'est pas un lien : {tag_name}"
    print(f"Type d'element correct : {tag_name}")

    # Verifier que le href est valide
    href = element.get_attribute("href")
    assert href is not None and len(href) > 0,f"URL invalide : {href}"
    print(f"Url valide : {href}")

    print("Test reussie")

except AssertionError as e:
    print(f"Erreur d'assertion: {e}")

except Exception as e:
    print(f"Erreur: {e}")

finally:
    driver.quit()
    print("Navigateur fermé")