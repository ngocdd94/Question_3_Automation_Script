from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage


class HomePage(BasePage):

    page_elements = {
        "top-nav franchising": (By.XPATH, "//nav[@class='top-nav']/descendant::a[text()='Franchising']"),
        "top-nav order now": (By.XPATH, "//nav[@class='top-nav']/descendant::a[text()='Order now']"),
        "language english": (By.XPATH, "//div[@class='right-content']/descendant::div[@class='lang-drop']/child::span[text()='English']"),
        "right-content language": (By.CSS_SELECTOR, ".right-content .languages")

    }

