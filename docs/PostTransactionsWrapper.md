# PostTransactionsWrapper


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction** | [**NewTransaction**](NewTransaction.md) |  | [optional] 
**transactions** | [**List[NewTransaction]**](NewTransaction.md) |  | [optional] 

## Example

```python
from ynab.models.post_transactions_wrapper import PostTransactionsWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of PostTransactionsWrapper from a JSON string
post_transactions_wrapper_instance = PostTransactionsWrapper.from_json(json)
# print the JSON string representation of the object
print(PostTransactionsWrapper.to_json())

# convert the object into a dict
post_transactions_wrapper_dict = post_transactions_wrapper_instance.to_dict()
# create an instance of PostTransactionsWrapper from a dict
post_transactions_wrapper_from_dict = PostTransactionsWrapper.from_dict(post_transactions_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


