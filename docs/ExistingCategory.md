# ExistingCategory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**note** | **str** |  | [optional] 
**category_group_id** | **UUID** |  | [optional] 
**goal_target** | **int** | The goal target amount in milliunits format.  If value is specified and goal has not already been configured for category, a monthly &#39;Needed for Spending&#39; goal will be created for the category with this target amount. | [optional] 
**goal_target_date** | **date** | The goal target date in ISO format (e.g. 2016-12-01). | [optional] 

## Example

```python
from ynab.models.existing_category import ExistingCategory

# TODO update the JSON string below
json = "{}"
# create an instance of ExistingCategory from a JSON string
existing_category_instance = ExistingCategory.from_json(json)
# print the JSON string representation of the object
print(ExistingCategory.to_json())

# convert the object into a dict
existing_category_dict = existing_category_instance.to_dict()
# create an instance of ExistingCategory from a dict
existing_category_from_dict = ExistingCategory.from_dict(existing_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


