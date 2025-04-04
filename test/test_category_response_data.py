# coding: utf-8

"""
    YNAB API Endpoints

    Our API uses a REST based design, leverages the JSON data format, and relies upon HTTPS for transport. We respond with meaningful HTTP response codes and if an error occurs, we include error details in the response body.  API Documentation is at https://api.ynab.com

    The version of the OpenAPI document: 1.72.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ynab.models.category_response_data import CategoryResponseData

class TestCategoryResponseData(unittest.TestCase):
    """CategoryResponseData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CategoryResponseData:
        """Test CategoryResponseData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CategoryResponseData`
        """
        model = CategoryResponseData()
        if include_optional:
            return CategoryResponseData(
                category = ynab.models.category.Category(
                    id = '', 
                    category_group_id = '', 
                    category_group_name = '', 
                    name = '', 
                    hidden = True, 
                    original_category_group_id = '', 
                    note = '', 
                    budgeted = 56, 
                    activity = 56, 
                    balance = 56, 
                    goal_type = 'TB', 
                    goal_needs_whole_amount = True, 
                    goal_day = 56, 
                    goal_cadence = 56, 
                    goal_cadence_frequency = 56, 
                    goal_creation_month = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    goal_target = 56, 
                    goal_target_month = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    goal_percentage_complete = 56, 
                    goal_months_to_budget = 56, 
                    goal_under_funded = 56, 
                    goal_overall_funded = 56, 
                    goal_overall_left = 56, 
                    deleted = True, )
            )
        else:
            return CategoryResponseData(
                category = ynab.models.category.Category(
                    id = '', 
                    category_group_id = '', 
                    category_group_name = '', 
                    name = '', 
                    hidden = True, 
                    original_category_group_id = '', 
                    note = '', 
                    budgeted = 56, 
                    activity = 56, 
                    balance = 56, 
                    goal_type = 'TB', 
                    goal_needs_whole_amount = True, 
                    goal_day = 56, 
                    goal_cadence = 56, 
                    goal_cadence_frequency = 56, 
                    goal_creation_month = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    goal_target = 56, 
                    goal_target_month = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    goal_percentage_complete = 56, 
                    goal_months_to_budget = 56, 
                    goal_under_funded = 56, 
                    goal_overall_funded = 56, 
                    goal_overall_left = 56, 
                    deleted = True, ),
        )
        """

    def testCategoryResponseData(self):
        """Test CategoryResponseData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
