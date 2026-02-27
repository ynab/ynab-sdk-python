# SaveCategory


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
from ynab.models.save_category import SaveCategory

# TODO update the JSON string below
json = "{}"
# create an instance of SaveCategory from a JSON string
save_category_instance = SaveCategory.from_json(json)
# print the JSON string representation of the object
print(SaveCategory.to_json())

# convert the object into a dict
save_category_dict = save_category_instance.to_dict()
# create an instance of SaveCategory from a dict
save_category_from_dict = SaveCategory.from_dict(save_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


