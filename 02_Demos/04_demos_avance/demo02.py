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
    
    def filter_by_category(self, category):
        """Filtrer par catégorie"""
        logger.info(f"Filtering by category: {category}")

        render_id = self.get_render_id()

        filter_option = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, f"//div[@class='filter-option' and text()='{category}']")
            )
        )
        filter_option.click()

        self.wait_for_ajax()
        self.wait_for_results_refresh(render_id)
        logger.info("Filter applied")

    def sort_results(self, sort_option):
        """Trier les résultats"""
        logger.info(f"Sorting by: {sort_option}")

        render_id = self.get_render_id()

        sort_dropdown = self.wait.until(
            EC.element_to_be_clickable((By.ID, "sort-dropdown"))
        )
        Select(sort_dropdown).select_by_value(sort_option)

        self.wait_for_ajax()
        self.wait_for_results_refresh(render_id)
        logger.info("Sorted")

    def click_item(self, item_index):
        """
        Cliquer un item.
        - Re-localise au dernier moment (anti-stale)
        - Scroll dans la vue (anti-not-interactable)
        - Fallback : appel JS direct à openDetailByIndex si le clic natif échoue
        """
        logger.info(f"Clicking item {item_index}...")

        items = self.wait.until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "item-card"))
        )

        if item_index >= len(items):
            logger.error(f"Item {item_index} not found (only {len(items)} items)")
            return None

        item = items[item_index]

        # Lire le titre avant de cliquer
        try:
            title = item.find_element(By.CLASS_NAME, "item-title").text
        except Exception:
            title = f"Item {item_index}"

        # Scroll pour mettre l'élément dans la zone visible
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", item
        )

        # Tentative de clic natif
        panel_opened = False
        try:
            WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(item))
            item.click()
            # Vérifier que le panneau s'est ouvert
            WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".item-detail.open"))
            )
            panel_opened = True
        except Exception:
            pass

        # Fallback : appel direct à la fonction JS du site
        if not panel_opened:
            logger.warning("Native click did not open panel, using JS fallback")
            self.driver.execute_script(f"openDetailByIndex({item_index});")
            self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".item-detail.open"))
            )

        logger.info(f"Clicked: {title}")
        return title if title else None

    def get_item_details(self):
        """Obtenir les détails de l'item ouvert"""
        logger.info("Getting item details...")

        try:
            title       = self.driver.find_element(By.CLASS_NAME, "detail-title").text
            price       = self.driver.find_element(By.CLASS_NAME, "detail-price").text
            description = self.driver.find_element(By.CLASS_NAME, "detail-description").text
            rating      = self.driver.find_element(By.CLASS_NAME, "detail-rating").text

            logger.info(f"  Title  : {title}")
            logger.info(f"  Price  : {price}")
            logger.info(f"  Rating : {rating}")

            return {
                "title": title,
                "price": price,
                "description": description,
                "rating": rating
            }
        except Exception as e:
            logger.error(f"Error getting details: {e}")
            return None

    def add_to_favorites(self):
        """Ajouter aux favoris"""
        logger.info("Adding to favorites...")

        favorite_btn = self.wait.until(
            EC.element_to_be_clickable((By.ID, "favorite-btn"))
        )
        favorite_btn.click()

        # Attendre la notification (classe 'visible' ajoutée par le JS)
        self.wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, ".favorite-notification.visible")
            )
        )
        logger.info("Added to favorites")

    def scroll_to_load_more(self):
        """Scroll pour déclencher le chargement infini"""
        logger.info("Scrolling to load more items...")

        initial_count = len(self.driver.find_elements(By.CLASS_NAME, "item-card"))
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        try:
            WebDriverWait(self.driver, 5).until(
                lambda d: len(
                    d.find_elements(By.CLASS_NAME, "item-card")
                ) > initial_count
            )
            new_count = len(self.driver.find_elements(By.CLASS_NAME, "item-card"))
            logger.info(f"Loaded {new_count - initial_count} more items")
        except Exception:
            logger.info("No more items to load")

    def check_console_errors(self):
        """Vérifier les erreurs console"""
        logger.info("Checking for console errors...")

        logs = self.driver.get_log("browser")
        errors = [log for log in logs if log["level"] == "SEVERE"]

        if errors:
            logger.warning(f"Found {len(errors)} console errors:")
            for error in errors:
                logger.warning(f"  - {error['message']}")
            return False

        logger.info("No console errors")
        return True

    def complete_spa_flow(self):
        logger.info("=" * 60)
        logger.info("SPA COMPLETE FLOW")
        logger.info("=" * 60)

        try:
            # 1. Naviguer vers le site local
            html_path = os.path.abspath("spa_test_site.html")
            url = f"file:///{html_path.replace(os.sep, '/')}"
            self.navigate_to_app(url)

            # 2. Rechercher
            results = self.search_items("laptop")
            if not results:
                return {"success": False, "error": "No results found"}

            # 3. Filtrer (Electronics contient les laptops)
            self.filter_by_category("Electronics")

            # 4. Trier par prix croissant
            self.sort_results("price-asc")

            # 5. Lire les résultats
            search_results = self.get_search_results()
            logger.info(f"Current results: {len(search_results)}")
            for r in search_results:
                logger.info(f"  → {r['title']} — {r['price']}")

            # 6. Cliquer le premier item
            clicked_item = self.click_item(0)
            if not clicked_item:
                # Titre vide possible si rendu pas encore terminé, on continue quand même
                logger.warning("Item clicked but title was empty")

            # 7. Lire les détails
            details = self.get_item_details()

            # 8. Ajouter aux favoris
            self.add_to_favorites()

            # 9. Scroll infini
            self.scroll_to_load_more()

            # 10. Vérifier les erreurs console
            self.check_console_errors()

            logger.info("=" * 60)
            logger.info("SPA FLOW COMPLETED SUCCESSFULLY")
            logger.info("=" * 60)

            return {
                "success": True,
                "item": clicked_item,
                "details": details,
                "total_results": len(search_results)
            }

        except Exception as e:
            logger.error(f"Flow failed: {e}")
            return {"success": False, "error": str(e)}


def main():
    automation = SPAAutomation(headless=False)

    try:
        result = automation.complete_spa_flow()

        if result["success"]:
            print("\nOK SPA Flow Successful!")
            print(f"   Item cliqué     : {result['item']}")
            print(f"   Total résultats : {result['total_results']}")
            if result["details"]:
                print(f"   Prix            : {result['details']['price']}")
                print(f"   Rating          : {result['details']['rating']}")
        else:
            print(f"\nNOK SPA Flow Failed: {result['error']}")

    finally:
        automation.close()


if __name__ == "__main__":
    main()
        

