# PostCategoryGroupWrapper


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category_group** | [**SaveCategoryGroup**](SaveCategoryGroup.md) |  | 

## Example

```python
from ynab.models.post_category_group_wrapper import PostCategoryGroupWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of PostCategoryGroupWrapper from a JSON string
post_category_group_wrapper_instance = PostCategoryGroupWrapper.from_json(json)
# print the JSON string representation of the object
print(PostCategoryGroupWrapper.to_json())

# convert the object into a dict
post_category_group_wrapper_dict = post_category_group_wrapper_instance.to_dict()
# create an instance of PostCategoryGroupWrapper from a dict
post_category_group_wrapper_from_dict = PostCategoryGroupWrapper.from_dict(post_category_group_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


