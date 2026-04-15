# ScheduledSubTransactionBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**scheduled_transaction_id** | **UUID** |  | 
**amount** | **int** | The scheduled subtransaction amount in milliunits format | 
**memo** | **str** |  | [optional] 
**payee_id** | **UUID** |  | [optional] 
**payee_name** | **str** |  | [optional] 
**category_id** | **UUID** |  | [optional] 
**category_name** | **str** |  | [optional] 
**transfer_account_id** | **UUID** | If a transfer, the account_id which the scheduled subtransaction transfers to | [optional] 
**deleted** | **bool** | Whether or not the scheduled subtransaction has been deleted. Deleted scheduled subtransactions will only be included in delta requests. | 

## Example

```python
from ynab.models.scheduled_sub_transaction_base import ScheduledSubTransactionBase

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduledSubTransactionBase from a JSON string
scheduled_sub_transaction_base_instance = ScheduledSubTransactionBase.from_json(json)
# print the JSON string representation of the object
print(ScheduledSubTransactionBase.to_json())

# convert the object into a dict
scheduled_sub_transaction_base_dict = scheduled_sub_transaction_base_instance.to_dict()
# create an instance of ScheduledSubTransactionBase from a dict
scheduled_sub_transaction_base_from_dict = ScheduledSubTransactionBase.from_dict(scheduled_sub_transaction_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


