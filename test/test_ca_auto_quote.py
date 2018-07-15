# -*- coding: utf-8 -*-
from model.parameters import Testdata
import pytest
from fixture.application import Application

@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_test_ca_auto_quote(app):
        app.session.open_home_page(Testdata(ca_zip_code="91764"))
        app.quotes.navigate_to_auto_quote_page()
        app.quotes.fill_contact_information_page(Testdata(email="vizovskiy.andrey@aaa-calif.com", phone_number="11111111111",
                                                        ca_zip_code="91764", address="1230 Main Street", last_name="Testprodquote",
                                                        first_name="Test"))
        app.quotes.fill_vehicle_information()
        app.quotes.fill_driver_page(Testdata(dob="01/01/1977"))

