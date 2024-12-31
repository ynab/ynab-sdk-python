# TransactionsImportResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**TransactionsImportResponseData**](TransactionsImportResponseData.md) |  | 

## Example

```python
from ynab.models.transactions_import_response import TransactionsImportResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionsImportResponse from a JSON string
transactions_import_response_instance = TransactionsImportResponse.from_json(json)
# print the JSON string representation of the object
print(TransactionsImportResponse.to_json())

# convert the object into a dict
transactions_import_response_dict = transactions_import_response_instance.to_dict()
# create an instance of TransactionsImportResponse from a dict
transactions_import_response_from_dict = TransactionsImportResponse.from_dict(transactions_import_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


