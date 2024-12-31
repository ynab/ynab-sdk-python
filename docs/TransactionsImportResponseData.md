# TransactionsImportResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_ids** | **List[str]** | The list of transaction ids that were imported. | 

## Example

```python
from ynab.models.transactions_import_response_data import TransactionsImportResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionsImportResponseData from a JSON string
transactions_import_response_data_instance = TransactionsImportResponseData.from_json(json)
# print the JSON string representation of the object
print(TransactionsImportResponseData.to_json())

# convert the object into a dict
transactions_import_response_data_dict = transactions_import_response_data_instance.to_dict()
# create an instance of TransactionsImportResponseData from a dict
transactions_import_response_data_from_dict = TransactionsImportResponseData.from_dict(transactions_import_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


