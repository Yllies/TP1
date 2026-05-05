from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

# Utile uniquement en local :
# avec un vrai site web, on utiliserait directement son URL HTTP/HTTPS.
html_file = Path(__file__).with_name("demo_dropdown.html")
driver.get(html_file.as_uri())

try:
    driver.get(html_file.as_uri())

    # On localise la balise <select>.
    dropdown_element = driver.find_element(By.ID, "category")

    # Select est l'outil Selenium prévu pour manipuler un menu déroulant <select>.
    dropdown = Select(dropdown_element)

    # On sélectionne ici par texte visible pour montrer une autre manière claire de choisir une option.
    dropdown.select_by_visible_text("Jeux")
    #dropdown.select_by_value("games")

    # first_selected_option renvoie l'option actuellement sélectionnée.
    selected_option = dropdown.first_selected_option

    # .text lit le texte visible de l'option.
    selected_text = selected_option.text
    assert selected_text == "Jeux", f"Texte sélectionné incorrect : {selected_text}"

    # get_attribute("value") lit la valeur HTML de l'option sélectionnée.
    selected_value = selected_option.get_attribute("value")
    assert selected_value == "games", f"Valeur sélectionnée incorrecte : {selected_value}"

    # On change ensuite de choix pour montrer qu'on peut modifier la sélection.
    dropdown.select_by_visible_text("Musique")

    selected_option = dropdown.first_selected_option
    assert selected_option.text == "Musique", f"Texte sélectionné incorrect : {selected_option.text}"
    assert selected_option.get_attribute("value") == "music", (
        f"Valeur sélectionnée incorrecte : {selected_option.get_attribute('value')}"
    )

    # Vérification simple du texte mis à jour dans la page.
    info = driver.find_element(By.ID, "info")
    assert "Musique (music)" in info.text, f"Texte affiché incorrect : {info.text}"

    print("Démo dropdown OK")


except Exception as e:
    print(f"Erreur : {e}")

finally:
        driver.quit()