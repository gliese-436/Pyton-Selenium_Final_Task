import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language")
    
@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    options = Options()
#    options.add_argument('headless')
#    options.add_argument('window-size=1920x935')
    options.add_experimental_option('prefs',  {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    print("\nstart chrome browser for test..")
    yield browser
#    time.sleep(100)
    print("\nquit browser..")
    browser.quit()
