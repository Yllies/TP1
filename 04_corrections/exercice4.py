# ## Exercice 4 : Sélectionner une Option dans un Dropdown
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
from selenium.webdriver.support.select import Select

def test_dropdown_selection():
    """
    Sélectionne des options dans un dropdown et vérifie la sélection
    """
    driver = webdriver.Chrome()

    try:
        # Accéder au site
        driver.get("https://the-internet.herokuapp.com/dropdown")
        print("Navigation vers le dropdown")

        # Localiser le dropdown
        dropdown_element = driver.find_element(By.ID, "dropdown")
        dropdown = Select(dropdown_element)
        print("Dropdown trouvé")

        # Sélectionner l'option "Option 1"
        dropdown.select_by_value("1")
        selected_option = dropdown.first_selected_option.text
        assert "Option 1" in selected_option, f"Option incorrecte: {selected_option}"
        print(f"Option 1' sélectionnée: {selected_option}")

        # Vérifier que "Option 1" est sélectionnée
        selected_value = dropdown.first_selected_option.get_attribute("value")
        assert selected_value == "1", f"Valeur incorrecte: {selected_value}"
        print("Vérification réussie: 'Option 1' est sélectionnée")

         # Changer pour "Option 2"
        dropdown.select_by_value("2")
        selected_option = dropdown.first_selected_option.text
        assert "Option 2" in selected_option, f"Option incorrecte: {selected_option}"
        print(f"'Option 2' sélectionnée: {selected_option}")

        # Vérifier que "Option 2" est maintenant sélectionnée
        selected_value = dropdown.first_selected_option.get_attribute("value")
        assert selected_value == "2", f"Valeur incorrecte: {selected_value}"
        print("Vérification réussie: 'Option 2' est sélectionnée")

        print("\nTest réussi!")
        return True
    
    except Exception as e:
        print(f"Erreur: {e}")
        return False

    finally:
        driver.quit()
        print("Navigateur fermé")

if __name__ == "__main__":
    test_dropdown_selection()