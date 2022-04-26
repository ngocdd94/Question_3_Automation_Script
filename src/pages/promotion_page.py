from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage


class PromotionPage(BasePage):

    page_elements = {
        "sort by": (By.CSS_SELECTOR, ".f-sort .form-control"),
        "product list": (By.CLASS_NAME, "product-list"),
        "field prince": (By.CLASS_NAME, "field-price")

    }

