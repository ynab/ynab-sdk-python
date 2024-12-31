# coding: utf-8

"""
    YNAB API Endpoints

    Our API uses a REST based design, leverages the JSON data format, and relies upon HTTPS for transport. We respond with meaningful HTTP response codes and if an error occurs, we include error details in the response body.  API Documentation is at https://api.ynab.com

    The version of the OpenAPI document: 1.72.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ynab.api.payee_locations_api import PayeeLocationsApi


class TestPayeeLocationsApi(unittest.TestCase):
    """PayeeLocationsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = PayeeLocationsApi()

    def tearDown(self) -> None:
        pass

    def test_get_payee_location_by_id(self) -> None:
        """Test case for get_payee_location_by_id

        Single payee location
        """
        pass

    def test_get_payee_locations(self) -> None:
        """Test case for get_payee_locations

        List payee locations
        """
        pass

    def test_get_payee_locations_by_payee(self) -> None:
        """Test case for get_payee_locations_by_payee

        List locations for a payee
        """
        pass


if __name__ == '__main__':
    unittest.main()