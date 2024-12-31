# MonthSummariesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**MonthSummariesResponseData**](MonthSummariesResponseData.md) |  | 

## Example

```python
from ynab.models.month_summaries_response import MonthSummariesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MonthSummariesResponse from a JSON string
month_summaries_response_instance = MonthSummariesResponse.from_json(json)
# print the JSON string representation of the object
print(MonthSummariesResponse.to_json())

# convert the object into a dict
month_summaries_response_dict = month_summaries_response_instance.to_dict()
# create an instance of MonthSummariesResponse from a dict
month_summaries_response_from_dict = MonthSummariesResponse.from_dict(month_summaries_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


