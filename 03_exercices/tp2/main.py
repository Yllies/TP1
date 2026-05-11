import logging
from datetime import datetime
from driver_factory import create_chrome_driver
from pages.dynamic_controls_page import DynamicControlsPage
from pages.dynamic_loading_page import DynamicLoadingPage
from pages.notification_page import NotificationPage
from pages.infinite_scroll_page import InfiniteScrollPage


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)



class TP2Executor:
    def __init__(self, headless=False):
        self.driver = create_chrome_driver(headless=headless)
        self.start_time = datetime.now()
        self.test_results = []

    def log_result(self, name, passed, message=""):
        """Noter le résultat"""
        status = "✓ OK" if passed else "✗ ERREUR"
        self.test_results.append((name, passed, message))
        logger.info(f"{status} - {name} {message}")

    def take_screenshot(self, name):
        """Prendre une capture"""
        filename = f"tp2_{name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        self.driver.save_screenshot(filename)
        logger.info(f"Capture d'écran sauvegardée: {filename}")

    def run_dynamic_controls(self):
        """Test des contrôles dynamiques"""
        page = DynamicControlsPage(self.driver)
        try:
            logger.info("=== Contrôles dynamiques ===")
            page.open()
            assert page.is_loaded(), "La page Contrôles dynamiques n'a pas chargé"
            assert page.is_checkbox_present(), "La case à cocher devrait être présente"

            page.click_remove_or_add()
            page.wait_checkbox_disappears()
            assert "It's gone!" in page.get_message(), "Message de suppression non trouvé"

            page.click_remove_or_add()
            page.wait_checkbox_appears()
            assert "It's back!" in page.get_message(), "Message d'ajout non trouvé"

            assert page.is_input_disabled(), "Le champ devrait être désactivé au départ"
            page.click_enable()
            page.wait_input_enabled()
            assert not page.is_input_disabled(), "Le champ devrait être activé"

            test_text = "Selenium TP2"
            page.enter_text(test_text)
            assert page.find(page.TEXT_INPUT).get_attribute("value") == test_text, "Le texte saisi ne correspond pas"

            self.log_result("Contrôles dynamiques", True)
        except Exception as exc:
            self.log_result("Contrôles dynamiques", False, str(exc))
            self.take_screenshot("dynamic_controls")

    def run_dynamic_loading(self):
        """Test du chargement dynamique"""
        page = DynamicLoadingPage(self.driver)
        try:
            logger.info("=== Chargement dynamique ===")
            page.open()
            page.click_example_2()
            assert page.is_start_present(), "Le bouton Démarrer manque"
            page.click_start()
            page.wait_for_hello()
            assert page.get_hello_text() == "Hello World!", "Le texte 'Hello World!' n'a pas été trouvé"
            self.log_result("Chargement dynamique", True)
        except Exception as exc:
            self.log_result("Chargement dynamique", False, str(exc))
            self.take_screenshot("dynamic_loading")

    def run_notification_message(self):
        """Test des notifications"""
        page = NotificationPage(self.driver)
        try:
            logger.info("=== Messages de notification ===")
            page.open()
            first_message = page.wait_for_message()
            assert first_message, "Aucun message de notification initial"

            for i in range(3):
                page.click_refresh()
                message = page.wait_for_message()
                assert message, f"Notification absente après le clic #{i+1}"
                assert page.is_message_expected(message), f"Message inattendu: {message}"

            self.log_result("Messages de notification", True)
        except Exception as exc:
            self.log_result("Messages de notification", False, str(exc))
            self.take_screenshot("notification_message")

    def run_infinite_scroll(self):
        """Test du défilement infini"""
        page = InfiniteScrollPage(self.driver)
        try:
            logger.info("=== Défilement infini ===")
            page.open()
            initial_count = page.get_block_count()
            assert initial_count >= 1, "Les blocs initiaux du défilement manquent"

            page.scroll_down()
            page.wait_for_additional_blocks(initial_count)
            final_count = page.get_block_count()
            assert final_count > initial_count, "Aucun nouveau bloc après le défilement"
            self.log_result("Défilement infini", True)
        except Exception as exc:
            self.log_result("Défilement infini", False, str(exc))
            self.take_screenshot("infinite_scroll")

    def run_all(self):
        """Lancer tous les tests"""
        try:
            self.run_dynamic_controls()
            self.run_dynamic_loading()
            self.run_notification_message()
            self.run_infinite_scroll()
        finally:
            self.driver.quit()
            self.print_summary()

    def print_summary(self):
        """Afficher le résumé final"""
        logger.info("=== Résumé TP2 ===")
        for name, passed, message in self.test_results:
            status = "✓ OK" if passed else "✗ ERREUR"
            logger.info(f"{name}: {status} {message}")
        success_count = sum(1 for _, passed, _ in self.test_results if passed)
        logger.info(f"{success_count}/{len(self.test_results)} scénarios réussis")


if __name__ == "__main__":
    TP2Executor(headless=False).run_all()
