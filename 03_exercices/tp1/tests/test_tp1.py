"""
Script de test alternatif avec unittest (optionnel)
Permet d'exécuter les tests avec pytest ou unittest
"""
import unittest
import sys
import time
from utils import get_chrome_driver
from pages.login_page import LoginPage
from pages.dropdown_page import DropdownPage
from pages.add_remove_page import AddRemovePage


class TestTP1(unittest.TestCase):
    """Tests unitaires pour TP1"""
    
    @classmethod
    def setUpClass(cls):
        """Initialiser le driver au démarrage"""
        cls.driver = get_chrome_driver(headless=False, maximize=True)
        cls.USERNAME = "tomsmith"
        cls.PASSWORD = "SuperSecretPassword!"
    
    @classmethod
    def tearDownClass(cls):
        """Fermer le driver à la fin"""
        cls.driver.quit()
    
    def test_01_login_page_opens(self):
        """Test 1: La page de login s'ouvre"""
        login_page = LoginPage(self.driver)
        login_page.open()
        self.assertTrue(login_page.is_login_page(), "La page de login n'est pas affichée")
    
    def test_02_login_success(self):
        """Test 2: La connexion réussit"""
        login_page = LoginPage(self.driver)
        login_page.open()
        login_page.login(self.USERNAME, self.PASSWORD)
        time.sleep(2)
        self.assertTrue(login_page.is_success_message_displayed(), "Le message de succès n'est pas affiché")
    
    def test_03_logout_button_visible(self):
        """Test 3: Le bouton logout est visible"""
        login_page = LoginPage(self.driver)
        self.assertTrue(login_page.is_logout_button_visible(), "Le bouton logout n'est pas visible")
    
    def test_04_logout(self):
        """Test 4: Le logout fonctionne"""
        login_page = LoginPage(self.driver)
        login_page.click_logout()
        time.sleep(1)
        self.assertTrue(login_page.is_login_page(), "La page de login n'est pas affichée après logout")
    
    def test_05_dropdown_present(self):
        """Test 5: La liste déroulante est présente"""
        dropdown_page = DropdownPage(self.driver)
        dropdown_page.open()
        self.assertTrue(dropdown_page.is_dropdown_present(), "La liste déroulante n'est pas présente")
    
    def test_06_select_option_1(self):
        """Test 6: Selection de Option 1"""
        dropdown_page = DropdownPage(self.driver)
        dropdown_page.select_option_by_text("Option 1")
        self.assertTrue(dropdown_page.is_option_selected("Option 1"), "Option 1 n'est pas sélectionnée")
    
    def test_07_select_option_2(self):
        """Test 7: Selection de Option 2"""
        dropdown_page = DropdownPage(self.driver)
        dropdown_page.select_option_by_text("Option 2")
        self.assertTrue(dropdown_page.is_option_selected("Option 2"), "Option 2 n'est pas sélectionnée")
    
    def test_08_add_elements(self):
        """Test 8: Ajouter des éléments"""
        add_remove_page = AddRemovePage(self.driver)
        add_remove_page.open()
        add_remove_page.add_elements(3)
        time.sleep(1)
        self.assertTrue(add_remove_page.are_delete_buttons_visible(3), "3 boutons Delete ne sont pas présents")
    
    def test_09_delete_one_element(self):
        """Test 9: Supprimer un élément"""
        add_remove_page = AddRemovePage(self.driver)
        add_remove_page.delete_first_element()
        time.sleep(0.5)
        self.assertTrue(add_remove_page.are_delete_buttons_visible(2), "Il n'y a pas 2 boutons Delete")
    
    def test_10_delete_all_elements(self):
        """Test 10: Supprimer tous les éléments"""
        add_remove_page = AddRemovePage(self.driver)
        add_remove_page.delete_all_elements()
        time.sleep(0.5)
        self.assertTrue(add_remove_page.are_all_elements_deleted(), "Il reste des boutons Delete")


if __name__ == "__main__":
    unittest.main()
