"""
Base Page Object - classe parente pour toutes les pages
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class BasePage:
    """Classe de base pour tous les Page Objects"""
    
    def __init__(self, driver):
        """
        Initialiser la page avec le driver Selenium
        
        Args:
            driver: instance WebDriver Selenium
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def find_element(self, locator):
        """
        Trouver un élément avec attente implicite
        
        Args:
            locator: tuple (By.ID, "id") ou (By.XPATH, "//xpath")
        
        Returns:
            WebElement ou None si non trouvé
        """
        try:
            return self.wait.until(EC.presence_of_element_located(locator))
        except TimeoutException:
            return None
    
    def find_elements(self, locator):
        """
        Trouver plusieurs éléments
        
        Args:
            locator: tuple (By.ID, "id") ou (By.XPATH, "//xpath")
        
        Returns:
            liste d'éléments
        """
        try:
            self.wait.until(EC.presence_of_all_elements_located(locator))
            return self.driver.find_elements(locator[0], locator[1])
        except TimeoutException:
            return []
    
    def click_element(self, locator):
        """
        Cliquer sur un élément
        
        Args:
            locator: tuple (By.ID, "id") ou (By.XPATH, "//xpath")
        """
        element = self.find_element(locator)
        if element:
            element.click()
    
    def send_keys(self, locator, text):
        """
        Saisir du texte dans un champ
        
        Args:
            locator: tuple (By.ID, "id") ou (By.XPATH, "//xpath")
            text: texte à saisir
        """
        element = self.find_element(locator)
        if element:
            element.clear()
            element.send_keys(text)
    
    def get_text(self, locator):
        """
        Récupérer le texte d'un élément
        
        Args:
            locator: tuple (By.ID, "id") ou (By.XPATH, "//xpath")
        
        Returns:
            texte de l'élément ou chaîne vide
        """
        element = self.find_element(locator)
        return element.text if element else ""
    
    def element_exists(self, locator):
        """
        Vérifier si un élément existe
        
        Args:
            locator: tuple (By.ID, "id") ou (By.XPATH, "//xpath")
        
        Returns:
            True si l'élément existe, False sinon
        """
        element = self.find_element(locator)
        return element is not None
    
    def navigate_to(self, url):
        """
        Naviguer vers une URL
        
        Args:
            url: URL à ouvrir
        """
        self.driver.get(url)
    
    def get_current_url(self):
        """
        Récupérer l'URL courante
        
        Returns:
            URL actuelle
        """
        return self.driver.current_url
    
    def get_title(self):
        """
        Récupérer le titre de la page
        
        Returns:
            Titre de la page
        """
        return self.driver.title
    
    def wait_for_element(self, locator, timeout=10):
        """
        Attendre qu'un élément soit visible
        
        Args:
            locator: tuple (By.ID, "id") ou (By.XPATH, "//xpath")
            timeout: temps d'attente en secondes
        
        Returns:
            l'élément si trouvé, None sinon
        """
        try:
            wait = WebDriverWait(self.driver, timeout)
            return wait.until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            return None
