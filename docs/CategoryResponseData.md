# CategoryResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | [**Category**](Category.md) |  | 

## Example

```python
from ynab.models.category_response_data import CategoryResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of CategoryResponseData from a JSON string
category_response_data_instance = CategoryResponseData.from_json(json)
# print the JSON string representation of the object
print(CategoryResponseData.to_json())

# convert the object into a dict
category_response_data_dict = category_response_data_instance.to_dict()
# create an instance of CategoryResponseData from a dict
category_response_data_from_dict = CategoryResponseData.from_dict(category_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


