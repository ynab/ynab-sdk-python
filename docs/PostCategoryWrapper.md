# PostCategoryWrapper


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | [**NewCategory**](NewCategory.md) |  | 

## Example

```python
from ynab.models.post_category_wrapper import PostCategoryWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of PostCategoryWrapper from a JSON string
post_category_wrapper_instance = PostCategoryWrapper.from_json(json)
# print the JSON string representation of the object
print(PostCategoryWrapper.to_json())

# convert the object into a dict
post_category_wrapper_dict = post_category_wrapper_instance.to_dict()
# create an instance of PostCategoryWrapper from a dict
post_category_wrapper_from_dict = PostCategoryWrapper.from_dict(post_category_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


