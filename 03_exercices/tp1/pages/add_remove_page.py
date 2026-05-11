"""
Page Object pour la page d'ajout/suppression d'éléments
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AddRemovePage(BasePage):
    """Page Object pour l'ajout/suppression dynamique d'éléments"""
    
    # Locators
    ADD_BUTTON = (By.CSS_SELECTOR, "button[onclick='addElement()']")
    DELETE_BUTTONS = (By.CSS_SELECTOR, "button[onclick='deleteElement()']")
    ELEMENTS_CONTAINER = (By.ID, "elements")
    
    BASE_URL = "https://the-internet.herokuapp.com/add_remove_elements/"
    
    def open(self):
        """Ouvrir la page Add/Remove Elements"""
        self.navigate_to(self.BASE_URL)
    
    def click_add_element(self):
        """Cliquer sur le bouton 'Add Element'"""
        self.click_element(self.ADD_BUTTON)
    
    def add_elements(self, count):
        """
        Ajouter plusieurs éléments
        
        Args:
            count: nombre d'éléments à ajouter
        """
        for _ in range(count):
            self.click_add_element()
    
    def get_delete_buttons_count(self):
        """
        Récupérer le nombre de boutons Delete
        
        Returns:
            nombre de boutons Delete
        """
        buttons = self.find_elements(self.DELETE_BUTTONS)
        return len(buttons)
    
    def are_delete_buttons_visible(self, expected_count):
        """
        Vérifier que le nombre attendu de boutons Delete est visible
        
        Args:
            expected_count: nombre attendu de boutons
        
        Returns:
            True si le nombre correspond
        """
        return self.get_delete_buttons_count() == expected_count
    
    def delete_first_element(self):
        """Supprimer le premier élément"""
        buttons = self.find_elements(self.DELETE_BUTTONS)
        if buttons:
            buttons[0].click()
    
    def delete_all_elements(self):
        """Supprimer tous les éléments"""
        while self.get_delete_buttons_count() > 0:
            self.delete_first_element()
    
    def are_all_elements_deleted(self):
        """Vérifier que tous les éléments ont été supprimés"""
        return self.get_delete_buttons_count() == 0
