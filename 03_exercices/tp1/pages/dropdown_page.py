"""
Page Object pour la page des listes déroulantes
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from pages.base_page import BasePage


class DropdownPage(BasePage):
    """Page Object pour la liste déroulante"""
    
    # Locators
    DROPDOWN = (By.ID, "dropdown")
    SELECTED_OPTION = (By.CSS_SELECTOR, "#dropdown option[selected]")
    
    BASE_URL = "https://the-internet.herokuapp.com/dropdown"
    
    def open(self):
        """Ouvrir la page de dropdown"""
        self.navigate_to(self.BASE_URL)
    
    def is_dropdown_present(self):
        """Vérifier que la liste déroulante est présente"""
        return self.element_exists(self.DROPDOWN)
    
    def select_option_by_text(self, option_text):
        """
        Sélectionner une option par son texte
        
        Args:
            option_text: texte de l'option (ex: "Option 1")
        """
        dropdown_element = self.find_element(self.DROPDOWN)
        if dropdown_element:
            select = Select(dropdown_element)
            select.select_by_visible_text(option_text)
    
    def select_option_by_value(self, option_value):
        """
        Sélectionner une option par sa valeur
        
        Args:
            option_value: valeur de l'option
        """
        dropdown_element = self.find_element(self.DROPDOWN)
        if dropdown_element:
            select = Select(dropdown_element)
            select.select_by_value(option_value)
    
    def get_selected_option(self):
        """
        Récupérer l'option actuellement sélectionnée
        
        Returns:
            texte de l'option sélectionnée
        """
        dropdown_element = self.find_element(self.DROPDOWN)
        if dropdown_element:
            select = Select(dropdown_element)
            return select.first_selected_option.text
        return ""
    
    def get_selected_option_value(self):
        """
        Récupérer la valeur de l'option sélectionnée
        
        Returns:
            valeur de l'option sélectionnée
        """
        dropdown_element = self.find_element(self.DROPDOWN)
        if dropdown_element:
            select = Select(dropdown_element)
            return select.first_selected_option.get_attribute("value")
        return ""
    
    def is_option_selected(self, option_text):
        """
        Vérifier qu'une option est sélectionnée
        
        Args:
            option_text: texte de l'option
        
        Returns:
            True si l'option est sélectionnée
        """
        selected = self.get_selected_option()
        return selected == option_text
