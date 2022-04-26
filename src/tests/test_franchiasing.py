import pytest


class TestFranchising:

    @pytest.mark.tc01
    def test_validate_email(self):
        # [Franchising] Verify that error message is displayed correctly when inputs invalid email.
        if self.home_page.get_element_text("right-content language") == "English":
            pass
        else:
            self.home_page.click_on_element("right-content language")
            self.home_page.click_on_element("language english")

        # 1. Click on Franchising menu.
        self.home_page.click_on_element("top-nav franchising")
        # 2. Input invalid email. E.g: “abc”
        input_email = "abc"
        self.franchising_page.input_value("contact email", input_email)
        # 3. Click on “Send” button.
        self.franchising_page.click_on_element("contact submit")
        # get html5 validation message
        validate_message = self.franchising_page.get_attribute("contact email", "validationMessage")

        # expected results
        # 1. Open Franchising page
        assert self.driver.current_url == "https://www.lotteria.vn/lotteria-franchise"
        # 2. Data is populate in Email field.
        assert self.franchising_page.get_attribute("contact email", "value") == input_email
        # 3. An error message is displayed “Please include an “@” in the email address. ‘abc’ is missing an ‘@’."
        assert "Please include an '@' in the email address. 'abc' is missing an '@'." in validate_message
