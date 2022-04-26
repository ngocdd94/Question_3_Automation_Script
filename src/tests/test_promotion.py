import pytest
from src.helper.helper import Helper


class TestPromotion:

    @pytest.mark.tc02
    def test_product_price_sorted_by_descending_order(self):
        # [Order Now] Verify that the product prices are sorted by descending order.
        if self.home_page.get_element_text("right-content language") == "English":
            pass
        else:
            self.home_page.click_on_element("right-content language")
            self.home_page.click_on_element("language english")

        # 1. Click on Order Now menu.
        self.home_page.click_on_element("top-nav order now")
        # 2. Select “Price from high to low” option in Sort by drop down box
        self.promotion_page.select_dropdown_by_visible_text("sort by", "Price from high to low")
        # 3. Observe the price of all products

        # Expected Results
        list_price = []
        # remove special characters
        for i in self.promotion_page.get_list_elements_value("field prince"):
            list_price.append(i.replace("₫", ""))
        # 3. Product prices are sorted by the descending order.
        assert Helper.is_ascending(list_price)

