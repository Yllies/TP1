from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Cette partie sert uniquement si on travaille avec un fichier HTML local.
# Elle n'est pas nécessaire quand on utilise directement une URL web.
html_file = Path(__file__).parent / "demo_formulaire.html"
local_url = html_file.resolve().as_uri()

driver = webdriver.Chrome()

# WebDriverWait permet d'attendre qu'une condition soit remplie
# pendant un certain temps avant de déclencher une erreur.
wait = WebDriverWait(driver, 10)


try:
    driver.get(local_url)
    #time.sleep(3)

    # By.ID permet de rechercher un élément grâce à la valeur de son attribut id.
    full_name_field = driver.find_element(By.ID, "fullName")
    email_field = driver.find_element(By.ID, "email")
    address_field = driver.find_element(By.ID, "address")

    # send_keys(...) simule la saisie clavier dans un champ.
    full_name_field.send_keys("John Doe")
    email_field.send_keys("john@example.com")
    address_field.send_keys("123 Main Street")

    #time.sleep(3)

    # On récupère le bouton grâce à son id.
    submit_button = driver.find_element(By.ID, "submit")

    # execute_script(...) exécute du JavaScript dans la page.
    # Le premier paramètre est le code JavaScript à lancer.
    # Les paramètres suivants sont accessibles dans ce code via arguments[0], arguments[1], etc.
    # Ici, arguments[0] représente l'élément submit_button transmis après la chaîne.
    # scrollIntoView() est une méthode JavaScript qui fait défiler la page jusqu'à cet élément.
    driver.execute_script("arguments[0].scrollIntoView();", submit_button)

    #time.sleep(3)

    # click() simule un clic sur l'élément.
    submit_button.click()

    # EC signifie expected_conditions.
    # presence_of_element_located(...) attend qu'un élément soit présent dans la page.
    # Ici, on attend que la zone de résultat soit présente avant de la lire.
    wait.until(EC.presence_of_element_located((By.ID, "output")))

    output = driver.find_element(By.ID, "output")
    output_text = output.text

    assert "John Doe" in output_text, "Nom non trouvé dans le résultat"
    assert "john@example.com" in output_text, "Email non trouvé dans le résultat"
    
    print(f"Résultat vérifié :\n{output_text}")



except AssertionError as e:
    print(f"Erreur d'assertion : {e}")

except Exception as e:
    print(f"Erreur : {e}")

finally:
    driver.quit()   