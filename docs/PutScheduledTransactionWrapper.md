# PutScheduledTransactionWrapper


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scheduled_transaction** | [**SaveScheduledTransaction**](SaveScheduledTransaction.md) |  | 

## Example

```python
from ynab.models.put_scheduled_transaction_wrapper import PutScheduledTransactionWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of PutScheduledTransactionWrapper from a JSON string
put_scheduled_transaction_wrapper_instance = PutScheduledTransactionWrapper.from_json(json)
# print the JSON string representation of the object
print(PutScheduledTransactionWrapper.to_json())

# convert the object into a dict
put_scheduled_transaction_wrapper_dict = put_scheduled_transaction_wrapper_instance.to_dict()
# create an instance of PutScheduledTransactionWrapper from a dict
put_scheduled_transaction_wrapper_from_dict = PutScheduledTransactionWrapper.from_dict(put_scheduled_transaction_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


