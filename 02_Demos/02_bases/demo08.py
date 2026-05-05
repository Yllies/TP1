from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def demo_xpath_wait_alert_extract():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        # Utile uniquement en local :
        # avec un vrai site web, on utiliserait directement son URL HTTP/HTTPS.
        html_file = Path(__file__).with_name("demo_xpath_wait_alert_extract.html")
        driver.get(html_file.as_uri())

        # contains(@class, 'card') est pratique quand un élément peut avoir plusieurs classes.
        cards = driver.find_elements(By.XPATH, "//article[contains(@class, 'card')]")
        assert len(cards) == 3, f"Nombre de cartes incorrect : {len(cards)}"

        # contains(...) peut aussi servir à trouver des titres par classe partielle.
        titles = driver.find_elements(By.XPATH, "//*[contains(@class, 'card-title')]")
        assert len(titles) == 3, f"Nombre de titres incorrect : {len(titles)}"
        assert titles[0].text == "Marteau", f"Premier titre incorrect : {titles[0].text}"

        # Attribut exact.
        buttons = driver.find_elements(By.XPATH, "//button[@class='btn btn-primary']")
        assert len(buttons) == 3, f"Nombre de boutons incorrect : {len(buttons)}"

        # ./parent::* part de l'élément courant et remonte vers son parent direct.
        first_button_parent = buttons[0].find_element(By.XPATH, "./parent::*")
        assert first_button_parent.tag_name == "div", f"Parent inattendu : {first_button_parent.tag_name}"

        # Position : [1] récupère le premier élément correspondant.
        first_card = driver.find_element(By.XPATH, "//article[contains(@class, 'card')][1]")
        assert "Marteau" in first_card.text, f"Première carte incorrecte : {first_card.text}"

        # position() <= 2 limite le nombre d'éléments renvoyés.
        first_two_cards = driver.find_elements(
            By.XPATH,
            "//article[contains(@class, 'card')][position() <= 2]"
        )
        assert len(first_two_cards) == 2, f"Nombre de cartes limité incorrect : {len(first_two_cards)}"

        # not(...) permet d'exclure certains éléments.
        cards_without_row = driver.find_elements(
            By.XPATH,
            "//article[contains(@class, 'card') and not(contains(@class, 'row'))]"
        )
        assert len(cards_without_row) == 2, f"Filtrage avec not() incorrect : {len(cards_without_row)}"

        # descendant::* vérifie qu'un élément contient un descendant correspondant.
        cards_with_title = driver.find_elements(
            By.XPATH,
            "//article[contains(@class, 'card') and descendant::*[contains(@class, 'card-title')]]"
        )
        assert len(cards_with_title) == 3, f"Recherche avec descendant incorrecte : {len(cards_with_title)}"

        # contains(@alt, 'product') or contains(@alt, 'image') combine deux conditions.
        images = driver.find_elements(
            By.XPATH,
            "//img[contains(@alt, 'product') or contains(@alt, 'image')]"
        )
        assert len(images) == 3, f"Nombre d'images incorrect : {len(images)}"

        # Ici on cherche à l'intérieur de chaque carte, pas dans toute la page.
        # Cela évite de mélanger les données de plusieurs produits.
        products = []
        for index, card in enumerate(cards, start=1):
            name = card.find_element(By.XPATH, ".//*[contains(@class, 'card-title')]").text.strip()

            text_elements = card.find_elements(By.XPATH, ".//*[contains(@class, 'card-text')]")
            text_values = [element.text.strip() for element in text_elements if element.text.strip()]

            products.append({
                "index": index,
                "name": name,
                "details": text_values,
            })

        print("Liste des produit recup : ",products)
        assert len(products) == 3, f"Liste de produits incorrecte : {len(products)}"
        assert products[0]["name"] == "Marteau", f"Nom extrait incorrect : {products[0]['name']}"
        assert "$12.50" in products[0]["details"], f"Détails extraits incorrects : {products[0]['details']}"


        # On déclenche un contenu qui apparaît après un délai.
        driver.find_element(By.ID, "load-button").click()

        # visibility_of_element_located attend qu'un élément existe et soit visible.
        delayed_result = wait.until(
            EC.visibility_of_element_located((By.ID, "delayed-result"))
        )

        assert delayed_result.text == "Contenu chargé", f"Texte chargé incorrect : {delayed_result.text}"

        # test des alert

        driver.find_element(By.ID, "alert-button").click()

        # alert_is_present() attend qu'une alerte JavaScript soit réellement ouverte.
        alert = wait.until(EC.alert_is_present())

        # .text lit le message affiché dans l'alerte.
        assert alert.text == "Bonjour depuis l'alerte simple", f"Alerte inattendue : {alert.text}"

        # accept() correspond au bouton OK.
        alert.accept()

        alert_result = driver.find_element(By.ID, "alert-result")
        assert alert_result.text == "Alerte acceptée", f"Résultat alerte incorrect : {alert_result.text}"

        driver.find_element(By.ID, "confirm-button").click()
        alert = wait.until(EC.alert_is_present())
        assert alert.text == "Voulez-vous continuer ?", f"Confirmation inattendue : {alert.text}"

        # dismiss() correspond au bouton Annuler / Cancel.
        alert.dismiss()

        alert_result = driver.find_element(By.ID, "alert-result")
        assert alert_result.text == "Confirmation refusée", f"Résultat confirmation incorrect : {alert_result.text}"

        driver.find_element(By.ID, "prompt-button").click()
        alert = wait.until(EC.alert_is_present())
        assert alert.text == "Entrez un texte :", f"Prompt inattendue : {alert.text}"

        # send_keys() envoie du texte dans une prompt JavaScript.
        alert.send_keys("Texte Selenium")
        alert.accept()

        alert_result = driver.find_element(By.ID, "alert-result")
        assert alert_result.text == "Texte saisi : Texte Selenium", (
            f"Résultat prompt incorrect : {alert_result.text}"
        )
        
        print("Démo XPath / waits / alertes / extraction OK")

    except Exception as e:
        print(f"Erreur : {e}")

    finally:
        driver.quit()


if __name__ == "__main__":
    demo_xpath_wait_alert_extract()