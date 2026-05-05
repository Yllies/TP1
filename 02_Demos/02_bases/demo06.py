from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

# Utile uniquement en local :
# avec un vrai site web, on utiliserait directement son URL.
html_file = Path(__file__).with_name("demo_checkboxes.html")
driver.get(html_file.as_uri())

try:
    # find_elements renvoie une liste de tous les éléments qui correspondent au sélecteur.
    checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
    assert len(checkboxes) == 2, f"Nombre de checkboxes inattendu : {len(checkboxes)}" 

    # On récupère ici la première et la deuxième checkbox par position.
    checkbox_1 = checkboxes[0]
    checkbox_2 = checkboxes[1]

    # is_selected() indique si la case est cochée ou non.
    assert not checkbox_1.is_selected(), "La checkbox 1 devrait être décochée au départ"
    assert checkbox_2.is_selected(), "La checkbox 2 devrait être cochée au départ"

    # On clique seulement si nécessaire pour obtenir l'état voulu.
    if not checkbox_1.is_selected():
        checkbox_1.click()

    if checkbox_2.is_selected():
        checkbox_2.click()

    # On vérifie l'état final après interaction.
    assert checkbox_1.is_selected(), "La checkbox 1 devrait être cochée"
    assert not checkbox_2.is_selected(), "La checkbox 2 devrait être décochée"

    # Vérification simple du texte mis à jour dans la page.
    status_a = driver.find_element(By.ID, "status-a")
    status_b = driver.find_element(By.ID, "status-b")

    assert status_a.text == "Newsletter : oui", f"Texte incorrect : {status_a.text}"
    assert status_b.text == "Notifications : non", f"Texte incorrect : {status_b.text}"

    print("Démo checkboxes OK")

except Exception as e:
    print(f"Erreur : {e}")

finally:
    driver.quit()