from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

import os
import logging


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)


class SPAAutomation:

    def __init__(self, headless=False):
        logger.info("Initializing Chrome driver for SPA...")

        options = Options()
        # Ouvre le navigateur en plein écran ou presque, selon le système
        #options.add_argument("--start-maximized")
        # Désactive les demandes de notification des sites web
        options.add_argument("--disable-notifications")
        # Désactive certains popups du navigateur
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--window-size=1920,1080")
        if headless:
            options.add_argument("--headless")

        # Préférences internes de Chrome
        # Elles permettent notamment d'éviter des alertes liées aux mots de passe
        prefs = {
            "profile.password_manager_leak_detection": False,
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False
        }
        # Ajoute les préférences Chrome à la configuration du navigateur
        options.add_experimental_option("prefs", prefs)

        self.driver = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.driver,10)

    def close(self):
        logger.info("Closing driver...")
        self.driver.quit()

    def navigate_to_app(self, url):
        logger.info(f"Navigating to {url}")
        self.driver.get(url)
        self.wait_for_spa_ready()

    def wait_for_spa_ready(self):
        """Attendre que le DOM soit chargé et qu'au moins un item soit visible"""
        logger.info("Waiting for SPA to be ready...")
        self.wait.until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )
        self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "search-result"))
        )
        logger.info("SPA is ready")

    def wait_for_ajax(self):
        """
        Attendre la fin du rendu SPA.
        On surveille la disparition de la classe 'visible' sur le spinner.
        Timeout court (2s) car le spinner est rapide sur un site local.
        """
        logger.info("Waiting for AJAX calls...")
        try:
            WebDriverWait(self.driver, 2).until(
                lambda d: "visible" not in (
                    d.find_element(By.ID, "loading-indicator")
                    .get_attribute("class") or ""
                )
            )
        except Exception:
            pass  # Spinner déjà disparu ou absent = on continue
        logger.info("AJAX calls completed")

    def wait_for_results_refresh(self, previous_render_id=None):
        """
        Attendre que le DOM soit re-rendu après filtre/tri/recherche.
        Utilise l'attribut data-render-id du container pour détecter
        chaque nouveau rendu, même si le nombre de résultats ne change pas.
        """
        logger.info("Waiting for DOM to stabilize...")
        try:
            if previous_render_id is not None:
                # Attendre que le render-id change (= nouveau rendu effectué)
                WebDriverWait(self.driver, 5).until(
                    lambda d: d.find_element(
                        By.ID, "results-container"
                    ).get_attribute("data-render-id") != previous_render_id
                )
            # Dans tous les cas, attendre qu'au moins 1 résultat soit présent
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, "search-result"))
            )
        except Exception:
            pass
        logger.info("DOM stabilized")

    def get_render_id(self):
        """Lire le render-id courant du container (avant une action)"""
        try:
            return self.driver.find_element(
                By.ID, "results-container"
            ).get_attribute("data-render-id")
        except Exception:
            return None

    def search_items(self, search_term):
        """Chercher des items dans l'app"""
        logger.info(f"Searching for: {search_term}")

        render_id = self.get_render_id()

        search_input = self.wait.until(
            EC.presence_of_element_located((By.ID, "search-input"))
        )
        search_input.clear()
        search_input.send_keys(search_term)

        self.wait_for_ajax()
        self.wait_for_results_refresh(render_id)

        results = self.driver.find_elements(By.CLASS_NAME, "search-result")
        logger.info(f"Found {len(results)} results")
        return results
        

