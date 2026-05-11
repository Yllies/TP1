"""
Page Object pour la page Notification Message
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class NotificationPage(BasePage):
    BASE_URL = "https://the-internet.herokuapp.com/notification_message"
    MESSAGE_BOX = (By.ID, "flash")
    CLICK_HERE_LINK = (By.LINK_TEXT, "Click here")

    EXPECTED_MESSAGES = [
        "Action successful",
        "Action unsuccessful, please try again",
        "Action unsuccessful",
        "Action unsuccesful, please try again"
    ]

    def open(self):
        """Aller sur la page"""
        self.navigate_to(self.BASE_URL)

    def get_message(self):
        """Récupérer le message"""
        message = self.get_text(self.MESSAGE_BOX)
        return message.replace("\n×", "").strip()

    def click_refresh(self):
        """Cliquer sur 'Click here' pour une nouvelle notification"""
        self.click(self.CLICK_HERE_LINK)

    def is_message_expected(self, message):
        """C'est un message valide?"""
        return any(expected in message for expected in self.EXPECTED_MESSAGES)

    def wait_for_message(self):
        """Attendre et récupérer le message"""
        self.wait_for_visibility(self.MESSAGE_BOX)
        return self.get_message()
