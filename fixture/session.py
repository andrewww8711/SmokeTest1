from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def open_home_page(self, parameters):
        wd = self.app.wd
        wd.get("https://www.aaa.com/stop/")
        zip_code1 = wd.find_element_by_id("zipCode")
        zip_code1.clear()
        zip_code1.send_keys(parameters.ca_zip_code)
        wd.find_element_by_id("goButton").click()
        zip_code2 = wd.find_element_by_name("zip-code")
        zip_code2.clear()
        zip_code2.send_keys(parameters.ca_zip_code)
        go_button = WebDriverWait(wd, 10).until(EC.visibility_of_element_located((By.XPATH, 'html/body/div[3]/div[2]/div/div/a')))
        go_button.click()


    #Login and Logout will be here
    pass
