# ScheduledSubTransaction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**scheduled_transaction_id** | **str** |  | 
**amount** | **int** | The scheduled subtransaction amount in milliunits format | 
**memo** | **str** |  | [optional] 
**payee_id** | **str** |  | [optional] 
**payee_name** | **str** |  | [optional] 
**category_id** | **str** |  | [optional] 
**category_name** | **str** |  | [optional] 
**transfer_account_id** | **str** | If a transfer, the account_id which the scheduled subtransaction transfers to | [optional] 
**deleted** | **bool** | Whether or not the scheduled subtransaction has been deleted. Deleted scheduled subtransactions will only be included in delta requests. | 

## Example

```python
from ynab.models.scheduled_sub_transaction import ScheduledSubTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduledSubTransaction from a JSON string
scheduled_sub_transaction_instance = ScheduledSubTransaction.from_json(json)
# print the JSON string representation of the object
print(ScheduledSubTransaction.to_json())

# convert the object into a dict
scheduled_sub_transaction_dict = scheduled_sub_transaction_instance.to_dict()
# create an instance of ScheduledSubTransaction from a dict
scheduled_sub_transaction_from_dict = ScheduledSubTransaction.from_dict(scheduled_sub_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


