# BulkResponseDataBulk


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_ids** | **List[str]** | The list of Transaction ids that were created. | 
**duplicate_import_ids** | **List[str]** | If any Transactions were not created because they had an &#x60;import_id&#x60; matching a transaction already on the same account, the specified import_id(s) will be included in this list. | 

## Example

```python
from ynab.models.bulk_response_data_bulk import BulkResponseDataBulk

# TODO update the JSON string below
json = "{}"
# create an instance of BulkResponseDataBulk from a JSON string
bulk_response_data_bulk_instance = BulkResponseDataBulk.from_json(json)
# print the JSON string representation of the object
print(BulkResponseDataBulk.to_json())

# convert the object into a dict
bulk_response_data_bulk_dict = bulk_response_data_bulk_instance.to_dict()
# create an instance of BulkResponseDataBulk from a dict
bulk_response_data_bulk_from_dict = BulkResponseDataBulk.from_dict(bulk_response_data_bulk_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


