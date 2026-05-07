from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


def demo_saucedemo_login():
    """Login sur Sauce Demo"""
    print("\n" + "="*60)
    print("DEMO: SAUCE DEMO LOGIN")
    print("="*60)

    driver = webdriver.Chrome()

    try:
        print("\n1. Navigation vers Sauce Demo...")
        driver.get("https://www.saucedemo.com/")
        time.sleep(2)
        print("    Page chargée")

        print("\n2. Remplissage du formulaire de login...")
        
        # Username
        print("   a) Saisie du username...")
        username = driver.find_element(By.ID, "user-name")
        username.send_keys("standard_user")
        print("       Username saisi")

        # Password
        print("   b) Saisie du password...")
        password = driver.find_element(By.ID, "password")
        password.send_keys("secret_sauce")
        print("       Password saisi")

        # Login
        print("\n3. Clic sur Login...")
        login_btn = driver.find_element(By.ID, "login-button")
        login_btn.click()
        time.sleep(2)
        print("    Login effectué")

        # Vérification
        print("\n4. Vérification de la connexion...")
        try:
            inventory = driver.find_element(By.CLASS_NAME, "inventory_list")
            print("    Connecté! Produits affichés")
        except:
            print("     Produits non trouvés")

    except Exception as e:
        print(f"    Erreur: {e}")
        import traceback
        traceback.print_exc()
    finally:
        print("\n6. Fermeture...")
        driver.quit()
        print("    Fermé")


def demo_saucedemo_shopping():
    """Ajout au panier et checkout"""
    print("\n" + "="*60)
    print("DEMO: SAUCE DEMO SHOPPING & CHECKOUT")
    print("="*60)

    driver = webdriver.Chrome()

    try:
        print("\n1. Navigation et login...")
        driver.get("https://www.saucedemo.com/")
        time.sleep(2)

        # Login
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        time.sleep(2)
        print("    Connecté")

        # Ajouter des produits au panier
        print("\n2. Ajout de produits au panier...")
        
        # Trouver les produits
        add_to_cart_buttons = driver.find_elements(By.CLASS_NAME, "btn_inventory")
        print(f"    {len(add_to_cart_buttons)} produits disponibles")

        # Ajouter les 2 premiers
        for i in range(min(2, len(add_to_cart_buttons))):
            product_name = driver.find_elements(By.CLASS_NAME, "inventory_item_name")[i].text
            print(f"\n   Produit {i+1}: {product_name}")
            add_to_cart_buttons[i].click()
            time.sleep(0.5)
            print(f"       Ajouté au panier")

        # Ouvrir le panier
        print("\n3. Ouverture du panier...")
        cart_btn = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        cart_btn.click()
        time.sleep(2)
        print("    Panier ouvert")

        # Vérifier les produits dans le panier
        print("\n4. Vérification du panier...")
        cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
        #assert len(cart_items) == 2, f'Attendu 2 produits mais {len(cart_items)} trouvé'
        print(f"    {len(cart_items)} produit(s) dans le panier")

        # Checkout
        print("\n5. Début du checkout...")
        checkout_btn = driver.find_element(By.ID, "checkout")
        checkout_btn.click()
        time.sleep(2)
        print("    Page de checkout")

        # Formulaire d'information
        print("\n6. Remplissage des informations...")
        try:
            driver.find_element(By.ID, "first-name").send_keys("Jean")
            driver.find_element(By.ID, "last-name").send_keys("Dupont")
            driver.find_element(By.ID, "postal-code").send_keys("75000")
            print("    Informations saisies")
        except Exception as e:
            print(f"     Erreur formulaire: {e}")

        # Continuer
        print("\n7. Continuation du checkout...")
        try:
            continue_btn = driver.find_element(By.ID, "continue")
            continue_btn.click()
            time.sleep(2)
            print("    Passage à la page de confirmation")
        except Exception as e:
            print(f"     Erreur: {e}")


        # Finir le checkout
        print("\n8. Finalisation de la commande...")
        try:
            finish_btn = driver.find_element(By.ID, "finish")
            finish_btn.click()
            time.sleep(2)
            print("    Commande finalisée!")
            
            # Message de confirmation
            try:
                confirmation = driver.find_element(By.CLASS_NAME, "complete-header").text
                print(f"   Message: {confirmation}")
            except:
                pass
        except Exception as e:
            print(f"     Erreur finalisation: {e}")

    except Exception as e:
        print(f"    Erreur: {e}")
    finally:
        print("\n10. Fermeture...")
        driver.quit()
        print("    Fermé")


def demo_saucedemo_sorting():
    """Démonstration du tri et du filtrage"""
    print("\n" + "="*60)
    print("DEMO: SAUCE DEMO SORTING & FILTERING")
    print("="*60)

    driver = webdriver.Chrome()

    try:
        print("\n1. Navigation et login...")
        driver.get("https://www.saucedemo.com/")
        time.sleep(2)

        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        time.sleep(2)
        print("    Connecté")


        # Récupérer les prix avant tri
        print("\n2. Récupération des prix avant tri...")
        prices_before = []
        price_elements = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
        for price in price_elements[:5]:
            price_text = price.text.replace("$", "")
            try:
                prices_before.append(float(price_text))
                print(f"   ${price_text}")
            except:
                pass

        # Tri
        print("\n3. Application du tri (Prix: Bas à Haut)...")
        sort_dropdown = driver.find_element(By.CLASS_NAME, "product_sort_container")
        select = Select(sort_dropdown)

        print("   Options disponibles:")
        for option in select.options:
            print(f"      - {option.text}")

        select.select_by_value("lohi")  # Price Low to High
        time.sleep(2)
        print("    Tri appliqué")

        # Vérifier les prix après tri
        print("\n4. Prix après tri (Bas à Haut):")
        prices_after = []
        price_elements = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
        for price in price_elements[:5]:
            price_text = price.text.replace("$", "")
            try:
                prices_after.append(float(price_text))
                print(f"   ${price_text}")
            except:
                pass

        # Vérifier si les prix sont triés
        if prices_after == sorted(prices_after):
            print("\n    Prix correctement triés!")
        else:
            print("\n     Les prix ne sont pas correctement triés")

    except Exception as e:
        print(f"    Erreur: {e}")
    finally:
        print("\n6. Fermeture...")
        driver.quit()
        print("    Fermé")
        


def main():
    """Menu principal"""
    print("\n" + ""*60)
    print("  SELENIUM DEMO: SAUCE DEMO E-COMMERCE")
    print(""*60)

    try:
        print("\nChoisissez la démo:")
        print("1. Login")
        print("2. Shopping et Checkout complet")
        print("3. Tri et Filtrage")
        print("4. Toutes les démos")

        choice = input("\nVotre choix (1-4): ").strip()

        if choice == "1":
            demo_saucedemo_login()
        elif choice == "2":
            demo_saucedemo_shopping()
        elif choice == "3":
            demo_saucedemo_sorting()
        elif choice == "4":
            demo_saucedemo_login()
            demo_saucedemo_shopping()
            demo_saucedemo_sorting()
        else:
            print("Choix invalide, exécution de la démo 1...")
            demo_saucedemo_login()

    except KeyboardInterrupt:
        print("\n\n  Interrompu par l'utilisateur")
    except Exception as e:
        print(f"\n Erreur: {e}")

if __name__ == "__main__":
    main()
