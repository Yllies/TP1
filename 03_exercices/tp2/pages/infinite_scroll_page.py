"""
Page Object pour la page Infinite Scroll
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InfiniteScrollPage(BasePage):
    BASE_URL = "https://the-internet.herokuapp.com/infinite_scroll"
    
    # les blocs de contenu qu'on charge dynamiquement
    CONTENT_BLOCKS = (By.CSS_SELECTOR, ".jscroll-added")

    def open(self):
        """Aller sur la page"""
        self.navigate_to(self.BASE_URL)

    def get_block_count(self):
        """Compter les blocs visibles"""
        return len(self.driver.find_elements(*self.CONTENT_BLOCKS))

    def wait_for_additional_blocks(self, previous_count, timeout=10):
        """Attendre que de nouveaux blocs arrivent"""
        self.wait.until(
            lambda driver: len(driver.find_elements(*self.CONTENT_BLOCKS)) > previous_count
        )

    def scroll_down(self):
        """Faire défiler pour charger du contenu"""
        self.scroll_to_bottom()
