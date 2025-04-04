# coding: utf-8

"""
    YNAB API Endpoints

    Our API uses a REST based design, leverages the JSON data format, and relies upon HTTPS for transport. We respond with meaningful HTTP response codes and if an error occurs, we include error details in the response body.  API Documentation is at https://api.ynab.com

    The version of the OpenAPI document: 1.72.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ynab.models.budget_settings_response import BudgetSettingsResponse

class TestBudgetSettingsResponse(unittest.TestCase):
    """BudgetSettingsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BudgetSettingsResponse:
        """Test BudgetSettingsResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BudgetSettingsResponse`
        """
        model = BudgetSettingsResponse()
        if include_optional:
            return BudgetSettingsResponse(
                data = ynab.models.budget_settings_response_data.BudgetSettingsResponse_data(
                    settings = ynab.models.budget_settings.BudgetSettings(
                        date_format = ynab.models.date_format.DateFormat(
                            format = '', ), 
                        currency_format = ynab.models.currency_format.CurrencyFormat(
                            iso_code = '', 
                            example_format = '', 
                            decimal_digits = 56, 
                            decimal_separator = '', 
                            symbol_first = True, 
                            group_separator = '', 
                            currency_symbol = '', 
                            display_symbol = True, ), ), )
            )
        else:
            return BudgetSettingsResponse(
                data = ynab.models.budget_settings_response_data.BudgetSettingsResponse_data(
                    settings = ynab.models.budget_settings.BudgetSettings(
                        date_format = ynab.models.date_format.DateFormat(
                            format = '', ), 
                        currency_format = ynab.models.currency_format.CurrencyFormat(
                            iso_code = '', 
                            example_format = '', 
                            decimal_digits = 56, 
                            decimal_separator = '', 
                            symbol_first = True, 
                            group_separator = '', 
                            currency_symbol = '', 
                            display_symbol = True, ), ), ),
        )
        """

    def testBudgetSettingsResponse(self):
        """Test BudgetSettingsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
