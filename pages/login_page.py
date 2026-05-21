from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    USER = (By.ID, "user-name")
    PASS = (By.ID, "password")
    SUBMIT = (By.ID, "login-button")
    
    def login(self, user, pwd):
        self.type(self.USER, user)
        self.type(self.PASS, pwd)
        self.click(self.SUBMIT)
    