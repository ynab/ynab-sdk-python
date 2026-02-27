# SaveCategoryGroupResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**SaveCategoryGroupResponseData**](SaveCategoryGroupResponseData.md) |  | 

## Example

```python
from ynab.models.save_category_group_response import SaveCategoryGroupResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SaveCategoryGroupResponse from a JSON string
save_category_group_response_instance = SaveCategoryGroupResponse.from_json(json)
# print the JSON string representation of the object
print(SaveCategoryGroupResponse.to_json())

# convert the object into a dict
save_category_group_response_dict = save_category_group_response_instance.to_dict()
# create an instance of SaveCategoryGroupResponse from a dict
save_category_group_response_from_dict = SaveCategoryGroupResponse.from_dict(save_category_group_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


