# MonthDetailResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**month** | [**MonthDetail**](MonthDetail.md) |  | 

## Example

```python
from ynab.models.month_detail_response_data import MonthDetailResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of MonthDetailResponseData from a JSON string
month_detail_response_data_instance = MonthDetailResponseData.from_json(json)
# print the JSON string representation of the object
print(MonthDetailResponseData.to_json())

# convert the object into a dict
month_detail_response_data_dict = month_detail_response_data_instance.to_dict()
# create an instance of MonthDetailResponseData from a dict
month_detail_response_data_from_dict = MonthDetailResponseData.from_dict(month_detail_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


