# ## Exercice 8 : Gérer les Alertes JavaScript
# **Site**: the-internet.herokuapp.com/javascript_alerts
# **Compétences**: Accepter/refuser les alertes
# **Instructions**:
# 1. Ouvrez le navigateur
# 2. Accédez à https://the-internet.herokuapp.com/javascript_alerts
# 3. Cliquez sur "Click for JS Alert"
# 4. Acceptez l'alerte (OK)
# 5. Vérifiez le message affiché après l'acceptation
# 6. Cliquez sur "Click for JS Confirm"
# 7. Refusez l'alerte (Cancel)
# 8. Vérifiez le message de refus
# 9. Fermez le navigateur
# **Validation**:
# - Les alertes sont gérées correctement
# - Les messages de confirmation/refus sont corrects

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert

def test_javascript_alerts():
    """
    Gère les alertes JavaScript (accept/cancel)
    """
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        # Accéder au site
        driver.get("https://the-internet.herokuapp.com/javascript_alerts")
        print("Navigation vers javascript_alerts")

        # Test Alerte Simple (Alert)
        print("\n--- Test 1: Simple Alert ---")
        alert_button = driver.find_element(By.XPATH, "//button[contains(text(), 'JS Alert')]")
        alert_button.click()
        print("Bouton cliqué")

        # Attendre et accepter l'alerte
        alert = wait.until(EC.alert_is_present())
        alert_text = alert.text
        print(f"Alerte trouvée: '{alert_text}'")

        alert.accept()  # Cliquer OK
        print("Alerte acceptée")

        # Vérifier le message de confirmation
        result_element = driver.find_element(By.ID, "result")
        result_text = result_element.text
        print(f"Résultat: {result_text}")

        # Test Alerte Confirm - Refus
        print("\n--- Test 2: Confirm Alert (Cancel) ---")
        confirm_button = driver.find_element(By.XPATH, "//button[contains(text(), 'JS Confirm')]")
        confirm_button.click()
        print("Bouton 'Confirm' cliqué")

        # Attendre et refuser l'alerte
        alert = wait.until(EC.alert_is_present())
        alert_text = alert.text
        print(f"Alerte trouvée: '{alert_text}'")

        alert.dismiss()  # Cliquer Cancel
        print("Alerte refusée (Cancel)")

        # Vérifier le message de refus
        result_element = driver.find_element(By.ID, "result")
        result_text = result_element.text
        print(f"Résultat: {result_text}")
        assert "cancel" in result_text.lower(), "Le refus n'a pas été enregistré"

        print("\nTest réussi!")
        return True

    except Exception as e:
        print(f"Erreur: {e}")
        return False

    finally:
        driver.quit()
        print("Navigateur fermé")

if __name__ == "__main__":
    test_javascript_alerts()
