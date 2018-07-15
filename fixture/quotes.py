from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By



class QuoteHelper:

    def __init__(self, app):
        self.app = app

    def select_coverage_page(self):
        wd = self.app.wd
        select_coverage = WebDriverWait(wd, 10).until(EC.visibility_of_element_located((By.ID, 'sltDefCovMedium')))
        select_coverage.click()
        wd.find_element_by_id("RequestQuoteBtnDsktp").click()

    def fill_driver_page(self, testdata):
        wd = self.app.wd
        gender = WebDriverWait(wd, 10).until(EC.visibility_of_element_located((By.ID, 'gender_1')))
        gender.click()
        marital_status = Select(wd.find_element_by_id("ddlMaritalStatus"))
        marital_status.select_by_visible_text("Single")
        dob_field = wd.find_element_by_id("txtDOB")
        dob_field.send_keys(testdata.dob)
        age_first_licensed = wd.find_element_by_id("txtAgeFirstLicensed")
        age_first_licensed.click()
        age_first_licensed.clear()
        age_first_licensed.send_keys("18")
        profession = Select(wd.find_element_by_id("ProfessionGroup"))
        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        profession.select_by_visible_text("Engineer- Licensed")
        wd.find_element_by_id("rdoHasBooDriverRecordNo").click()
        wd.find_element_by_id("rdoAdditionalNo").click()
        wd.find_element_by_id("btnAddNext").click()

    def fill_vehicle_information(self):
        wd = self.app.wd
        veh_year = Select(wd.find_element_by_id("ddlVehicleYear"))
        veh_year.select_by_value('2006')
        veh_make = Select(wd.find_element_by_id("ddlVehicleMake"))
        veh_make.select_by_visible_text("HONDA")
        veh_model = Select(wd.find_element_by_id("ddlVehicleModel"))
        veh_model.select_by_visible_text("CIVIC HYBRID")
        wd.find_element_by_id("rdoHasSalvageTitleNo").click()
        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        veh_usage = Select(wd.find_element_by_id("ddlPrimaryUse"))
        veh_usage.select_by_visible_text("Pleasure")
        veh_owned_time = Select(wd.find_element_by_id("ddlOwnedTime"))
        veh_owned_time.select_by_visible_text("Under 3 months")
        wd.find_element_by_id("rdoAdditionalNo").click()
        wd.find_element_by_id("btnAddNext").click()

    def fill_contact_information_page(self, testdata):
        wd = self.app.wd
        first_name_field = WebDriverWait(wd, 10).until(EC.visibility_of_element_located((By.ID, 'txtFirstName')))
        first_name_field.click()
        wd.find_element_by_id("txtFirstName").clear()
        wd.find_element_by_id("txtFirstName").send_keys(testdata.first_name)
        wd.find_element_by_id("txtLastName").click()
        wd.find_element_by_id("txtLastName").clear()
        wd.find_element_by_id("txtLastName").send_keys(testdata.last_name)
        wd.find_element_by_id("txtAddressStreet").click()
        wd.find_element_by_id("txtAddressStreet").clear()
        wd.find_element_by_id("txtAddressStreet").send_keys(testdata.address)
        wd.find_element_by_id("txtAddressZip").click()
        wd.find_element_by_id("txtAddressZip").clear()
        wd.find_element_by_id("txtAddressZip").send_keys(testdata.ca_zip_code)
        phone = Select(wd.find_element_by_id("ddlPhoneType"))
        phone.select_by_visible_text("Mobile")
        WebDriverWait(wd, 10).until(EC.visibility_of_element_located((By.ID, 'txtAddressCity')))
        wd.find_element_by_id("txtPhone").click()
        wd.find_element_by_id("txtPhone").clear()
        wd.find_element_by_id("txtPhone").send_keys(testdata.phone_number)
        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        wd.find_element_by_id("txtEmailAddress").send_keys(testdata.email)
        add_veh_button = wd.find_element_by_xpath("//div[8]/button[2]")
        actions = ActionChains(wd)
        actions.move_to_element(add_veh_button).perform()
        add_veh_button.click()

    def navigate_to_auto_quote_page(self):
        wd = self.app.wd
        auto_quote_link = WebDriverWait(wd, 10).until(EC.visibility_of_element_located((By.ID, 'nav-1')))
        auto_quote_link.click()
        wd.find_element_by_link_text("Auto insurance").click()
        wd.find_element_by_xpath("//div[@id='hero']//a[.='GET A QUOTE']").click()
