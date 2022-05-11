import time

import pytest
from src.helper.helper import Helper
import pandas as pd


class TestPromotion:

    @pytest.mark.home01
    def test_amazone(self):
        self.driver.get("https://www.ebay.com/")
        self.home_page.input_value("search box", "Iphone 11")
        self.home_page.click_on_element("search button")
        self.home_page.click_on_element("menu")
        self.home_page.click_on_element("custom")
        self.home_page.click_on_element("convert")
        self.home_page.click_on_element("submit")


        aa = self.home_page.get_list_elements_value("aa")
        name = self.home_page.get_list_elements_value("product name list")
        price = self.home_page.get_list_elements_value("product price list")
        links = self.home_page.get_list_element_attribute("product link", "href")



        site = []
        price.pop(0)
        # price.pop(0)
        # name.pop(0)
        # links.pop(0)

        # for i in range(len(name)):
        #     site.append("Amazone")

        for i in range(len(aa)):
            value = str(aa[i])
            if value != "":
                print(value)
                print(value.index("$"))
                print(value[i][164:5])

        ebay_temp = {
            "name": name,
            "price": price,
            "site": site,
            "links": links

        }
        # print(len(name))
        # print(len(price))
        # print(aa)
        # print(len(links))


        # amazone = pd.DataFrame(ebay_temp)
        # print(amazone)
        # amazone.to_excel("output.xlsx")




