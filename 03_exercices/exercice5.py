# **Site**: the-internet.herokuapp.com/checkboxes
# **Compétences**: Gérer les checkboxes

# **Instructions**:
# 1. Ouvrez le navigateur
# 2. Accédez à https://the-internet.herokuapp.com/checkboxes
# 3. Localisez les checkboxes
# 4. Vérifiez l'état initial des cases
# 5. Cochez la première case si elle n'est pas cochée
# 6. Vérifiez que la première case est maintenant cochée
# 7. Décochez la deuxième case si elle est cochée
# 8. Vérifiez que la deuxième case est décochée
# 9. Fermez le navigateur

# **Validation**:
# - L'état initial est vérifié
# - La case se coche/décoche correctement
# - La vérification de l'état fonctionne

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

try:
    driver.get("https://the-internet.herokuapp.com/checkboxes")

    checkboxes = driver.find_elements(By.CSS_SELECTOR,"#checkboxes input[type='checkbox']")
    
    checkbox1 = checkboxes[0]
    checkbox2 = checkboxes[1]

    # verif l'etat initial
    assert not checkbox1.is_selected(), "La première case doit être décochée initialement"
    assert checkbox2.is_selected(), "La deuxième case doit être cochée initialement"
    print("Etat initial vérifié")

    # cocher la premiere case si elle n'est pas cochée
    if not checkbox1.is_selected():
        checkbox1.click()
    
    # verif que la premiere case est cochée
    assert checkbox1.is_selected(), "La première case n'est pas cochée après le clic"
    print("La première case est cochée")

    # decochez la deuxieme case si elle est cochée
    if checkbox2.is_selected():
        checkbox2.click()

    # verif que la deuxieme case est decochee
    assert not checkbox2.is_selected(), "La deuxième case n'est pas décochée après le clic"
    print("La deuxième case est décochée")
    print("Test OK")
    
except AssertionError as e:
    print(f"Erreur d'assertion: {e}")
except Exception as e:
    print(f"Erreur: {e}")