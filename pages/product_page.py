from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage): 
    def add_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        link.click()
        basketprice = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        priceproduct = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text
        assert basketprice == priceproduct, 'Prices are different'
        producttitle = self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text
        messageproducttitle = self.browser.find_element(*ProductPageLocators.MESSAGE_PRODUCT_TITLE).text
        assert producttitle == messageproducttitle, 'Titles are different' 

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"   

    def message_should_be_dissapered(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disapered, but should be"

        
