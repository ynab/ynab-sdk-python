# PatchMonthCategoryWrapper


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | [**SaveMonthCategory**](SaveMonthCategory.md) |  | 

## Example

```python
from ynab.models.patch_month_category_wrapper import PatchMonthCategoryWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of PatchMonthCategoryWrapper from a JSON string
patch_month_category_wrapper_instance = PatchMonthCategoryWrapper.from_json(json)
# print the JSON string representation of the object
print(PatchMonthCategoryWrapper.to_json())

# convert the object into a dict
patch_month_category_wrapper_dict = patch_month_category_wrapper_instance.to_dict()
# create an instance of PatchMonthCategoryWrapper from a dict
patch_month_category_wrapper_from_dict = PatchMonthCategoryWrapper.from_dict(patch_month_category_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


