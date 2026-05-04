from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By

# Cette partie sert uniquement si on travaille avec un fichier HTML local.
# Elle n'est pas nécessaire quand on utilise directement une URL web.
# Path permet de construire proprement un chemin vers le fichier.
html_file = Path(__file__).parent / "demo_page.html"
# as_uri() transforme le chemin local en URL de type file://
# afin que le navigateur puisse ouvrir le fichier.
local_url = html_file.resolve().as_uri()


driver = webdriver.Chrome()

try:
    # get(...) ouvre la page demandée.
    driver.get(local_url)

    # driver.title contient le titre actuel de la page.
    # assert sert à vérifier qu'une condition est vraie.
    # Si la condition est fausse, Python déclenche une AssertionError.
    assert driver.title == "Demo Selenium ", f"Titre incorrect : {driver.title}"
    print(f"Titre vérifié : {driver.title}")

    # By permet d'indiquer la façon de rechercher un élément.
    # By.TAG_NAME signifie qu'on cherche par nom de balise HTML.
    # find_element(...) récupère le premier élément correspondant.
    heading = driver.find_element(By.TAG_NAME, "h1")

    # .text récupère le texte visible de l'élément trouvé.
    assert "Bienvenue" in heading.text, "Texte attendu non trouvé dans le h1"
    print(f"Contenu vérifié : {heading.text}")

    # driver.current_url contient l'adresse actuellement ouverte.
    # Ici, on vérifie qu'on est bien sur un fichier local.
    assert driver.current_url.startswith("file:///"), "URL locale incorrecte"
    print(f"URL vérifiée : {driver.current_url}")


except AssertionError as e:
    # AssertionError correspond aux erreurs provoquées par assert.
    # Cela permet de distinguer un échec de vérification d'une autre erreur technique.
    print(f"Erreur d'assertion : {e}")

except Exception as e:
    # Exception permet d'attraper les autres erreurs possibles :
    # problème de navigateur, élément introuvable, souci de driver, etc.
    print(f"Erreur : {e}")

finally:
    # finally s'exécute dans tous les cas, qu'il y ait une erreur ou non.
    # quit() ferme complètement le navigateur et termine la session Selenium.
    driver.quit()