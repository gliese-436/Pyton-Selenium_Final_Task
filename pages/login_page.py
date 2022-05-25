from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        login_url = self.browser.current_url
        assert 'login' in login_url, "Login URL is incorrect"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        input_email = self.browser.find_element(*LoginPageLocators.FIELD_EMAIL) 
        input_email.send_keys(email)
        input_password = self.browser.find_element(*LoginPageLocators.FIELD_PASSWORD) 
        input_password.send_keys(password)
        input_password_again = self.browser.find_element(*LoginPageLocators.FIELD_PASSWORD2) 
        input_password_again.send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON) 
        register_button.click()


