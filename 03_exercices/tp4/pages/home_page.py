from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.logger_config import get_logger


class HomePage:
    URL = "https://automationexercise.com/"

    NAV_PRODUCTS = (By.CSS_SELECTOR, "a[href='/products']")

    COOKIE_OVERLAY = (By.CSS_SELECTOR, ".fc-dialog-overlay")
    COOKIE_CONSENT_BTN = (
        By.CSS_SELECTOR,
        ".fc-cta-consent, button.fc-button.fc-cta-consent",
    )

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        self.logger = get_logger(self.__class__.__name__)

    def _dismiss_cookie_banner(self):

        try:
            short_wait = WebDriverWait(self.driver, 5)
            btn = short_wait.until(EC.element_to_be_clickable(self.COOKIE_CONSENT_BTN))
            btn.click()
            short_wait.until(EC.invisibility_of_element_located(self.COOKIE_OVERLAY))
            self.logger.info("Bandeau cookies fermé")
        except Exception:
            self.logger.debug("Aucun bandeau cookies détecté")

    def open(self):
        """Ouvre le site, maximise la fenêtre et ferme le bandeau cookies."""
        self.logger.info(f"Ouverture du site : {self.URL}")
        self.driver.get(self.URL)
        self.driver.maximize_window()
        self.wait.until(EC.visibility_of_element_located(self.NAV_PRODUCTS))
        self.logger.info("Page d'accueil chargée")
        self._dismiss_cookie_banner()

    def go_to_products(self):
        """Clique sur le lien Products dans la navigation."""
        self.logger.info("Navigation vers la page Products")
        self.wait.until(EC.element_to_be_clickable(self.NAV_PRODUCTS)).click()
