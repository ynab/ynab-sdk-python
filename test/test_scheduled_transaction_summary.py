# coding: utf-8

"""
    YNAB API Endpoints

    Our API uses a REST based design, leverages the JSON data format, and relies upon HTTPS for transport. We respond with meaningful HTTP response codes and if an error occurs, we include error details in the response body.  API Documentation is at https://api.ynab.com

    The version of the OpenAPI document: 1.72.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ynab.models.scheduled_transaction_summary import ScheduledTransactionSummary

class TestScheduledTransactionSummary(unittest.TestCase):
    """ScheduledTransactionSummary unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ScheduledTransactionSummary:
        """Test ScheduledTransactionSummary
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ScheduledTransactionSummary`
        """
        model = ScheduledTransactionSummary()
        if include_optional:
            return ScheduledTransactionSummary(
                id = '',
                date_first = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                date_next = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                frequency = 'never',
                amount = 56,
                memo = '',
                flag_color = 'red',
                flag_name = '',
                account_id = '',
                payee_id = '',
                category_id = '',
                transfer_account_id = '',
                deleted = True
            )
        else:
            return ScheduledTransactionSummary(
                id = '',
                date_first = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                date_next = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                frequency = 'never',
                amount = 56,
                account_id = '',
                deleted = True,
        )
        """

    def testScheduledTransactionSummary(self):
        """Test ScheduledTransactionSummary"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
