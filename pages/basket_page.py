from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def go_to_basket(self):
        link = self.browser.find_element(*BasketPageLocators.BASKET_LINK)
        link.click()
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "There are items in the basket"
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_TEXT), "Text:'basket is empty' is not presented"
