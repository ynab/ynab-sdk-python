# BudgetSummaryResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**budgets** | [**List[BudgetSummary]**](BudgetSummary.md) |  | 
**default_budget** | [**BudgetSummary**](BudgetSummary.md) |  | [optional] 

## Example

```python
from ynab.models.budget_summary_response_data import BudgetSummaryResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of BudgetSummaryResponseData from a JSON string
budget_summary_response_data_instance = BudgetSummaryResponseData.from_json(json)
# print the JSON string representation of the object
print(BudgetSummaryResponseData.to_json())

# convert the object into a dict
budget_summary_response_data_dict = budget_summary_response_data_instance.to_dict()
# create an instance of BudgetSummaryResponseData from a dict
budget_summary_response_data_from_dict = BudgetSummaryResponseData.from_dict(budget_summary_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


