# PlanSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**name** | **str** |  | 
**last_modified_on** | **datetime** | The last time any changes were made to the plan from either a web or mobile client | [optional] 
**first_month** | **date** | The earliest plan month | [optional] 
**last_month** | **date** | The latest plan month | [optional] 
**date_format** | [**DateFormat**](DateFormat.md) |  | [optional] 
**currency_format** | [**CurrencyFormat**](CurrencyFormat.md) |  | [optional] 
**accounts** | [**List[Account]**](Account.md) | The plan accounts (only included if &#x60;include_accounts&#x3D;true&#x60; specified as query parameter) | [optional] 

## Example

```python
from ynab.models.plan_summary import PlanSummary

# TODO update the JSON string below
json = "{}"
# create an instance of PlanSummary from a JSON string
plan_summary_instance = PlanSummary.from_json(json)
# print the JSON string representation of the object
print(PlanSummary.to_json())

# convert the object into a dict
plan_summary_dict = plan_summary_instance.to_dict()
# create an instance of PlanSummary from a dict
plan_summary_from_dict = PlanSummary.from_dict(plan_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


