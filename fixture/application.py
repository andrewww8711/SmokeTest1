from selenium import webdriver
from fixture.session import SessionHelper
from fixture.quotes import QuoteHelper


class Application:

    def __init__(self):
        self.wd = webdriver.Firefox(capabilities={"marionette": False})
        # self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(60)
        self.wd.maximize_window()
        self.session = SessionHelper(self)
        self.quotes = QuoteHelper(self)


    def destroy(self):
        self.wd.quit()