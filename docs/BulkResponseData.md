# BulkResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bulk** | [**BulkResponseDataBulk**](BulkResponseDataBulk.md) |  | 

## Example

```python
from ynab.models.bulk_response_data import BulkResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of BulkResponseData from a JSON string
bulk_response_data_instance = BulkResponseData.from_json(json)
# print the JSON string representation of the object
print(BulkResponseData.to_json())

# convert the object into a dict
bulk_response_data_dict = bulk_response_data_instance.to_dict()
# create an instance of BulkResponseData from a dict
bulk_response_data_from_dict = BulkResponseData.from_dict(bulk_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


