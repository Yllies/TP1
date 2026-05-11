from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
try:
    
    driver.get("https://demoqa.com/text-box")
    driver.maximize_window()

    # Remplir le form
    driver.find_element(By.ID,"userName").send_keys("John Doe")
    driver.find_element(By.ID,"userEmail").send_keys("johndoe@gmail.com")
    driver.find_element(By.ID,"currentAddress").send_keys("100 Chemin du Cimetière")
    element = driver.find_element(By.ID, "submit")
    driver.execute_script("arguments[0].scrollIntoView();", element)
    time.sleep(1) # Attendre 2 secondes pour voir les champs remplis


    # Soumettre le form
    driver.find_element(By.ID,"submit").click()
    output = driver.find_element(By.ID,"output").text
    assert "John Doe" in output, "Le nom n'est pas affiché dans le résultat"
    assert "johndoe@gmail.com" in output, "L'email n'est pas affiché dans le résultat"
    assert "100 Chemin du Cimetière" in output, "L'adresse n'est pas affichée dans le résultat"

    print("Formulaire soumis avec succès")

except Exception as e:
    print(f"Erreur: {e}")

finally:
    driver.quit()
    print("Navigateur fermé")