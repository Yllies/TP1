import time
from selenium import webdriver

print("\n" + "=" * 60)
print("DEMO : SEQUENCE DE NAVIGATION")
print("=" * 60)

driver = webdriver.Chrome()

try:
    print("\n1. Navigation vers Wikipedia...")
    driver.get("https://wikipedia.org")
    time.sleep(1)
    print(f"    Titre: {driver.title}")
    time.sleep(1)

    print("\n2. Navigation vers GitHub...")
    driver.get("https://github.com")
    time.sleep(1)
    print(f"    Titre: {driver.title}")
    time.sleep(1)

    print("\n3. Retour en arrière (history back)...")
    driver.back()
    time.sleep(1)
    print(f"    Titre actuel: {driver.title}")
    time.sleep(1)

    print("\n4. Avancer (history forward)...")
    driver.forward()
    time.sleep(1)
    print(f"    Titre actuel: {driver.title}")

    print("\n5. Rafraîchir la page (F5)...")
    driver.refresh()
    time.sleep(1)
    print("    Page rafraîchie")

    print("\n6. Appuyez sur Entrée pour fermer...")
    
except Exception as e:
    print(f"    Erreur: {e}")
finally:
    print("\n7. Fermeture...")
    driver.quit()
    print("    Fermé")   