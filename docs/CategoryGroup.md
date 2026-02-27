# CategoryGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**name** | **str** |  | 
**hidden** | **bool** | Whether or not the category group is hidden | 
**deleted** | **bool** | Whether or not the category group has been deleted.  Deleted category groups will only be included in delta requests. | 

## Example

```python
from ynab.models.category_group import CategoryGroup

# TODO update the JSON string below
json = "{}"
# create an instance of CategoryGroup from a JSON string
category_group_instance = CategoryGroup.from_json(json)
# print the JSON string representation of the object
print(CategoryGroup.to_json())

# convert the object into a dict
category_group_dict = category_group_instance.to_dict()
# create an instance of CategoryGroup from a dict
category_group_from_dict = CategoryGroup.from_dict(category_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


