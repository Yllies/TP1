from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def demo_google_assertions():
    """Tester Google avec assertions"""
    print("\n" + "="*60)
    print("DEMO: ASSERTIONS SUR GOOGLE")
    print("="*60)

    driver = webdriver.Chrome()

    try:
        # Navigation
        print("\n1. Navigation vers Google...")
        driver.get("https://google.com")
        time.sleep(1)

        # Assertion 1: Titre
        print("2. Assertion 1: Vérifier le titre")
        assert driver.title == "Google", f"Title error: {driver.title}"
        print(f"    Titre correct: '{driver.title}'")

        # Assertion 2: URL
        print("3. Assertion 2: Vérifier l'URL")
        assert "google" in driver.current_url, f"URL error: {driver.current_url}"
        print(f"    URL correcte: {driver.current_url}")

        # Assertion 3: Élément existe
        print("4. Assertion 3: Barre de recherche existe")
        search_box = driver.find_element(By.NAME, "q")
        assert search_box is not None, "Search box not found"
        print("    Barre de recherche trouvée")

        # Assertion 4: Bouton existe
        print("5. Assertion 4: Boutons de recherche existent")
        buttons = driver.find_elements(By.CSS_SELECTOR, "button")
        assert len(buttons) > 0, "No buttons found"
        print(f"    {len(buttons)} boutons trouvés")

        # Assertion 5: Vérifier le contenu de la page
        print("6. Assertion 5: Contenu de la page")
        assert "Search" in driver.page_source or "search" in driver.page_source
        print("    Contenu 'search' trouvé")

        # Assertion 6: Élément est enabled
        print("7. Assertion 6: Barre est enabled")
        assert search_box.is_enabled(), "Search box is not enabled"
        print("    Barre de recherche est enabled")

        # Assertion 7: Élément est visible
        print("8. Assertion 7: Barre est visible")
        assert search_box.is_displayed(), "Search box is not displayed"
        print("    Barre de recherche est visible")

        # Assertion 8: Élément input accepte du texte (via JavaScript)
        print("\n10. Assertion 8: Saisie de texte dans barre")
        driver.execute_script("arguments[0].value = 'Selenium Python';", search_box)
        value = search_box.get_attribute("value")
        assert "Selenium" in value, "Text not entered"
        print(f"    Texte entré: {value}")

        print("\n" + "="*60)
        print(" TOUS LES TESTS SONT PASSÉS!")
        print("="*60)

    except AssertionError as e:
        print(f"\n Assertion échouée: {e}")
    except Exception as e:
        print(f"\n Erreur: {e}")
        import traceback
        traceback.print_exc()
    finally:
        print("\nFermeture du navigateur...")
        driver.quit()
        print(" Fermé")

def demo_demoqa_assertions():
    """Tester DemoQA avec assertions"""
    print("\n" + "="*60)
    print("DEMO: ASSERTIONS SUR DEMOQA")
    print("="*60)


    driver = webdriver.Chrome()

    try:
        # Navigation
        print("\n1. Navigation vers DemoQA...")
        driver.get("https://demoqa.com/text-box")
        time.sleep(2)

        # Assertion 1: Page chargée
        print("2. Assertion 1: Page chargée")
        assert "demosite" in driver.title, f"Title: {driver.title}"
        print(f"    Titre: '{driver.title}'")

        # Assertion 2: Formulaire existe
        print("3. Assertion 2: Formulaire texte existe")
        form = driver.find_element(By.ID, "userForm")
        assert form is not None
        print("    Formulaire trouvé")

        # Assertion 3: Input pour nom existe
        print("4. Assertion 3: Champ nom existe")
        name_input = driver.find_element(By.ID, "userName")
        assert name_input is not None
        assert name_input.is_enabled()
        print("    Champ nom trouvé et enabled")

        # Remplir le formulaire
        print("\n5. Remplissage du formulaire...")
        name_input.send_keys("Jean Dupont")

        email_input = driver.find_element(By.ID, "userEmail")
        email_input.send_keys("jean@example.com")

        print("    Texte saisi")

        # Assertion 4: Valeur saisie
        print("6. Assertion 4: Valeur saisie correctement")
        assert name_input.get_attribute("value") == "Jean Dupont"
        assert email_input.get_attribute("value") == "jean@example.com"
        print("    Valeurs correctes")

        # Assertion 5: Bouton submit existe
        print("7. Assertion 5: Bouton soumettre existe")
        submit_btn = driver.find_element(By.ID, "submit")
        assert submit_btn is not None
        assert submit_btn.is_displayed()
        assert submit_btn.is_enabled()
        print("    Bouton submit trouvé et enabled")

        print("\n" + "="*60)
        print(" TOUS LES TESTS SUR DEMOQA SONT PASSÉS!")
        print("="*60)

    except AssertionError as e:
        print(f"\n Assertion échouée: {e}")
    except Exception as e:
        print(f"\n Erreur: {e}")
    finally:
        print("\nFermeture...")
        driver.quit()
        print(" Fermé")



def test_function_with_return():
    """Fonction de test avec retour de valeur"""
    print("\n" + "="*60)
    print("DEMO: FONCTION DE TEST")
    print("="*60)

    driver = webdriver.Chrome()

    try:
        print("\n1. Exécution du test...")
        driver.get("https://wikipedia.org")
        time.sleep(1)

        # ARRANGE
        title = driver.title

        # ACT & ASSERT
        print("2. Vérifications...")
        assert title != "", "Title is empty"
        assert "Wikipedia" in title, f"Title should contain Wikipedia, got: {title}"

        # Vérifier élément
        search_input = driver.find_element(By.ID, "searchInput")
        assert search_input is not None, "Search not found"

        print("3. Résultats:")
        print(f"    Titre: {title}")
        print(f"    URL: {driver.current_url}")
        print(f"    Élément trouvé")

        return True  # Succès

    except AssertionError as e:
        print(f"    Test échoué: {e}")
        return False  # Échec

    finally:
        driver.quit()

def main():
    """Menu principal"""
    print("\n" + ""*60)
    print("  SELENIUM DEMO 6: TESTS & ASSERTIONS")
    print(""*60)

    try:
        print("\nChoisissez la démo:")
        print("1. Assertions sur Google")
        print("2. Assertions sur DemoQA")
        print("3. Fonction de test")
        print("4. Toutes les démos")

        choice = input("\nVotre choix (1-4): ").strip()

        if choice == "1":
            demo_google_assertions()
        elif choice == "2":
            demo_demoqa_assertions()
        elif choice == "3":
            result = test_function_with_return()
            print(f"\nRésultat: {'PASS' if result else 'FAIL'}")
        elif choice == "4":
            demo_google_assertions()
            print("\n")
            time.sleep(2)
            demo_demoqa_assertions()
            print("\n")
            time.sleep(2)
            result = test_function_with_return()
            print(f"\nRésultat: {'PASS' if result else 'FAIL'}")
        else:
            print("Choix invalide, exécution de la démo 1...")
            demo_google_assertions()

    except KeyboardInterrupt:
        print("\n\n  Interrompu par l'utilisateur")
    except Exception as e:
        print(f"\n Erreur: {e}")

if __name__ == "__main__":
    main()