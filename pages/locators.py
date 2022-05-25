from selenium.webdriver.common.by import By


#class MainPageLocators():
#    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET_LINK = (By.CSS_SELECTOR, "[class='basket-mini pull-right hidden-xs']>span>a")
    BASKET_EMPTY_TEXT = (By.CSS_SELECTOR, "#content_inner>p")
    BASKET_ITEMS = (By.CSS_SELECTOR, "[class='basket-items']")
    

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    FIELD_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    FIELD_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    FIELD_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")  

class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, "[class='btn btn-lg btn-primary btn-add-to-basket']")
    BASKET_PRICE = (By.CSS_SELECTOR, "[class='alertinner ']>p>strong")
    PRICE_PRODUCT = (By.CSS_SELECTOR, "[class='price_color']")
    PRODUCT_TITLE = (By.CSS_SELECTOR, "[class='col-sm-6 product_main'] > h1")
    MESSAGE_PRODUCT_TITLE = (By.CSS_SELECTOR, "#messages>div>div>strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "[class='alert alert-safe alert-noicon alert-success  fade in']")