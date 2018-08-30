
Feature: California quotes

  Scenario Outline: Create California auto quote
      Given a user with <first_name>, <phone_number>, <address>, <last_name>, <email>, <ca_zip_code>
      Given the user opens the home page with <ca_zip_code>
      When the user navigates to the CA auto quote page
      When user fills in contact information page
      When user fills in vehicle information page
      When user fills in driver information page
      Then user selects coverage_change on local
      #Then a new quote is created
      
      remote change
      
        
      Examples:

      | ca_zip_code | first_name | phone_number | address          | last_name     | email                          |
      | 91762       | Test       | 11111111111  | 1230 Main Street | Testprodquote | Vizovskiy.Andrey@aaa-calif.com |





      #| ca_zip_code |
      #| 91764       |



    #email="vizovskiy.andrey@aaa-calif.com", phone_number="11111111111",
                                                        #ca_zip_code="91764", address="1230 Main Street", last_name="Testprodquote",
                                                        #first_name="Test"
