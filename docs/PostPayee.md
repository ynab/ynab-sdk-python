# PostPayee


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the payee. | 

## Example

```python
from ynab.models.post_payee import PostPayee

# TODO update the JSON string below
json = "{}"
# create an instance of PostPayee from a JSON string
post_payee_instance = PostPayee.from_json(json)
# print the JSON string representation of the object
print(PostPayee.to_json())

# convert the object into a dict
post_payee_dict = post_payee_instance.to_dict()
# create an instance of PostPayee from a dict
post_payee_from_dict = PostPayee.from_dict(post_payee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


