# NewCategory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**note** | **str** |  | [optional] 
**category_group_id** | **UUID** |  | [optional] 
**goal_target** | **int** | The goal target amount in milliunits format.  If value is specified and goal has not already been configured for category, a monthly goal will be created for the category with this target amount.  If goal_type is not specified, it will default to &#39;NEED&#39; or &#39;MF&#39; for Credit Card Payment categories. | [optional] 
**goal_target_date** | **date** | The goal target date in ISO format (e.g. 2016-12-01). | [optional] 
**goal_needs_whole_amount** | **bool** | Whether the goal requires the full target amount each period. Only supported for &#39;NEED&#39; goals. When true, the goal is configured as &#39;Set aside another...&#39;. When false, the goal is configured as &#39;Refill up to...&#39;. | [optional] 

## Example

```python
from ynab.models.new_category import NewCategory

# TODO update the JSON string below
json = "{}"
# create an instance of NewCategory from a JSON string
new_category_instance = NewCategory.from_json(json)
# print the JSON string representation of the object
print(NewCategory.to_json())

# convert the object into a dict
new_category_dict = new_category_instance.to_dict()
# create an instance of NewCategory from a dict
new_category_from_dict = NewCategory.from_dict(new_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


