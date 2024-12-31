# PostScheduledTransactionWrapper


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scheduled_transaction** | [**SaveScheduledTransaction**](SaveScheduledTransaction.md) |  | 

## Example

```python
from ynab.models.post_scheduled_transaction_wrapper import PostScheduledTransactionWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of PostScheduledTransactionWrapper from a JSON string
post_scheduled_transaction_wrapper_instance = PostScheduledTransactionWrapper.from_json(json)
# print the JSON string representation of the object
print(PostScheduledTransactionWrapper.to_json())

# convert the object into a dict
post_scheduled_transaction_wrapper_dict = post_scheduled_transaction_wrapper_instance.to_dict()
# create an instance of PostScheduledTransactionWrapper from a dict
post_scheduled_transaction_wrapper_from_dict = PostScheduledTransactionWrapper.from_dict(post_scheduled_transaction_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


