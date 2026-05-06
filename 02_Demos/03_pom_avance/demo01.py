from selenium import webdriver
from dropdown_page import DropdowPage

driver = webdriver.Chrome()

try:
    print("Demo POM dropdown")
    page = DropdowPage(driver)

    print("Ouverture de la page")
    page.open()

    print("Selectionner Option")
    page.select_option_by_text("Option 1")

    print("Lecture de l'Option")
    selected = page.get_selected_option_text()
    print("Option selectionner : ",selected)

    assert selected == "Option 1"
    print("verification OK")

    print("Selectionner Option")
    page.select_option_by_text("Option 2")

    print("Lecture de l'Option")
    selected = page.get_selected_option_text()
    print("Option selectionner : ",selected)

    assert selected == "Option 2"
    print("verification OK")

except Exception as e:
    print(f"Erreur : {e}")

finally:
    driver.quit()