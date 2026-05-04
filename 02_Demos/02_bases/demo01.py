import time

from selenium import webdriver

print("\n" + "=" * 60)
print("DEMO 3: GESTION DE LA FENETRE")
print("=" * 60)

driver = webdriver.Chrome()

try:
    print("\n1. Navigation vers example.com...")
    driver.get("https://example.com")
    time.sleep(2)
    print(f"    Titre: {driver.title}")

    current_size = driver.get_window_size()
    print(f"\n2. Taille actuelle: {current_size['width']}x{current_size['height']}")

    print("\n3. Redimensionner à 800x600...")
    driver.set_window_size(800, 600)
    time.sleep(2)
    new_size = driver.get_window_size()
    print(f"    Nouvelle taille: {new_size['width']}x{new_size['height']}")

    print("\n4. Maximiser la fenêtre...")
    driver.maximize_window()
    time.sleep(2)
    max_size = driver.get_window_size()
    print(f"    Taille maximisée: {max_size['width']}x{max_size['height']}")

    position = driver.get_window_position()
    print(f"\n5. Position de la fenêtre: X={position['x']}, Y={position['y']}")

    print("\n6. Appuyez sur Entrée pour fermer...")
except Exception as e:
    print(f"    Erreur: {e}")
finally:
    print("\n7. Fermeture...")
    driver.quit()
    print("    Fermé")