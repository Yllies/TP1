from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    """Classe de base pour tous les Page Objects"""
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def navigate_to(self, url):
        """Accéder à une page"""
        self.driver.get(url)

    def find(self, locator):
        """Chercher un élément (avec attente)"""
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_all(self, locator):
        """Chercher tous les éléments"""
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def click(self, locator):
        """Cliquer sur un bouton ou un lien"""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
        return element

    def send_keys(self, locator, value):
        """Taper du texte dans un champ"""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(value)
        return element

    def get_text(self, locator):
        """Récupérer le texte d'un élément"""
        element = self.find(locator)
        return element.text.strip()

    def is_present(self, locator):
        """Vérifier si un élément existe"""
        try:
            self.find(locator)
            return True
        except TimeoutException:
            return False

    def wait_for_visibility(self, locator, timeout=None):
        """Attendre que ça apparaisse à l'écran"""
        wait = self.wait if timeout is None else WebDriverWait(self.driver, timeout)
        return wait.until(EC.visibility_of_element_located(locator))

    def wait_for_invisibility(self, locator, timeout=None):
        """Attendre que ça disparaisse"""
        wait = self.wait if timeout is None else WebDriverWait(self.driver, timeout)
        return wait.until(EC.invisibility_of_element_located(locator))

    def wait_for_clickable(self, locator, timeout=None):
        """Attendre que ce soit cliquable"""
        wait = self.wait if timeout is None else WebDriverWait(self.driver, timeout)
        return wait.until(EC.element_to_be_clickable(locator))

    def scroll_to_bottom(self):
        """Défiler vers le bas"""
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def take_screenshot(self, name):
        """Prendre une capture d'écran"""
        filename = f"screenshot_tp2_{name}.png"
        self.driver.save_screenshot(filename)
        return filename
