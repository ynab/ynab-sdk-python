# MonthDetailResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**MonthDetailResponseData**](MonthDetailResponseData.md) |  | 

## Example

```python
from ynab.models.month_detail_response import MonthDetailResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MonthDetailResponse from a JSON string
month_detail_response_instance = MonthDetailResponse.from_json(json)
# print the JSON string representation of the object
print(MonthDetailResponse.to_json())

# convert the object into a dict
month_detail_response_dict = month_detail_response_instance.to_dict()
# create an instance of MonthDetailResponse from a dict
month_detail_response_from_dict = MonthDetailResponse.from_dict(month_detail_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


