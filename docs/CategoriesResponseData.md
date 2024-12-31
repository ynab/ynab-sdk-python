# CategoriesResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category_groups** | [**List[CategoryGroupWithCategories]**](CategoryGroupWithCategories.md) |  | 
**server_knowledge** | **int** | The knowledge of the server | 

## Example

```python
from ynab.models.categories_response_data import CategoriesResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of CategoriesResponseData from a JSON string
categories_response_data_instance = CategoriesResponseData.from_json(json)
# print the JSON string representation of the object
print(CategoriesResponseData.to_json())

# convert the object into a dict
categories_response_data_dict = categories_response_data_instance.to_dict()
# create an instance of CategoriesResponseData from a dict
categories_response_data_from_dict = CategoriesResponseData.from_dict(categories_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


