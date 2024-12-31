# SaveScheduledTransaction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** |  | 
**var_date** | **date** | The scheduled transaction date in ISO format (e.g. 2016-12-01).  This should be a future date no more than 5 years into the future. | 
**amount** | **int** | The scheduled transaction amount in milliunits format. | [optional] 
**payee_id** | **str** | The payee for the scheduled transaction.  To create a transfer between two accounts, use the account transfer payee pointing to the target account.  Account transfer payees are specified as &#x60;transfer_payee_id&#x60; on the account resource. | [optional] 
**payee_name** | **str** | The payee name for the the scheduled transaction.  If a &#x60;payee_name&#x60; value is provided and &#x60;payee_id&#x60; has a null value, the &#x60;payee_name&#x60; value will be used to resolve the payee by either (1) a payee with the same name or (2) creation of a new payee. | [optional] 
**category_id** | **str** | The category for the scheduled transaction. Credit Card Payment categories are not permitted. Creating a split scheduled transaction is not currently supported. | [optional] 
**memo** | **str** |  | [optional] 
**flag_color** | [**TransactionFlagColor**](TransactionFlagColor.md) |  | [optional] 
**frequency** | [**ScheduledTransactionFrequency**](ScheduledTransactionFrequency.md) |  | [optional] 

## Example

```python
from ynab.models.save_scheduled_transaction import SaveScheduledTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of SaveScheduledTransaction from a JSON string
save_scheduled_transaction_instance = SaveScheduledTransaction.from_json(json)
# print the JSON string representation of the object
print(SaveScheduledTransaction.to_json())

# convert the object into a dict
save_scheduled_transaction_dict = save_scheduled_transaction_instance.to_dict()
# create an instance of SaveScheduledTransaction from a dict
save_scheduled_transaction_from_dict = SaveScheduledTransaction.from_dict(save_scheduled_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


