from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class DynamicControlsPage(BasePage):
    BASE_URL = "https://the-internet.herokuapp.com/dynamic_controls"

    # où trouver les choses sur la page
    CHECKBOX_CONTAINER = (By.ID, "checkbox")
    CHECKBOX = (By.CSS_SELECTOR, "#checkbox input[type='checkbox']")
    REMOVE_ADD_BUTTON = (By.CSS_SELECTOR, "#checkbox-example button")
    MESSAGE = (By.ID, "message")
    ENABLE_BUTTON = (By.CSS_SELECTOR, "#input-example button")
    TEXT_INPUT = (By.CSS_SELECTOR, "#input-example input[type='text']")

    def open(self):
        """Aller sur la page"""
        self.navigate_to(self.BASE_URL)

    def is_loaded(self):
        """C'est bon, la page est chargée?"""
        return self.is_present(self.REMOVE_ADD_BUTTON) and self.is_present(self.ENABLE_BUTTON)

    def is_checkbox_present(self):
        """Est-ce que la checkbox est là?"""
        return self.is_present(self.CHECKBOX_CONTAINER)

    def click_remove_or_add(self):
        """Cliquer sur Remove/Add"""
        self.click(self.REMOVE_ADD_BUTTON)

    def wait_checkbox_disappears(self):
        """Attendre qu'elle disparaisse"""
        self.wait_for_invisibility(self.CHECKBOX_CONTAINER)

    def wait_checkbox_appears(self):
        """Attendre qu'elle réapparaisse"""
        self.wait_for_visibility(self.CHECKBOX_CONTAINER)

    def get_message(self):
        """Récupérer le message affiché"""
        return self.get_text(self.MESSAGE)

    def is_input_disabled(self):
        """Le champ est désactivé?"""
        input_element = self.find(self.TEXT_INPUT)
        return not input_element.is_enabled()

    def click_enable(self):
        """Cliquer sur Enable"""
        self.click(self.ENABLE_BUTTON)

    def wait_input_enabled(self):
        """Attendre que le champ soit activé"""
        input_element = self.wait_for_visibility(self.TEXT_INPUT)
        self.wait.until(lambda driver: input_element.is_enabled())
        return input_element

    def enter_text(self, value):
        """Taper du texte"""
        self.send_keys(self.TEXT_INPUT, value)
        return self.get_text(self.TEXT_INPUT)
