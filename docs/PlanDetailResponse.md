# PlanDetailResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PlanDetailResponseData**](PlanDetailResponseData.md) |  | 

## Example

```python
from ynab.models.plan_detail_response import PlanDetailResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PlanDetailResponse from a JSON string
plan_detail_response_instance = PlanDetailResponse.from_json(json)
# print the JSON string representation of the object
print(PlanDetailResponse.to_json())

# convert the object into a dict
plan_detail_response_dict = plan_detail_response_instance.to_dict()
# create an instance of PlanDetailResponse from a dict
plan_detail_response_from_dict = PlanDetailResponse.from_dict(plan_detail_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


