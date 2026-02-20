# PlanSummaryResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**budgets** | [**List[PlanSummary]**](PlanSummary.md) |  | 
**default_budget** | [**PlanSummary**](PlanSummary.md) |  | [optional] 

## Example

```python
from ynab.models.plan_summary_response_data import PlanSummaryResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of PlanSummaryResponseData from a JSON string
plan_summary_response_data_instance = PlanSummaryResponseData.from_json(json)
# print the JSON string representation of the object
print(PlanSummaryResponseData.to_json())

# convert the object into a dict
plan_summary_response_data_dict = plan_summary_response_data_instance.to_dict()
# create an instance of PlanSummaryResponseData from a dict
plan_summary_response_data_from_dict = PlanSummaryResponseData.from_dict(plan_summary_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


