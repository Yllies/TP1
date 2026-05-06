from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait,Select
from selenium.webdriver.support import expected_conditions as EC

class DropdowPage:
    URL = "https://the-internet.herokuapp.com/dropdown"
    DROPDOWN = (By.ID,"dropdown")

    def __init__(self,driver,timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver,timeout)

    def open(self):
        self.driver.get(self.URL)

    def select_option_by_text(self,text):
        element = self.wait.until(EC.visibility_of_element_located(self.DROPDOWN))
        Select(element).select_by_visible_text(text)

    def get_selected_option_text(self):
        element = self.wait.until(EC.visibility_of_element_located(self.DROPDOWN))
        return Select(element).first_selected_option.text

    