# ## Exercice 5 : Cocher des Cases à Cocher
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


def test_checkboxes():
    """
    Coche/décoche des cases à cocher et vérifie l'état
    """
    driver = webdriver.Chrome()

    try:
        #  Accéder au site
        driver.get("https://the-internet.herokuapp.com/checkboxes")
        print("Navigation vers la page des checkboxes")

        #  Localiser les checkboxes
        checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
        print(f"{len(checkboxes)} checkboxes trouvées")

        # Vérifier l'état initial
        checkbox_1 = checkboxes[0]
        checkbox_2 = checkboxes[1]

        is_checked_1 = checkbox_1.is_selected()
        is_checked_2 = checkbox_2.is_selected()
        print(f"État initial - Checkbox 1: {'Cochée' if is_checked_1 else 'Décochée'}")
        print(f"État initial - Checkbox 2: {'Cochée' if is_checked_2 else 'Décochée'}")

        # Cocher la première si elle n'est pas cochée
        if not checkbox_1.is_selected():
            checkbox_1.click()
            print("Checkbox 1 cochée")

        # Vérifier que la première est maintenant cochée
        assert checkbox_1.is_selected(), "La checkbox 1 n'est pas cochée"
        print("Vérification: Checkbox 1 est cochée")

        # Décocher la deuxième si elle est cochée
        if checkbox_2.is_selected():
            checkbox_2.click()
            print("Checkbox 2 décochée")

        # Vérifier que la deuxième est maintenant décochée
        assert not checkbox_2.is_selected(), "La checkbox 2 est toujours cochée"
        print("Vérification: Checkbox 2 est décochée")

        print("\nTest réussi!")
        return True

    except Exception as e:
        print(f"Erreur: {e}")
        return False

    finally:
        driver.quit()
        print("Navigateur fermé")

if __name__ == "__main__":
    test_checkboxes()