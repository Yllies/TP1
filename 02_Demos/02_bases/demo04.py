from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Cette partie sert uniquement si on travaille avec un fichier HTML local.
# Elle n'est pas nécessaire quand on utilise directement une URL web.
html_file = Path(__file__).parent / "demo2_page.html"
local_url = html_file.resolve().as_uri()


driver = webdriver.Chrome()


try:
    driver.get(local_url)

    # By.TAG_NAME permet de rechercher un élément par nom de balise HTML.
    # Ici, on cherche la première balise <button> de la page.
    element = driver.find_element(By.TAG_NAME, "button")
    print(f"Élément trouvé : {element.text}")

    # tag_name permet de connaître le nom réel de la balise trouvée.
    # Cela permet de vérifier qu'on a bien récupéré un bouton.
    tag_name = element.tag_name
    assert tag_name == "button", f"L'élément n'est pas un bouton, tag trouvé : {tag_name}"
    print(f"Type d'élément vérifié : <{tag_name}>")

    # get_attribute(...) permet de lire la valeur d'un attribut HTML.
    # Ici, on récupère la valeur de l'attribut type du bouton.
    button_type = element.get_attribute("type")
    assert button_type == "button", f"Type de bouton incorrect : {button_type}"
    print(f"Attribut type vérifié : {button_type}")

    # By.CSS_SELECTOR recherche un élément avec un sélecteur CSS.
    # Ici, "#start-btn" signifie : l'élément qui possède l'id start-btn.
    element_by_css = driver.find_element(By.CSS_SELECTOR, "#start-btn")
    print(f"Élément trouvé avec CSS_SELECTOR : {element_by_css.text}")

    # By.XPATH recherche un élément avec une expression XPath.
    # Ici, //button signifie : chercher une balise <button> n'importe où dans la page.
    element_by_xpath = driver.find_element(By.XPATH, "//button")
    print(f"Élément trouvé avec XPATH : {element_by_xpath.text}")

except AssertionError as e:
    print(f"Erreur d'assertion : {e}")

except Exception as e:
    print(f"Erreur : {e}")

finally:
    driver.quit()