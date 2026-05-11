"""
Script principal pour exécuter tous les scénarios de test du TP1
Utilise le pattern Page Object Model (POM)
"""
import sys
import logging
from datetime import datetime
from utils import get_chrome_driver
from pages.login_page import LoginPage
from pages.secure_area_page import SecureAreaPage
from pages.dropdown_page import DropdownPage
from pages.add_remove_page import AddRemovePage


# Configuration des logs
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(f'test_logs_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class TestTP1:
    """Classe principale pour l'exécution des tests TP1"""
    
    def __init__(self):
        """Initialiser le driver et les credentials"""
        self.driver = None
        self.USERNAME = "tomsmith"
        self.PASSWORD = "SuperSecretPassword!"
        self.test_results = []
    
    def setup_driver(self):
        """Initialiser le driver Chrome"""
        try:
            self.driver = get_chrome_driver(headless=False, maximize=True)
            logger.info("✓ Driver Chrome initialisé avec succès")
        except Exception as e:
            logger.error(f"✗ Erreur lors de l'initialisation du driver: {e}")
            sys.exit(1)
    
    def teardown_driver(self):
        """Fermer le driver et le navigateur"""
        if self.driver:
            self.driver.quit()
            logger.info("✓ Navigateur fermé")
    
    def log_test_result(self, test_name, passed, message=""):
        """
        Enregistrer le résultat d'un test
        
        Args:
            test_name: nom du test
            passed: True si réussi, False sinon
            message: message additionnel
        """
        status = "✓ PASS" if passed else "✗ FAIL"
        result = f"{status} - {test_name}"
        if message:
            result += f" ({message})"
        
        self.test_results.append((test_name, passed))
        logger.info(result)
    
    def print_summary(self):
        """Afficher le résumé des tests"""
        logger.info("\n" + "="*60)
        logger.info("RÉSUMÉ DES TESTS")
        logger.info("="*60)
        
        passed = sum(1 for _, result in self.test_results if result)
        total = len(self.test_results)
        
        for test_name, result in self.test_results:
            status = "✓ PASS" if result else "✗ FAIL"
            logger.info(f"{status} - {test_name}")
        
        logger.info("-"*60)
        logger.info(f"Total: {passed}/{total} tests réussis")
        
        if passed == total:
            logger.info("🎉 TOUS LES TESTS SONT PASSÉS!")
        else:
            logger.warning(f"⚠️ {total - passed} test(s) échoué(s)")
        
        logger.info("="*60 + "\n")
    
    def test_partie_1_authentication(self):
        """
        PARTIE 1 — Authentification
        Scénario:
        1. Ouvrir la page de login
        2. Vérifier que c'est la page de login
        3. Saisir username et password
        4. Cliquer sur le bouton de connexion
        5. Vérifier la connexion réussie
        6. Vérifier le message de succès
        7. Vérifier le bouton logout
        8. Cliquer sur logout
        9. Vérifier le retour à la page de login
        """
        logger.info("\n" + "="*60)
        logger.info("PARTIE 1 — AUTHENTIFICATION")
        logger.info("="*60)
        
        try:
            login_page = LoginPage(self.driver)
            secure_page = SecureAreaPage(self.driver)
            
            # Étape 1: Ouvrir la page de login
            logger.info("\n1. Ouvrir la page de login...")
            login_page.open()
            
            # Étape 2: Vérifier que c'est la page de login
            logger.info("2. Vérifier la page de login...")
            is_login = login_page.is_login_page()
            self.log_test_result("Page de login affichée", is_login)
            
            # Étape 3: Saisir les credentials
            logger.info("3. Saisir username et password...")
            login_page.enter_username(self.USERNAME)
            login_page.enter_password(self.PASSWORD)
            self.log_test_result("Credentials saisis", True)
            
            # Étape 4: Cliquer sur le bouton de connexion
            logger.info("4. Cliquer sur le bouton de connexion...")
            login_page.click_login()
            
            # Petite pause pour laisser la page charger
            import time
            time.sleep(2)
            
            # Étape 5-6: Vérifier la connexion réussie et le message
            logger.info("5-6. Vérifier la connexion réussie...")
            is_success = login_page.is_success_message_displayed()
            success_msg = login_page.get_success_message()
            self.log_test_result("Message de succès affiché", is_success, success_msg[:50])
            
            # Étape 7: Vérifier le bouton logout
            logger.info("7. Vérifier la présence du bouton logout...")
            is_logout_btn = login_page.is_logout_button_visible()
            self.log_test_result("Bouton logout visible", is_logout_btn)
            
            # Étape 8: Cliquer sur logout
            logger.info("8. Cliquer sur logout...")
            login_page.click_logout()
            time.sleep(2)
            
            # Étape 9: Vérifier le retour à la page de login
            logger.info("9. Vérifier le retour à la page de login...")
            time.sleep(1)  # Attendre la redirection
            is_back_login = login_page.is_login_page()
            self.log_test_result("Retour page de login après logout", is_back_login)
            
            logger.info("✓ PARTIE 1 terminée avec succès\n")
            
        except Exception as e:
            logger.error(f"✗ Erreur dans PARTIE 1: {e}")
            self.take_screenshot("partie1_error")
    
    def test_partie_2_dropdown(self):
        """
        PARTIE 2 — Liste déroulante
        Scénario:
        1. Ouvrir la page Dropdown
        2. Vérifier que la liste déroulante est présente
        3. Sélectionner Option 1
        4. Vérifier que Option 1 est sélectionnée
        5. Sélectionner Option 2
        6. Vérifier que Option 2 est sélectionnée
        """
        logger.info("\n" + "="*60)
        logger.info("PARTIE 2 — LISTE DÉROULANTE")
        logger.info("="*60)
        
        try:
            dropdown_page = DropdownPage(self.driver)
            
            # Étape 1: Ouvrir la page
            logger.info("\n1. Ouvrir la page Dropdown...")
            dropdown_page.open()
            
            # Étape 2: Vérifier la présence de la dropdown
            logger.info("2. Vérifier la présence de la liste déroulante...")
            is_dropdown = dropdown_page.is_dropdown_present()
            self.log_test_result("Liste déroulante présente", is_dropdown)
            
            # Étape 3: Sélectionner Option 1
            logger.info("3. Sélectionner Option 1...")
            dropdown_page.select_option_by_text("Option 1")
            
            # Étape 4: Vérifier la sélection
            logger.info("4. Vérifier la sélection de Option 1...")
            is_option1_selected = dropdown_page.is_option_selected("Option 1")
            selected = dropdown_page.get_selected_option()
            self.log_test_result("Option 1 sélectionnée", is_option1_selected, f"Sélection: {selected}")
            
            # Étape 5: Sélectionner Option 2
            logger.info("5. Sélectionner Option 2...")
            dropdown_page.select_option_by_text("Option 2")
            
            # Étape 6: Vérifier la sélection
            logger.info("6. Vérifier la sélection de Option 2...")
            is_option2_selected = dropdown_page.is_option_selected("Option 2")
            selected = dropdown_page.get_selected_option()
            self.log_test_result("Option 2 sélectionnée", is_option2_selected, f"Sélection: {selected}")
            
            logger.info("✓ PARTIE 2 terminée avec succès\n")
            
        except Exception as e:
            logger.error(f"✗ Erreur dans PARTIE 2: {e}")
            self.take_screenshot("partie2_error")
    
    def test_partie_3_add_remove(self):
        """
        PARTIE 3 — Ajout et suppression d'éléments
        Scénario:
        1. Ouvrir la page Add/Remove Elements
        2. Cliquer 3 fois sur Add Element
        3. Vérifier 3 boutons Delete
        4. Supprimer 1 élément
        5. Vérifier 2 boutons Delete
        6. Supprimer tous les éléments restants
        7. Vérifier qu'il n'y a plus aucun Delete
        """
        logger.info("\n" + "="*60)
        logger.info("PARTIE 3 — AJOUT ET SUPPRESSION D'ÉLÉMENTS")
        logger.info("="*60)
        
        try:
            add_remove_page = AddRemovePage(self.driver)
            import time
            
            # Étape 1: Ouvrir la page
            logger.info("\n1. Ouvrir la page Add/Remove Elements...")
            add_remove_page.open()
            
            # Étape 2: Ajouter 3 éléments
            logger.info("2. Ajouter 3 éléments...")
            add_remove_page.add_elements(3)
            time.sleep(1)
            
            # Étape 3: Vérifier 3 boutons Delete
            logger.info("3. Vérifier la présence de 3 boutons Delete...")
            count_1 = add_remove_page.get_delete_buttons_count()
            is_3_buttons = add_remove_page.are_delete_buttons_visible(3)
            self.log_test_result("3 boutons Delete présents", is_3_buttons, f"Nombre: {count_1}")
            
            # Étape 4: Supprimer 1 élément
            logger.info("4. Supprimer 1 élément...")
            add_remove_page.delete_first_element()
            time.sleep(0.5)
            
            # Étape 5: Vérifier 2 boutons Delete
            logger.info("5. Vérifier la présence de 2 boutons Delete...")
            count_2 = add_remove_page.get_delete_buttons_count()
            is_2_buttons = add_remove_page.are_delete_buttons_visible(2)
            self.log_test_result("2 boutons Delete restants", is_2_buttons, f"Nombre: {count_2}")
            
            # Étape 6: Supprimer tous les éléments
            logger.info("6. Supprimer tous les éléments restants...")
            add_remove_page.delete_all_elements()
            time.sleep(0.5)
            
            # Étape 7: Vérifier qu'il n'y a plus d'éléments
            logger.info("7. Vérifier qu'il n'y a plus de boutons Delete...")
            is_all_deleted = add_remove_page.are_all_elements_deleted()
            count_final = add_remove_page.get_delete_buttons_count()
            self.log_test_result("Tous les éléments supprimés", is_all_deleted, f"Nombre final: {count_final}")
            
            logger.info("✓ PARTIE 3 terminée avec succès\n")
            
        except Exception as e:
            logger.error(f"✗ Erreur dans PARTIE 3: {e}")
            self.take_screenshot("partie3_error")
    
    def take_screenshot(self, name):
        """
        Prendre une capture d'écran en cas d'erreur
        
        Args:
            name: nom de la capture
        """
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"screenshot_{name}_{timestamp}.png"
            self.driver.save_screenshot(filename)
            logger.info(f"📸 Capture d'écran sauvegardée: {filename}")
        except Exception as e:
            logger.error(f"Erreur lors de la capture d'écran: {e}")
    
    def run_all_tests(self):
        """Exécuter tous les tests"""
        logger.info("\n" + "🚀 "*30)
        logger.info("DÉMARRAGE DES TESTS TP1")
        logger.info("🚀 "*30)
        logger.info(f"Timestamp: {datetime.now()}\n")
        
        try:
            self.setup_driver()
            
            # Exécuter toutes les parties
            self.test_partie_1_authentication()
            self.test_partie_2_dropdown()
            self.test_partie_3_add_remove()
            
        except Exception as e:
            logger.error(f"Erreur critique: {e}")
        
        finally:
            self.teardown_driver()
            self.print_summary()
            
            logger.info("\n" + "="*60)
            logger.info("FIN DE L'EXÉCUTION DES TESTS")
            logger.info("="*60)


def main():
    """Point d'entrée du programme"""
    test = TestTP1()
    test.run_all_tests()


if __name__ == "__main__":
    main()
