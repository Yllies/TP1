## Exercice 8 : Gérer les Alertes JavaScript


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
# 1. Ouvrez le navigateur
driver = webdriver.Chrome()
try:
    # 2. Accédez à https://the-internet.herokuapp.com/javascript_alerts
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    
    # 3. Cliquez sur "Click for JS Alert"
    js_alert_button = driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']")
    js_alert_button.click()
    
    # 4. Acceptez l'alerte (OK)
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.accept()
    
    # 5. Vérifiez le message affiché après l'acceptation
    result_text = driver.find_element(By.ID, "result").text
    assert result_text == "You successfully clicked an alert", "Message d'alerte incorrect après acceptation"
    
    # 6. Cliquez sur "Click for JS Confirm"
    js_confirm_button = driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']")
    js_confirm_button.click()
    
    # 7. Refusez l'alerte (Cancel)
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    confirm_alert = driver.switch_to.alert
    confirm_alert.dismiss()
    
    # 8. Vérifiez le message de refus
    confirm_result_text = driver.find_element(By.ID, "result").text
    assert confirm_result_text == "You clicked: Cancel", "Message d'alerte incorrect après refus"
finally:
    # 9. Fermez le navigateur
    driver.quit()
    print("Navigateur fermé.")