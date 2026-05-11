from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://practicesoftwaretesting.com"
        
        self.SEARCH_INPUT = (By.ID, "search-query")
        self.SEARCH_BUTTON = (By.CSS_SELECTOR, "button[data-test='search-submit']")
        self.PRODUCT_CARDS = (By.CSS_SELECTOR, ".card")
        self.PRODUCT_NAME = (By.CSS_SELECTOR, ".card-title")
        self.PRODUCT_PRICE = (By.CSS_SELECTOR, "[data-test='product-price']")

    def open(self):
        self.driver.get(self.url)

    def is_form_ready(self):
        """Vérifie que les éléments de recherche sont visibles (Tâche 1)"""
        wait = WebDriverWait(self.driver, 10)
        input_visible = wait.until(EC.visibility_of_element_located(self.SEARCH_INPUT))
        btn_visible = wait.until(EC.visibility_of_element_located(self.SEARCH_BUTTON))
        return input_visible and btn_visible

    def search_for(self, term):
        """Saisit le terme et lance la recherche (Tâche 2)"""
        search_field = self.driver.find_element(*self.SEARCH_INPUT)
        search_field.clear()
        search_field.send_keys(term)
        self.driver.find_element(*self.SEARCH_BUTTON).click()

    def wait_for_results(self):
        """Attente explicite du chargement (Tâche 2)"""
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.PRODUCT_CARDS)
        )

    def get_results_data(self):
        """Extrait les données de chaque produit (Tâche 3)"""
        cards = self.driver.find_elements(*self.PRODUCT_CARDS)
        products = []

        for card in cards:
            name = card.find_element(*self.PRODUCT_NAME).text.strip()
            price_text = card.find_element(*self.PRODUCT_PRICE).text.strip()
            price_value = float(
                price_text.replace('€', '').replace('$', '').replace('£', '').replace(',', '.').strip()
            )

            products.append({
                "name": name,
                "price_display": price_text,
                "price": price_value
            })

        return products