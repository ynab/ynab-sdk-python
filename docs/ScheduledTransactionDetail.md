# ScheduledTransactionDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**date_first** | **date** | The first date for which the Scheduled Transaction was scheduled. | 
**date_next** | **date** | The next date for which the Scheduled Transaction is scheduled. | 
**frequency** | **str** |  | 
**amount** | **int** | The scheduled transaction amount in milliunits format | 
**memo** | **str** |  | [optional] 
**flag_color** | [**TransactionFlagColor**](TransactionFlagColor.md) |  | [optional] 
**flag_name** | **str** | The customized name of a transaction flag | [optional] 
**account_id** | **str** |  | 
**payee_id** | **str** |  | [optional] 
**category_id** | **str** |  | [optional] 
**transfer_account_id** | **str** | If a transfer, the account_id which the scheduled transaction transfers to | [optional] 
**deleted** | **bool** | Whether or not the scheduled transaction has been deleted.  Deleted scheduled transactions will only be included in delta requests. | 
**account_name** | **str** |  | 
**payee_name** | **str** |  | [optional] 
**category_name** | **str** | The name of the category.  If a split scheduled transaction, this will be &#39;Split&#39;. | [optional] 
**subtransactions** | [**List[ScheduledSubTransaction]**](ScheduledSubTransaction.md) | If a split scheduled transaction, the subtransactions. | 

## Example

```python
from ynab.models.scheduled_transaction_detail import ScheduledTransactionDetail

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduledTransactionDetail from a JSON string
scheduled_transaction_detail_instance = ScheduledTransactionDetail.from_json(json)
# print the JSON string representation of the object
print(ScheduledTransactionDetail.to_json())

# convert the object into a dict
scheduled_transaction_detail_dict = scheduled_transaction_detail_instance.to_dict()
# create an instance of ScheduledTransactionDetail from a dict
scheduled_transaction_detail_from_dict = ScheduledTransactionDetail.from_dict(scheduled_transaction_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


