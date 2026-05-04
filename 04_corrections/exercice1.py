# **Instructions**:
# 1. Ouvrez un navigateur Chrome
# 2. Accédez à https://example.com
# 3. Vérifiez que le titre de la page est exactement "Example Domain"
# 4. Vérifiez que le contenu contient "Example Domain"
# 5. Fermez le navigateur

from selenium import webdriver
from selenium.webdriver.common.by import By

# initialiser le driver
driver = webdriver.Chrome()

try:
    # Accédez à https://example.com
    driver.get("https://example.com")

    # 3. Vérifiez que le titre de la page est exactement "Example Domain"
    assert driver.title == "Example Domain", f"Titre incorrect {driver.title}"
    print(f"Titre vérifié: {driver.title}")

    # 4. Vérifiez que le contenu contient "Example Domain"
    body = driver.find_element(By.TAG_NAME,"body")
    body_text = body.text
    print("#"*100)
    print(body_text)
    print("#"*100)
    assert "Example Domain" in body_text,"Texte 'Example Domain' non trouvé"
    print("Contenu vérifié: 'Example Domain' trouvé")


except AssertionError as e:
    print(f"Erreur d'assertion: {e}")

except Exception as e:
    print(f"Erreur: {e}")

finally:
    # 5. Fermer le navigateur
    driver.quit()
    print("Navigateur fermé")