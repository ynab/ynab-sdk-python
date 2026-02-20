# ScheduledTransactionSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**date_first** | **date** | The first date for which the Scheduled Transaction was scheduled. | 
**date_next** | **date** | The next date for which the Scheduled Transaction is scheduled. | 
**frequency** | **str** |  | 
**amount** | **int** | The scheduled transaction amount in milliunits format | 
**memo** | **str** |  | [optional] 
**flag_color** | [**TransactionFlagColor**](TransactionFlagColor.md) |  | [optional] 
**flag_name** | **str** | The customized name of a transaction flag | [optional] 
**account_id** | **UUID** |  | 
**payee_id** | **UUID** |  | [optional] 
**category_id** | **UUID** |  | [optional] 
**transfer_account_id** | **UUID** | If a transfer, the account_id which the scheduled transaction transfers to | [optional] 
**deleted** | **bool** | Whether or not the scheduled transaction has been deleted.  Deleted scheduled transactions will only be included in delta requests. | 

## Example

```python
from ynab.models.scheduled_transaction_summary import ScheduledTransactionSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduledTransactionSummary from a JSON string
scheduled_transaction_summary_instance = ScheduledTransactionSummary.from_json(json)
# print the JSON string representation of the object
print(ScheduledTransactionSummary.to_json())

# convert the object into a dict
scheduled_transaction_summary_dict = scheduled_transaction_summary_instance.to_dict()
# create an instance of ScheduledTransactionSummary from a dict
scheduled_transaction_summary_from_dict = ScheduledTransactionSummary.from_dict(scheduled_transaction_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


