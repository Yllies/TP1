from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BooksPage:
    URL = "https://books.toscrape.com"

    BOOKS = (By.CLASS_NAME,"product_pod")
    TITLE = (By.TAG_NAME, "h3")
    PRICE = (By.CLASS_NAME, "price_color")
    AVAILABILITY = (By.CLASS_NAME, "instock")
    RATING = (By.CLASS_NAME, "star-rating")

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self):
        self.driver.get(self.URL)

    def wait_for_books_to_load(self):
        self.wait.until(EC.presence_of_all_elements_located(self.BOOKS))

    def get_book_elements(self):
        return self.driver.find_elements(*self.BOOKS)
    
    def extract_book_data(self):
        books = []
        book_elements = self.get_book_elements()

        for i,book in enumerate(book_elements):
            try:
                title_elem = book.find_element(*self.TITLE)
                title = title_elem.text.strip()

                price_elem = book.find_element(*self.PRICE)
                price_text = price_elem.text.strip()
                price = float(price_text.replace("£", ""))

                avail_elem = book.find_element(*self.AVAILABILITY)
                availability = avail_elem.text.strip()

                rating_elem = book.find_element(*self.RATING)
                rating = rating_elem.get_attribute("class").split()[-1]

                books.append({
                    "id": i + 1,
                    "title": title,
                    "price": price,
                    "availability": availability,
                    "rating": rating
                })
            
            except Exception as e:
                print(f"Erreur extraction livre {i+1}: {e}")
        
        return books
    
