from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class DynamicLoadingPage(BasePage):
    BASE_URL = "https://the-internet.herokuapp.com/dynamic_loading"
    
    # les localisateurs
    EXAMPLE_2_LINK = (By.LINK_TEXT, "Example 2: Element rendered after the fact")
    START_BUTTON = (By.CSS_SELECTOR, "#start button")
    HELLO_WORLD_TEXT = (By.CSS_SELECTOR, "#finish h4")

    def open(self):
        """Aller sur la page"""
        self.navigate_to(self.BASE_URL)

    def click_example_2(self):
        """Cliquer sur l'exemple 2"""
        self.click(self.EXAMPLE_2_LINK)

    def is_start_present(self):
        """Le bouton Start est là?"""
        return self.is_present(self.START_BUTTON)

    def click_start(self):
        """Cliquer sur Start"""
        self.click(self.START_BUTTON)

    def wait_for_hello(self):
        """Attendre que le texte apparaisse"""
        self.wait_for_visibility(self.HELLO_WORLD_TEXT)

    def get_hello_text(self):
        """Récupérer le texte"""
        return self.get_text(self.HELLO_WORLD_TEXT)
