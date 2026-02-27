# SaveCategoryGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the category group. The name must be a maximum of 50 characters. | 

## Example

```python
from ynab.models.save_category_group import SaveCategoryGroup

# TODO update the JSON string below
json = "{}"
# create an instance of SaveCategoryGroup from a JSON string
save_category_group_instance = SaveCategoryGroup.from_json(json)
# print the JSON string representation of the object
print(SaveCategoryGroup.to_json())

# convert the object into a dict
save_category_group_dict = save_category_group_instance.to_dict()
# create an instance of SaveCategoryGroup from a dict
save_category_group_from_dict = SaveCategoryGroup.from_dict(save_category_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


