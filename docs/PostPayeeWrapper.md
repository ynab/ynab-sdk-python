# PostPayeeWrapper


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payee** | [**PostPayee**](PostPayee.md) |  | 

## Example

```python
from ynab.models.post_payee_wrapper import PostPayeeWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of PostPayeeWrapper from a JSON string
post_payee_wrapper_instance = PostPayeeWrapper.from_json(json)
# print the JSON string representation of the object
print(PostPayeeWrapper.to_json())

# convert the object into a dict
post_payee_wrapper_dict = post_payee_wrapper_instance.to_dict()
# create an instance of PostPayeeWrapper from a dict
post_payee_wrapper_from_dict = PostPayeeWrapper.from_dict(post_payee_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


