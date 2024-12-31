# PostAccountWrapper


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | [**SaveAccount**](SaveAccount.md) |  | 

## Example

```python
from ynab.models.post_account_wrapper import PostAccountWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of PostAccountWrapper from a JSON string
post_account_wrapper_instance = PostAccountWrapper.from_json(json)
# print the JSON string representation of the object
print(PostAccountWrapper.to_json())

# convert the object into a dict
post_account_wrapper_dict = post_account_wrapper_instance.to_dict()
# create an instance of PostAccountWrapper from a dict
post_account_wrapper_from_dict = PostAccountWrapper.from_dict(post_account_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


