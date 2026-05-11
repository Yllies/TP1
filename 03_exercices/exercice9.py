## Exercice 9 : Attendre un Élément qui Charge Dynamiquement

# **Site**: the-internet.herokuapp.com/dynamic_loading/1
# **Compétences**: Explicit waits avec WebDriverWait

# **Instructions**:
# 1. Ouvrez le navigateur
# 2. Accédez à https://the-internet.herokuapp.com/dynamic_loading/1
# 3. Cliquez sur le bouton "Start"
# 4. Attendez explicitement (max 10 secondes) que le texte "Hello World!" apparaisse
# 5. Vérifiez que le texte contient "Hello World!"
# 6. Vérifiez que le texte ne contient pas "It's gone!"
# 7. Fermez le navigateur

# **Validation**:
# - L'attente fonctionne correctement
# - L'élément dynamique est trouvé
# - Le texte est correct
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# 1. Ouvrez le navigateur
driver = webdriver.Chrome()
try:
    # 2. Accédez à https://the-internet.herokuapp.com/dynamic_loading/1
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
    
    # 3. Cliquez sur le bouton "Start"
    start_button = driver.find_element(By.XPATH, "//div[@id='start']/button")
    start_button.click()
    
    # 4. Attendez explicitement (max 10 secondes) que le texte "Hello World!" apparaisse
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.ID, "finish"), "Hello World!")
    )
    
    # 5. Vérifiez que le texte contient "Hello World!"
    finish_text = driver.find_element(By.ID, "finish").text
    assert "Hello World!" in finish_text, "Le texte ne contient pas 'Hello World!'"
    
    # 6. Vérifiez que le texte ne contient pas "It's gone!"
    assert "It's gone!" not in finish_text, "Le texte contient 'It's gone!'"
finally:
    # 7. Fermez le navigateur
    driver.quit()
    print("Navigateur fermé.")