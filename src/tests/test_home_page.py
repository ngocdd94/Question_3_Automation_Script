import time

import pytest
from src.helper.helper import Helper
import pandas as pd
import re


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


        get_text = self.home_page.get_list_elements_value("aa")
        e_links = self.home_page.get_list_element_attribute("product link", "href")

        e_links.pop(0)
        e_name = []
        e_price = []
        e_site = []

        for i in range(len(get_text)):
            value = str(get_text[i])
            if value != "":
                e_site.append("Ebay")
                idx = value.index("\n")
                e_name.append(value[0:idx])
                index = value.index("$")
                n_temp1 = value[index+1:index+7]
                n_temp2 = re.sub("[$a-zA-Z]", "", n_temp1)
                e_price.append(n_temp2)

        ebay_temp = {
            "name": e_name,
            "price": e_price,
            "site": e_site,
            "links": e_links

        }

        ebay = pd.DataFrame(ebay_temp)


        self.driver.get("https://www.amazon.com/")
        self.home_page.input_value("a search box", "Iphone 11")
        self.home_page.click_on_element("a submit")

        a_name = self.home_page.get_list_elements_value("a name")
        a_price = self.home_page.get_list_elements_value("a price")
        a_links = self.home_page.get_list_element_attribute("a links", "href")
        a_site = []

        for i in range(len(a_name)):
            a_price[i] = str(a_price[i]).replace(",", "")
            a_site.append("Amazon")

        amzon_temp = {
            "name": a_name,
            "price": a_price,
            "site": a_site,
            "links": a_links
        }

        amazon = pd.DataFrame(amzon_temp)
        a_frame = [ebay, amazon]
        all_d = pd.concat(a_frame)
        all_d["price"] = pd.to_numeric(all_d["price"])
        all_d.sort_values(by="price", ascending=True, inplace=True)
        all_d.to_excel("result.xlsx")