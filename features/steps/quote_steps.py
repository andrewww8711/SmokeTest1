

from pytest_bdd import given, when, then
from model.parameters import Testdata

@given('a user with <first_name>, <phone_number>, <address>, <last_name>, <email>, <ca_zip_code>')
def ca_user(first_name, phone_number, address, last_name, email, ca_zip_code):
    return Testdata(first_name=first_name, phone_number=phone_number, address=address, last_name=last_name, email=email, ca_zip_code=ca_zip_code)

@given('the user opens the home page with <ca_zip_code>')
def open_home_page(app, ca_zip_code):
    app.session.open_home_page(Testdata(ca_zip_code))


@when('the user navigates to the CA auto quote page')
def navigate_to_auto_quote_page(app):
    app.quotes.navigate_to_auto_quote_page()


@when('user fills in contact information page')
def fill_contact_information_page(app, ca_user):
    app.quotes.fill_contact_information_page(ca_user)


@when('user fills in vehicle information page')
def fill_vehicle_information():
    pass


@when('user fills in driver information page')
def fill_driver_page():
    pass


@then('user selects coverage')
def select_coverage_page():
    pass

#@then('a new quote is created')
#def select_coverage_page():
    #pass