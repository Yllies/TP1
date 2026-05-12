from selenium import webdriver

from pages.home_page import HomePage
from pages.products_page import ProductsPage
from utils.logger_config import get_logger
from utils.screenshot import take_screenshot
from utils.report import Report

SEARCH_QUERY = "top"

logger = get_logger("test_search_products")


def test_search_products():
    logger.info("=== DÉMARRAGE DU TEST ===")
    driver = webdriver.Chrome()
    products = []
    success = False

    try:
        home_page = HomePage(driver)
        products_page = ProductsPage(driver)

        home_page.open()
        screenshot_path = take_screenshot(driver, "01_accueil")
        logger.info(f"Screenshot accueil : {screenshot_path}")

        assert (
            "Automation Exercise" in driver.title
        ), f"Titre inattendu : {driver.title}"
        logger.info(f"Titre de page vérifié : '{driver.title}'")

        home_page.go_to_products()
        products_page.verify_loaded()

        products_page.search(SEARCH_QUERY)

        screenshot_path = take_screenshot(driver, "02_resultats_recherche")
        logger.info(f"Screenshot résultats : {screenshot_path}")

        products = products_page.get_products()

        assert len(products) > 0, "Aucun produit trouvé dans les résultats"
        logger.info(f"Assertion 1 OK — {len(products)} produit(s) trouvé(s)")

        matching = [p for p in products if SEARCH_QUERY.lower() in p.name.lower()]
        ratio = len(matching) / len(products)
        assert ratio > 0.5, (
            f"Trop peu de résultats pertinents : {len(matching)}/{len(products)} "
            f"contiennent '{SEARCH_QUERY}' ({ratio:.0%})"
        )
        logger.info(
            f"Assertion 2 OK — {len(matching)}/{len(products)} produits "
            f"contiennent '{SEARCH_QUERY}' ({ratio:.0%})"
        )

        success = True
        logger.info("=== TEST TERMINÉ AVEC SUCCÈS ===")

    except AssertionError as e:
        logger.error(f"Assertion échouée : {e}")
        screenshot_path = take_screenshot(driver, "03_erreur_assertion")
        logger.error(f"Screenshot erreur : {screenshot_path}")

    except Exception as e:
        logger.error(f"Erreur inattendue : {e}")
        screenshot_path = take_screenshot(driver, "03_erreur_exception")
        logger.error(f"Screenshot erreur : {screenshot_path}")

    finally:
        report = Report(output_file="rapport_tp4.txt")
        report.generate(products, success=success)
        logger.info("Rapport généré : rapport_tp4.txt")

        driver.quit()
        logger.info("Navigateur fermé")


if __name__ == "__main__":
    test_search_products()
