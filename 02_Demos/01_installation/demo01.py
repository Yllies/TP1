import selenium
from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service

print("Version de selenium : ",selenium.__version__)

# 1. Ouvrir un navigateur
# service = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service)
driver = webdriver.Chrome()

try:
    # 2. Aller sur un site
    driver.get("https://example.com")

    # 3. Vérifier le titre
    print(f"Titre: {driver.title}")

    # 4. Attendre un peu
    input("Appuyez sur Entrée pour fermer...")

finally:
    # 5. Fermer le navigateur
    driver.quit()