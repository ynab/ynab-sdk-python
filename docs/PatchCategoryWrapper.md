# PatchCategoryWrapper


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | [**ExistingCategory**](ExistingCategory.md) |  | 

## Example

```python
from ynab.models.patch_category_wrapper import PatchCategoryWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of PatchCategoryWrapper from a JSON string
patch_category_wrapper_instance = PatchCategoryWrapper.from_json(json)
# print the JSON string representation of the object
print(PatchCategoryWrapper.to_json())

# convert the object into a dict
patch_category_wrapper_dict = patch_category_wrapper_instance.to_dict()
# create an instance of PatchCategoryWrapper from a dict
patch_category_wrapper_from_dict = PatchCategoryWrapper.from_dict(patch_category_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


