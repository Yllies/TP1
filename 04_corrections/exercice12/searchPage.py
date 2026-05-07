from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class SearchPage:
    URL = "https://practicesoftwaretesting.com"
    SEARCH_INPUT = (By.ID,"search-query")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    def __init__(self,driver,timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver,timeout)

    def open(self):
        self.driver.get(self.URL)

    def wait_for_page_ready(self):
        self.wait.until(EC.presence_of_element_located(self.SEARCH_INPUT))

    def get_search_field(self):
        return self.driver.find_element(*self.SEARCH_INPUT)
    
    def get_search_button(self):
        return self.driver.find_element(*self.SEARCH_BUTTON)
    
    def search_products(self,query):
        search_field = self.get_search_field()
        search_field.clear()
        search_field.send_keys(query)
        search_button = self.get_search_button()
        search_button.click()

    def wait_for_results(self):
        # solution 1
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'[data-test="search_completed"]')))
        # solution 2
        # time.sleep(2)
        # self.wait.until(EC.presence_of_all_elements_located((By.XPATH,"//a[@class='card']")))

    def get_result_cards(self):
        return self.driver.find_elements(By.CSS_SELECTOR,"a.card")
    
    def extract_product_data(self):
        products_data = []
        self.wait_for_results()
        products = self.get_result_cards()

        for i, product in enumerate(products):
            try:
                name_elem = product.find_element(By.TAG_NAME, "h5")
                name = name_elem.text

                price_elem = product.find_element(By.CSS_SELECTOR, "[data-test='product-price']")
                price_text = price_elem.text.replace("$", "").strip()
                price = float(price_text)

                products_data.append({
                    "id": i + 1,
                    "name": name,
                    "price": price
                })

            except Exception as e:
                print(f"Erreur extraction produit {i+1}: {e}")

        return products_data
    
