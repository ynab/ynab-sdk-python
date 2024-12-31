# PutTransactionWrapper


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction** | [**ExistingTransaction**](ExistingTransaction.md) |  | 

## Example

```python
from ynab.models.put_transaction_wrapper import PutTransactionWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of PutTransactionWrapper from a JSON string
put_transaction_wrapper_instance = PutTransactionWrapper.from_json(json)
# print the JSON string representation of the object
print(PutTransactionWrapper.to_json())

# convert the object into a dict
put_transaction_wrapper_dict = put_transaction_wrapper_instance.to_dict()
# create an instance of PutTransactionWrapper from a dict
put_transaction_wrapper_from_dict = PutTransactionWrapper.from_dict(put_transaction_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


