# MonthDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**month** | **date** |  | 
**note** | **str** |  | [optional] 
**income** | **int** | The total amount of transactions categorized to &#39;Inflow: Ready to Assign&#39; in the month | 
**budgeted** | **int** | The total amount assigned (budgeted) in the month | 
**activity** | **int** | The total amount of transactions in the month, excluding those categorized to &#39;Inflow: Ready to Assign&#39; | 
**to_be_budgeted** | **int** | The available amount for &#39;Ready to Assign&#39; | 
**age_of_money** | **int** | The Age of Money as of the month | [optional] 
**deleted** | **bool** | Whether or not the month has been deleted.  Deleted months will only be included in delta requests. | 
**categories** | [**List[Category]**](Category.md) | The plan month categories.  Amounts (budgeted, activity, balance, etc.) are specific to the {month} parameter specified. | 

## Example

```python
from ynab.models.month_detail import MonthDetail

# TODO update the JSON string below
json = "{}"
# create an instance of MonthDetail from a JSON string
month_detail_instance = MonthDetail.from_json(json)
# print the JSON string representation of the object
print(MonthDetail.to_json())

# convert the object into a dict
month_detail_dict = month_detail_instance.to_dict()
# create an instance of MonthDetail from a dict
month_detail_from_dict = MonthDetail.from_dict(month_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


