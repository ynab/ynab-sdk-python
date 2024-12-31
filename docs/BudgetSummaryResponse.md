# BudgetSummaryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**BudgetSummaryResponseData**](BudgetSummaryResponseData.md) |  | 

## Example

```python
from ynab.models.budget_summary_response import BudgetSummaryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BudgetSummaryResponse from a JSON string
budget_summary_response_instance = BudgetSummaryResponse.from_json(json)
# print the JSON string representation of the object
print(BudgetSummaryResponse.to_json())

# convert the object into a dict
budget_summary_response_dict = budget_summary_response_instance.to_dict()
# create an instance of BudgetSummaryResponse from a dict
budget_summary_response_from_dict = BudgetSummaryResponse.from_dict(budget_summary_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


