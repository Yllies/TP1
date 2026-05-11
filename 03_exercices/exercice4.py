## Exercice 4 : Sélectionner une Option dans un Dropdown


# **Site**: the-internet.herokuapp.com/dropdown
# **Compétences**: Gérer les dropdowns HTML

# **Instructions**:
# 1. Ouvrez le navigateur
# 2. Accédez à https://the-internet.herokuapp.com/dropdown
# 3. Localisez le dropdown principal
# 4. Sélectionnez l'option "Option 1"
# 5. Vérifiez que "Option 1" est sélectionné
# 6. Changez pour "Option 2"
# 7. Vérifiez que "Option 2" est maintenant sélectionné
# 8. Fermez le navigateur

# **Validation**:
# - Le dropdown est accessible
# - La sélection change correctement
# - La vérification fonctionne

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select    
import time

driver = webdriver.Chrome()

try:
    driver.get("https://the-internet.herokuapp.com/dropdown")

    dropdown_element = driver.find_element(By.ID,"dropdown")
    dropdown = Select(dropdown_element)

    # selectionner option 1
    dropdown.select_by_visible_text("Option 1")
    time.sleep(1) # attendre pour voir la selection

    # verifier que option 1 est selectionnee
    selected_option = dropdown.first_selected_option
    assert selected_option.text == "Option 1",f"Option 1 n'est pas selectionnee : {selected_option.text}"
    print("Option 1 est selectionnée")

    # changer pour option 2
    dropdown.select_by_visible_text("Option 2")
    #time.sleep(1) # attendre pour voir la selection

    # verifier que option 2 est selectionnee
    selected_option = dropdown.first_selected_option
    assert selected_option.text == "Option 2",f"Option 2 n'est pas selectionnee : {selected_option.text}"
    print("Option 2 est selectionnée")
    
    print("Test reussie")
except AssertionError as e:
    print(f"Erreur d'assertion: {e}")
except Exception as e:
    print(f"Erreur: {e}")