# SaveCategoryResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | [**Category**](Category.md) |  | 
**server_knowledge** | **int** | The knowledge of the server | 

## Example

```python
from ynab.models.save_category_response_data import SaveCategoryResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of SaveCategoryResponseData from a JSON string
save_category_response_data_instance = SaveCategoryResponseData.from_json(json)
# print the JSON string representation of the object
print(SaveCategoryResponseData.to_json())

# convert the object into a dict
save_category_response_data_dict = save_category_response_data_instance.to_dict()
# create an instance of SaveCategoryResponseData from a dict
save_category_response_data_from_dict = SaveCategoryResponseData.from_dict(save_category_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


