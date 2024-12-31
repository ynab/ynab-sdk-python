# SaveCategoryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**SaveCategoryResponseData**](SaveCategoryResponseData.md) |  | 

## Example

```python
from ynab.models.save_category_response import SaveCategoryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SaveCategoryResponse from a JSON string
save_category_response_instance = SaveCategoryResponse.from_json(json)
# print the JSON string representation of the object
print(SaveCategoryResponse.to_json())

# convert the object into a dict
save_category_response_dict = save_category_response_instance.to_dict()
# create an instance of SaveCategoryResponse from a dict
save_category_response_from_dict = SaveCategoryResponse.from_dict(save_category_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


