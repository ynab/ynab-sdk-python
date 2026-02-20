# PlanSummaryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PlanSummaryResponseData**](PlanSummaryResponseData.md) |  | 

## Example

```python
from ynab.models.plan_summary_response import PlanSummaryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PlanSummaryResponse from a JSON string
plan_summary_response_instance = PlanSummaryResponse.from_json(json)
# print the JSON string representation of the object
print(PlanSummaryResponse.to_json())

# convert the object into a dict
plan_summary_response_dict = plan_summary_response_instance.to_dict()
# create an instance of PlanSummaryResponse from a dict
plan_summary_response_from_dict = PlanSummaryResponse.from_dict(plan_summary_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


