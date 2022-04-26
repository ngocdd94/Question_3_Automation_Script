import platform
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


class BasePage(object):

    def __init__(self, **kwargs):
        self.driver = kwargs["driver"]
        self.webdriverwait = kwargs["webdriverwait"]
        self.platform = platform.system()

    def click_on_element(self, element):
        el = self.check_element_clickable(element)
        el.click()

    def select_dropdown_by_visible_text(self, element, value):
        select = Select(self.check_element_clickable(element))
        select.select_by_visible_text(value)

    def input_value(self, element, value):
        # clear text box before input value
        element = self.driver.find_element(*self.page_elements[element])
        if self.platform == "Darwin":  # Darwin mean Mac OS
            # perform ctrl = a before input text for Mac
            element.send_keys(Keys.COMMAND, 'a')
        else:
            # perform ctrl = a before input text for Windows
            element.send_keys(Keys.CONTROL, 'a')
        # input text
        element.send_keys(value)

    def get_element_text(self, element):
        ele = self.check_visibility_of_element(element)
        return ele.text

    def get_attribute(self, element, attribute):
        attr = self.check_visibility_of_element(element)
        return attr.get_attribute(attribute)

    def check_element_clickable(self, element, time_out=5):
        return self.webdriverwait(self.driver, time_out).until(
            EC.element_to_be_clickable((self.page_elements[element])))

    def check_visibility_of_element(self, element, time_out=5):
        return self.webdriverwait(self.driver, time_out).until(
            EC.visibility_of_element_located((self.page_elements[element])))

    def get_number_of_elements(self, element):
        # use find elements to get all elements have same locator in DOM
        total_elements = self.driver.find_elements(*self.page_elements[element])
        return len(total_elements)

    def get_list_elements_value(self, element):
        elements = self.driver.find_elements(*self.page_elements[element])
        data_list = []
        for i in range(len(elements)):
            data_list.append(elements[i].text)
        return data_list
