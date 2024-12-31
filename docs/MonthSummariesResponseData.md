# MonthSummariesResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**months** | [**List[MonthSummary]**](MonthSummary.md) |  | 
**server_knowledge** | **int** | The knowledge of the server | 

## Example

```python
from ynab.models.month_summaries_response_data import MonthSummariesResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of MonthSummariesResponseData from a JSON string
month_summaries_response_data_instance = MonthSummariesResponseData.from_json(json)
# print the JSON string representation of the object
print(MonthSummariesResponseData.to_json())

# convert the object into a dict
month_summaries_response_data_dict = month_summaries_response_data_instance.to_dict()
# create an instance of MonthSummariesResponseData from a dict
month_summaries_response_data_from_dict = MonthSummariesResponseData.from_dict(month_summaries_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


