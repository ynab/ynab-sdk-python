# Account


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**name** | **str** |  | 
**type** | [**AccountType**](AccountType.md) |  | 
**on_budget** | **bool** | Whether this account is \&quot;on budget\&quot; or not | 
**closed** | **bool** | Whether this account is closed or not | 
**note** | **str** |  | [optional] 
**balance** | **int** | The current available balance of the account in milliunits format | 
**cleared_balance** | **int** | The current cleared balance of the account in milliunits format | 
**uncleared_balance** | **int** | The current uncleared balance of the account in milliunits format | 
**transfer_payee_id** | **UUID** | The payee id which should be used when transferring to this account | 
**direct_import_linked** | **bool** | Whether or not the account is linked to a financial institution for automatic transaction import. | [optional] 
**direct_import_in_error** | **bool** | If an account linked to a financial institution (direct_import_linked&#x3D;true) and the linked connection is not in a healthy state, this will be true. | [optional] 
**last_reconciled_at** | **datetime** | A date/time specifying when the account was last reconciled. | [optional] 
**debt_original_balance** | **int** | This field is deprecated and will always be null. | [optional] 
**debt_interest_rates** | **Dict[str, int]** |  | [optional] 
**debt_minimum_payments** | **Dict[str, int]** |  | [optional] 
**debt_escrow_amounts** | **Dict[str, int]** |  | [optional] 
**deleted** | **bool** | Whether or not the account has been deleted.  Deleted accounts will only be included in delta requests. | 

## Example

```python
from ynab.models.account import Account

# TODO update the JSON string below
json = "{}"
# create an instance of Account from a JSON string
account_instance = Account.from_json(json)
# print the JSON string representation of the object
print(Account.to_json())

# convert the object into a dict
account_dict = account_instance.to_dict()
# create an instance of Account from a dict
account_from_dict = Account.from_dict(account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


