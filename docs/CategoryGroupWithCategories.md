# CategoryGroupWithCategories


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**name** | **str** |  | 
**hidden** | **bool** | Whether or not the category group is hidden | 
**deleted** | **bool** | Whether or not the category group has been deleted.  Deleted category groups will only be included in delta requests. | 
**categories** | [**List[Category]**](Category.md) | Category group categories.  Amounts (assigned, activity, available, etc.) are specific to the current plan month (UTC). | 

## Example

```python
from ynab.models.category_group_with_categories import CategoryGroupWithCategories

# TODO update the JSON string below
json = "{}"
# create an instance of CategoryGroupWithCategories from a JSON string
category_group_with_categories_instance = CategoryGroupWithCategories.from_json(json)
# print the JSON string representation of the object
print(CategoryGroupWithCategories.to_json())

# convert the object into a dict
category_group_with_categories_dict = category_group_with_categories_instance.to_dict()
# create an instance of CategoryGroupWithCategories from a dict
category_group_with_categories_from_dict = CategoryGroupWithCategories.from_dict(category_group_with_categories_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


