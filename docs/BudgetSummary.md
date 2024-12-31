# BudgetSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**last_modified_on** | **datetime** | The last time any changes were made to the budget from either a web or mobile client | [optional] 
**first_month** | **date** | The earliest budget month | [optional] 
**last_month** | **date** | The latest budget month | [optional] 
**date_format** | [**DateFormat**](DateFormat.md) |  | [optional] 
**currency_format** | [**CurrencyFormat**](CurrencyFormat.md) |  | [optional] 
**accounts** | [**List[Account]**](Account.md) | The budget accounts (only included if &#x60;include_accounts&#x3D;true&#x60; specified as query parameter) | [optional] 

## Example

```python
from ynab.models.budget_summary import BudgetSummary

# TODO update the JSON string below
json = "{}"
# create an instance of BudgetSummary from a JSON string
budget_summary_instance = BudgetSummary.from_json(json)
# print the JSON string representation of the object
print(BudgetSummary.to_json())

# convert the object into a dict
budget_summary_dict = budget_summary_instance.to_dict()
# create an instance of BudgetSummary from a dict
budget_summary_from_dict = BudgetSummary.from_dict(budget_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


