# BulkTransactions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transactions** | [**List[SaveTransactionWithOptionalFields]**](SaveTransactionWithOptionalFields.md) |  | 

## Example

```python
from ynab.models.bulk_transactions import BulkTransactions

# TODO update the JSON string below
json = "{}"
# create an instance of BulkTransactions from a JSON string
bulk_transactions_instance = BulkTransactions.from_json(json)
# print the JSON string representation of the object
print(BulkTransactions.to_json())

# convert the object into a dict
bulk_transactions_dict = bulk_transactions_instance.to_dict()
# create an instance of BulkTransactions from a dict
bulk_transactions_from_dict = BulkTransactions.from_dict(bulk_transactions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


