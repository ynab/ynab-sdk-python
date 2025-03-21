# coding: utf-8

"""
    YNAB API Endpoints

    Our API uses a REST based design, leverages the JSON data format, and relies upon HTTPS for transport. We respond with meaningful HTTP response codes and if an error occurs, we include error details in the response body.  API Documentation is at https://api.ynab.com

    The version of the OpenAPI document: 1.72.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ynab.models.budget_detail_response import BudgetDetailResponse

class TestBudgetDetailResponse(unittest.TestCase):
    """BudgetDetailResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BudgetDetailResponse:
        """Test BudgetDetailResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BudgetDetailResponse`
        """
        model = BudgetDetailResponse()
        if include_optional:
            return BudgetDetailResponse(
                data = ynab.models.budget_detail_response_data.BudgetDetailResponse_data(
                    budget = null, 
                    server_knowledge = 56, )
            )
        else:
            return BudgetDetailResponse(
                data = ynab.models.budget_detail_response_data.BudgetDetailResponse_data(
                    budget = null, 
                    server_knowledge = 56, ),
        )
        """

    def testBudgetDetailResponse(self):
        """Test BudgetDetailResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
