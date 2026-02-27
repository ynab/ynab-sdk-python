# SaveMonthCategory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**budgeted** | **int** | Assigned (budgeted) amount in milliunits format | 

## Example

```python
from ynab.models.save_month_category import SaveMonthCategory

# TODO update the JSON string below
json = "{}"
# create an instance of SaveMonthCategory from a JSON string
save_month_category_instance = SaveMonthCategory.from_json(json)
# print the JSON string representation of the object
print(SaveMonthCategory.to_json())

# convert the object into a dict
save_month_category_dict = save_month_category_instance.to_dict()
# create an instance of SaveMonthCategory from a dict
save_month_category_from_dict = SaveMonthCategory.from_dict(save_month_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


