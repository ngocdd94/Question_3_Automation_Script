from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage


class HomePage(BasePage):

    page_elements = {
        "top-nav franchising": (By.XPATH, "//nav[@class='top-nav']/descendant::a[text()='Franchising']"),
        "top-nav order now": (By.XPATH, "//nav[@class='top-nav']/descendant::a[text()='Order now']"),
        "language english": (By.XPATH, "//div[@class='right-content']/descendant::div[@class='lang-drop']/child::span[text()='English']"),
        "right-content language": (By.CSS_SELECTOR, ".right-content .languages"),

        # ebay
        "search box": (By.XPATH, "//input[@name='_nkw']"),
        "search button": (By.ID, "gh-btn"),
        "product name list": (By.XPATH, "//h3[@class='s-item__title']"),
        "product price list": (By.XPATH, "//span[@class='s-item__price']"),
        "product link": (By.CLASS_NAME, "s-item__link"),
        "menu": (By.CSS_SELECTOR, ".srp-controls__control.srp-view-options "),
        "custom": (By.CSS_SELECTOR, ".fake-menu-button__item.btn.srp-view-options__customize"),
        "convert": (By.XPATH, "//label[contains(text(),'Convert')]//preceding-sibling::span//child::input"),
        "submit": (By.XPATH, "//button[@type='submit'][@class='btn btn--primary']"),
        "aa": (By.CSS_SELECTOR, ".s-item.s-item__pl-on-bottom"),

        #amazone
        "a search box": (By.ID, "twotabsearchtextbox"),
        "a submit": (By.ID, "nav-search-submit-button"),
        "a price": (By.CSS_SELECTOR, ".a-price-whole"),
        "a links": (By.XPATH, "//span[@class='a-price-whole']/ancestor::div[@class='a-section a-spacing-small a-spacing-top-small']/div/h2/a"),
        "a name": (By.XPATH, "//span[@class='a-price-whole']/ancestor::div[@class='a-section a-spacing-small a-spacing-top-small']/div/h2/a/span")

    }

