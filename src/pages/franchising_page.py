from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage


class FranchisingPage(BasePage):

    page_elements = {
        "contact email": (By.XPATH, "//div[@class='register-shop']/descendant::input[@name='email']"),
        "contact submit": (By.XPATH, "//div[@class='register-shop']/descendant::button[@type='submit']")

    }

