# CategoryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CategoryResponseData**](CategoryResponseData.md) |  | 

## Example

```python
from ynab.models.category_response import CategoryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CategoryResponse from a JSON string
category_response_instance = CategoryResponse.from_json(json)
# print the JSON string representation of the object
print(CategoryResponse.to_json())

# convert the object into a dict
category_response_dict = category_response_instance.to_dict()
# create an instance of CategoryResponse from a dict
category_response_from_dict = CategoryResponse.from_dict(category_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


