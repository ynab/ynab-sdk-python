# PatchCategoryGroupWrapper


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category_group** | [**SaveCategoryGroup**](SaveCategoryGroup.md) |  | 

## Example

```python
from ynab.models.patch_category_group_wrapper import PatchCategoryGroupWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of PatchCategoryGroupWrapper from a JSON string
patch_category_group_wrapper_instance = PatchCategoryGroupWrapper.from_json(json)
# print the JSON string representation of the object
print(PatchCategoryGroupWrapper.to_json())

# convert the object into a dict
patch_category_group_wrapper_dict = patch_category_group_wrapper_instance.to_dict()
# create an instance of PatchCategoryGroupWrapper from a dict
patch_category_group_wrapper_from_dict = PatchCategoryGroupWrapper.from_dict(patch_category_group_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


