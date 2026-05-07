from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import logging
from datetime import datetime
import os

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('selenium_test.log'),
        logging.StreamHandler() # pour affciher dans la console
    ]
)

logger = logging.getLogger(__name__)

# Créer dossier pour screenshots
os.makedirs('screenshots', exist_ok=True)

def demo_with_logging():
    """Démo avec logging détaillé"""
    print("\n" + "="*60)
    print("DEMO: LOGGING ET GESTION D'ERREURS")
    print("="*60)

    try:
        logger.info("=" * 60)
        logger.info("Démarrage du test")
        logger.info("=" * 60)

        # Initialisation
        logger.info("Initialisation du WebDriver...")
        driver = webdriver.Chrome()
        logger.info(" WebDriver initialisé")

        # Navigation
        logger.info("Navigation vers Wikipedia...")
        driver.get("https://en.wikipedia.org/wiki/Python_(programming_language)")
        # screenshot_name = f"screenshots/test_good_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        # driver.save_screenshot(screenshot_name)
        logger.info(f" Page chargée. Titre: {driver.title}")

        # Extraction du contenu
        logger.info("Extraction du contenu de la page...")

        # Titre principal
        h1 = driver.find_element(By.TAG_NAME, "h1")
        logger.info(f" Titre trouvé: {h1.text}")

        # Paragraphes d'introduction
        intro_paragraphs = driver.find_elements(By.CSS_SELECTOR, "#mw-content-text > div.mw-parser-output > p")
        logger.info(f" {len(intro_paragraphs)} paragraphes d'introduction trouvés")

        # Infobox
        try:
            infobox = driver.find_element(By.CLASS_NAME, "infobox")
            logger.info(f" Infobox trouvée")
        except:
            logger.warning("  Infobox non trouvée")

        logger.info(" TEST PASSÉ")

    except Exception as e:
        logger.error(f" ERREUR: {e}")
        logger.error("Stack trace:", exc_info=True)

        # Prendre une screenshot
        if driver:
            screenshot_name = f"screenshots/error_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            driver.save_screenshot(screenshot_name)
            logger.info(f" Screenshot sauvegardé: {screenshot_name}")

    finally:
        if driver:
            logger.info("Fermeture du WebDriver...")
            driver.quit()
            logger.info(" WebDriver fermé")

        logger.info("=" * 60)
        logger.info("Fin du test")
        logger.info("=" * 60)




def demo_error_recovery():
    """Démo avec récupération d'erreurs"""
    print("\n" + "="*60)
    print("DEMO: RÉCUPÉRATION D'ERREURS")
    print("="*60)

    driver = webdriver.Chrome()

    try:
        logger.info("\n Test: Recherche Wikipedia")

        driver.get("https://wikipedia.org")
        logger.info(f" Page chargée: {driver.title}")

        # Essayer de trouver un élément
        logger.info("Recherche de la barre de recherche...")
        try:
            search_box = driver.find_element(By.ID, "searchInput")
            logger.info(" Barre trouvée avec ID")
        except:
            logger.warning("  ID non trouvé, essai avec selector CSS...")
            try:
                search_box = driver.find_element(By.CSS_SELECTOR, "input[name='search']")
                logger.info(" Barre trouvée avec CSS")
            except:
                logger.error(" Impossible de trouver la barre")
                search_box = None

        if search_box:
            logger.info("Saisie du texte...")
            search_box.send_keys("Python")
            time.sleep(1)
            logger.info(" Texte saisi")
        else:
            logger.warning("  Impossible de saisir sans barre")

        # Vérification du contenu
        logger.info("Vérification du contenu de la page...")
        page_text = driver.page_source
        if "Python" in page_text or "wikipedia" in page_text:
            logger.info(" Contenu vérifié")
        else:
            logger.warning("  Contenu attendu non trouvé")

        logger.info(" Test complété")

    except Exception as e:
        logger.error(f" Erreur non gérée: {e}")
        import traceback
        logger.error(traceback.format_exc())

    finally:
        driver.quit()
        logger.info("Fermeture")



def demo_assertions_with_logging():
    """Démo avec assertions et logging"""
    print("\n" + "="*60)
    print("DEMO: ASSERTIONS AVEC LOGGING")
    print("="*60)

    driver = webdriver.Chrome()

    try:
        logger.info("\n Test: Assertions sur DemoQA")

        driver.get("https://demoqa.com/text-box")
        logger.info(f" Page chargée: {driver.title}")

        # Assertion 1
        logger.info("Assertion 1: Vérifier le titre...")
        #assert "DemoQA" in driver.title   # erreur provoque pour tester la capture d'ecran
        assert "demosite" in driver.title
        logger.info(" Titre correct")

        # Assertion 2
        logger.info("Assertion 2: Formulaire existe...")
        form = driver.find_element(By.ID, "userForm")
        assert form is not None
        logger.info(" Formulaire trouvé")

        # Assertion 3
        logger.info("Assertion 3: Champs accessibles...")
        name_field = driver.find_element(By.ID, "userName")
        assert name_field.is_enabled()
        logger.info(" Champ nom enabled")

        # Assertion 4
        logger.info("Assertion 4: Saisie de données...")
        name_field.send_keys("Test User")
        #assert "Test User" in name_field.get_attribute("value")
        assert "Toto" in name_field.get_attribute("value") , "Valeur incorrect dans l'input" # erreur provoque pour tester la capture d'ecran
        logger.info(" Données saisies correctement")

        # Assertion 5
        logger.info("Assertion 5: Bouton submit...")
        submit_btn = driver.find_element(By.ID, "submit")
        assert submit_btn.is_displayed()
        assert submit_btn.is_enabled()
        logger.info(" Bouton submit prêt")

        logger.info("\n TOUS LES TESTS SONT PASSÉS")

    except AssertionError as e:
        logger.error(f" Assertion échouée: {e}")
        screenshot_name = f"screenshots/assertion_fail_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        driver.save_screenshot(screenshot_name)
        logger.info(f" Screenshot: {screenshot_name}")

    except Exception as e:
        logger.error(f" Erreur: {e}")
        import traceback
        logger.error(traceback.format_exc())

    finally:
        driver.quit()
        logger.info("Test terminé\n")


demo_assertions_with_logging()