from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By


def demo_css_selectors():
    driver = webdriver.Chrome()

    try:
        # Utile uniquement en local :
        # avec un vrai site web, on utiliserait directement son URL.
        html_file = Path(__file__).with_name("demo_css_selectors.html")
        driver.get(html_file.as_uri())

        # ".card" sélectionne tous les éléments ayant la classe "card".
        # find_elements => liste d’objets Selenium de type WebElement
        product_cards = driver.find_elements(By.CSS_SELECTOR, ".card")
        assert len(product_cards) == 3, f"Nombre de cartes incorrect : {len(product_cards)}"

        # ".card-title" sélectionne tous les éléments ayant cette classe.
        product_titles = driver.find_elements(By.CSS_SELECTOR, ".card-title")
        assert len(product_titles) == 3, f"Nombre de titres incorrect : {len(product_titles)}"

        first_title = product_titles[0].text
        assert first_title == "Marteau", f"Premier titre incorrect : {first_title}"

        # "p.card-text" cible une balise <p> qui possède la classe "card-text".
        texts = driver.find_elements(By.CSS_SELECTOR, "p.card-text")
        assert len(texts) == 6, f"Nombre de paragraphes incorrect : {len(texts)}"

        # "[class*='text']" signifie :
        # sélectionner les éléments dont l'attribut class contient "text".
        text_elements = driver.find_elements(By.CSS_SELECTOR, "[class*='text']")
        assert len(text_elements) == 6, f"Nombre d'éléments avec class*='text' incorrect : {len(text_elements)}"

        # ".card-text[class*='price']" combine une classe
        # et un attribut dont la valeur contient "price".
        prices = driver.find_elements(By.CSS_SELECTOR, ".card-text[class*='price']")
        assert len(prices) == 3, f"Nombre de prix incorrect : {len(prices)}"

        first_price = prices[0].text
        assert first_price == "$12.50", f"Premier prix incorrect : {first_price}"

        # "button.btn" cible les balises <button> qui ont la classe "btn".
        buttons = driver.find_elements(By.CSS_SELECTOR, "button.btn")
        assert len(buttons) == 3, f"Nombre de boutons incorrect : {len(buttons)}"

        # is_displayed() indique si l'élément est visible à l'écran.
        visible_buttons = [button for button in buttons if button.is_displayed()]
        assert len(visible_buttons) == 2, f"Nombre de boutons visibles incorrect : {len(visible_buttons)}"

        print("Démo CSS selectors OK")

    except Exception as e:
        print(f"Erreur : {e}")

    finally:
        driver.quit()


if __name__ == "__main__":
    demo_css_selectors()