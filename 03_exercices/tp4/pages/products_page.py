from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.product_card import ProductCard
from utils.logger_config import get_logger


class ProductsPage:
    SEARCH_INPUT = (By.ID, "search_product")
    SEARCH_BUTTON = (By.ID, "submit_search")
    PAGE_HEADING = (By.CSS_SELECTOR, ".features_items h2.title")

    PRODUCT_ITEMS = (By.CSS_SELECTOR, ".productinfo")
    PRODUCT_NAME = (By.CSS_SELECTOR, "p")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "h2")

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        self.logger = get_logger(self.__class__.__name__)

    def verify_loaded(self):
        """Vérifie que la page Products est bien chargée."""
        heading = self.wait.until(EC.visibility_of_element_located(self.PAGE_HEADING))
        assert (
            "ALL PRODUCTS" in heading.text.upper()
        ), f"Page Products non chargée : {heading.text}"
        self.logger.info("Page Products chargée")

    def search(self, query: str):
        """Saisit le texte de recherche et soumet le formulaire."""
        self.logger.info(f"Recherche : '{query}'")
        search_input = self.wait.until(
            EC.visibility_of_element_located(self.SEARCH_INPUT)
        )
        search_input.clear()
        search_input.send_keys(query)
        self.wait.until(EC.element_to_be_clickable(self.SEARCH_BUTTON)).click()

        # Attendre que le titre de la section de résultats soit visible.
        self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "h2.title.text-center"))
        )
        self.logger.info("Résultats de recherche chargés")

    def get_products(self) -> list[ProductCard]:
        items = self.driver.find_elements(*self.PRODUCT_ITEMS)
        products = []

        for item in items:
            try:
                name = item.find_element(*self.PRODUCT_NAME).text.strip()
                price = item.find_element(*self.PRODUCT_PRICE).text.strip()
                products.append(ProductCard(name=name, price=price))
            except Exception as e:
                self.logger.debug(f"Produit ignoré (élément manquant) : {e}")
                continue

        self.logger.info(f"{len(products)} produit(s) extrait(s)")
        return products
