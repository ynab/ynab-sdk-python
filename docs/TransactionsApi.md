# ynab.TransactionsApi

All URIs are relative to *https://api.ynab.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_transaction**](TransactionsApi.md#create_transaction) | **POST** /budgets/{plan_id}/transactions | Create a single transaction or multiple transactions
[**delete_transaction**](TransactionsApi.md#delete_transaction) | **DELETE** /budgets/{plan_id}/transactions/{transaction_id} | Delete a transaction
[**get_transaction_by_id**](TransactionsApi.md#get_transaction_by_id) | **GET** /budgets/{plan_id}/transactions/{transaction_id} | Get a transaction
[**get_transactions**](TransactionsApi.md#get_transactions) | **GET** /budgets/{plan_id}/transactions | Get all transactions
[**get_transactions_by_account**](TransactionsApi.md#get_transactions_by_account) | **GET** /budgets/{plan_id}/accounts/{account_id}/transactions | Get all account transactions
[**get_transactions_by_category**](TransactionsApi.md#get_transactions_by_category) | **GET** /budgets/{plan_id}/categories/{category_id}/transactions | Get all category transactions
[**get_transactions_by_month**](TransactionsApi.md#get_transactions_by_month) | **GET** /budgets/{plan_id}/months/{month}/transactions | Get all plan month transactions
[**get_transactions_by_payee**](TransactionsApi.md#get_transactions_by_payee) | **GET** /budgets/{plan_id}/payees/{payee_id}/transactions | Get all payee transactions
[**import_transactions**](TransactionsApi.md#import_transactions) | **POST** /budgets/{plan_id}/transactions/import | Import transactions
[**update_transaction**](TransactionsApi.md#update_transaction) | **PUT** /budgets/{plan_id}/transactions/{transaction_id} | Update a transaction
[**update_transactions**](TransactionsApi.md#update_transactions) | **PATCH** /budgets/{plan_id}/transactions | Update multiple transactions


# **create_transaction**
> SaveTransactionsResponse create_transaction(plan_id, data)

Create a single transaction or multiple transactions

Creates a single transaction or multiple transactions.  If you provide a body containing a `transaction` object, a single transaction will be created and if you provide a body containing a `transactions` array, multiple transactions will be created.  Scheduled transactions (transactions with a future date) cannot be created on this endpoint.

### Example

* Bearer Authentication (bearer):

```python
import ynab
from ynab.models.post_transactions_wrapper import PostTransactionsWrapper
from ynab.models.save_transactions_response import SaveTransactionsResponse
from ynab.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ynab.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ynab.Configuration(
    host = "https://api.ynab.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer
configuration = ynab.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with ynab.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ynab.TransactionsApi(api_client)
    plan_id = 'plan_id_example' # str | The id of the plan. \"last-used\" can be used to specify the last used plan and \"default\" can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan).
    data = ynab.PostTransactionsWrapper() # PostTransactionsWrapper | The transaction or transactions to create.  To create a single transaction you can specify a value for the `transaction` object and to create multiple transactions you can specify an array of `transactions`.  It is expected that you will only provide a value for one of these objects.

    try:
        # Create a single transaction or multiple transactions
        api_response = api_instance.create_transaction(plan_id, data)
        print("The response of TransactionsApi->create_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->create_transaction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_id** | **str**| The id of the plan. \&quot;last-used\&quot; can be used to specify the last used plan and \&quot;default\&quot; can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan). | 
 **data** | [**PostTransactionsWrapper**](PostTransactionsWrapper.md)| The transaction or transactions to create.  To create a single transaction you can specify a value for the &#x60;transaction&#x60; object and to create multiple transactions you can specify an array of &#x60;transactions&#x60;.  It is expected that you will only provide a value for one of these objects. | 

### Return type

[**SaveTransactionsResponse**](SaveTransactionsResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The transaction or transactions were successfully created |  -  |
**400** | The request could not be understood due to malformed syntax or validation error(s). |  -  |
**409** | A transaction on the same account with the same &#x60;import_id&#x60; already exists. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_transaction**
> TransactionResponse delete_transaction(plan_id, transaction_id)

Delete a transaction

Deletes a transaction

### Example

* Bearer Authentication (bearer):

```python
import ynab
from ynab.models.transaction_response import TransactionResponse
from ynab.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ynab.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ynab.Configuration(
    host = "https://api.ynab.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer
configuration = ynab.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with ynab.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ynab.TransactionsApi(api_client)
    plan_id = 'plan_id_example' # str | The id of the plan. \"last-used\" can be used to specify the last used plan and \"default\" can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan).
    transaction_id = 'transaction_id_example' # str | The id of the transaction

    try:
        # Delete a transaction
        api_response = api_instance.delete_transaction(plan_id, transaction_id)
        print("The response of TransactionsApi->delete_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->delete_transaction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_id** | **str**| The id of the plan. \&quot;last-used\&quot; can be used to specify the last used plan and \&quot;default\&quot; can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan). | 
 **transaction_id** | **str**| The id of the transaction | 

### Return type

[**TransactionResponse**](TransactionResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The transaction was successfully deleted |  -  |
**404** | The transaction was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transaction_by_id**
> TransactionResponse get_transaction_by_id(plan_id, transaction_id)

Get a transaction

Returns a single transaction

### Example

* Bearer Authentication (bearer):

```python
import ynab
from ynab.models.transaction_response import TransactionResponse
from ynab.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ynab.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ynab.Configuration(
    host = "https://api.ynab.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer
configuration = ynab.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with ynab.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ynab.TransactionsApi(api_client)
    plan_id = 'plan_id_example' # str | The id of the plan. \"last-used\" can be used to specify the last used plan and \"default\" can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan).
    transaction_id = 'transaction_id_example' # str | The id of the transaction

    try:
        # Get a transaction
        api_response = api_instance.get_transaction_by_id(plan_id, transaction_id)
        print("The response of TransactionsApi->get_transaction_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->get_transaction_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_id** | **str**| The id of the plan. \&quot;last-used\&quot; can be used to specify the last used plan and \&quot;default\&quot; can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan). | 
 **transaction_id** | **str**| The id of the transaction | 

### Return type

[**TransactionResponse**](TransactionResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested transaction |  -  |
**404** | The transaction was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transactions**
> TransactionsResponse get_transactions(plan_id, since_date=since_date, type=type, last_knowledge_of_server=last_knowledge_of_server)

Get all transactions

Returns plan transactions, excluding any pending transactions

### Example

* Bearer Authentication (bearer):

```python
import ynab
from ynab.models.transactions_response import TransactionsResponse
from ynab.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ynab.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ynab.Configuration(
    host = "https://api.ynab.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer
configuration = ynab.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with ynab.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ynab.TransactionsApi(api_client)
    plan_id = 'plan_id_example' # str | The id of the plan. \"last-used\" can be used to specify the last used plan and \"default\" can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan).
    since_date = '2013-10-20' # date | If specified, only transactions on or after this date will be included.  The date should be ISO formatted (e.g. 2016-12-30). (optional)
    type = 'type_example' # str | If specified, only transactions of the specified type will be included. \"uncategorized\" and \"unapproved\" are currently supported. (optional)
    last_knowledge_of_server = 56 # int | The starting server knowledge.  If provided, only entities that have changed since `last_knowledge_of_server` will be included. (optional)

    try:
        # Get all transactions
        api_response = api_instance.get_transactions(plan_id, since_date=since_date, type=type, last_knowledge_of_server=last_knowledge_of_server)
        print("The response of TransactionsApi->get_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->get_transactions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_id** | **str**| The id of the plan. \&quot;last-used\&quot; can be used to specify the last used plan and \&quot;default\&quot; can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan). | 
 **since_date** | **date**| If specified, only transactions on or after this date will be included.  The date should be ISO formatted (e.g. 2016-12-30). | [optional] 
 **type** | **str**| If specified, only transactions of the specified type will be included. \&quot;uncategorized\&quot; and \&quot;unapproved\&quot; are currently supported. | [optional] 
 **last_knowledge_of_server** | **int**| The starting server knowledge.  If provided, only entities that have changed since &#x60;last_knowledge_of_server&#x60; will be included. | [optional] 

### Return type

[**TransactionsResponse**](TransactionsResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of requested transactions |  -  |
**400** | An error occurred |  -  |
**404** | No transactions were found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transactions_by_account**
> TransactionsResponse get_transactions_by_account(plan_id, account_id, since_date=since_date, type=type, last_knowledge_of_server=last_knowledge_of_server)

Get all account transactions

Returns all transactions for a specified account, excluding any pending transactions

### Example

* Bearer Authentication (bearer):

```python
import ynab
from ynab.models.transactions_response import TransactionsResponse
from ynab.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ynab.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ynab.Configuration(
    host = "https://api.ynab.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer
configuration = ynab.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with ynab.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ynab.TransactionsApi(api_client)
    plan_id = 'plan_id_example' # str | The id of the plan. \"last-used\" can be used to specify the last used plan and \"default\" can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan).
    account_id = 'account_id_example' # str | The id of the account
    since_date = '2013-10-20' # date | If specified, only transactions on or after this date will be included.  The date should be ISO formatted (e.g. 2016-12-30). (optional)
    type = 'type_example' # str | If specified, only transactions of the specified type will be included. \"uncategorized\" and \"unapproved\" are currently supported. (optional)
    last_knowledge_of_server = 56 # int | The starting server knowledge.  If provided, only entities that have changed since `last_knowledge_of_server` will be included. (optional)

    try:
        # Get all account transactions
        api_response = api_instance.get_transactions_by_account(plan_id, account_id, since_date=since_date, type=type, last_knowledge_of_server=last_knowledge_of_server)
        print("The response of TransactionsApi->get_transactions_by_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->get_transactions_by_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_id** | **str**| The id of the plan. \&quot;last-used\&quot; can be used to specify the last used plan and \&quot;default\&quot; can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan). | 
 **account_id** | **str**| The id of the account | 
 **since_date** | **date**| If specified, only transactions on or after this date will be included.  The date should be ISO formatted (e.g. 2016-12-30). | [optional] 
 **type** | **str**| If specified, only transactions of the specified type will be included. \&quot;uncategorized\&quot; and \&quot;unapproved\&quot; are currently supported. | [optional] 
 **last_knowledge_of_server** | **int**| The starting server knowledge.  If provided, only entities that have changed since &#x60;last_knowledge_of_server&#x60; will be included. | [optional] 

### Return type

[**TransactionsResponse**](TransactionsResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of requested transactions |  -  |
**404** | No transactions were found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transactions_by_category**
> HybridTransactionsResponse get_transactions_by_category(plan_id, category_id, since_date=since_date, type=type, last_knowledge_of_server=last_knowledge_of_server)

Get all category transactions

Returns all transactions for a specified category, excluding any pending transactions

### Example

* Bearer Authentication (bearer):

```python
import ynab
from ynab.models.hybrid_transactions_response import HybridTransactionsResponse
from ynab.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ynab.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ynab.Configuration(
    host = "https://api.ynab.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer
configuration = ynab.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with ynab.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ynab.TransactionsApi(api_client)
    plan_id = 'plan_id_example' # str | The id of the plan. \"last-used\" can be used to specify the last used plan and \"default\" can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan).
    category_id = 'category_id_example' # str | The id of the category
    since_date = '2013-10-20' # date | If specified, only transactions on or after this date will be included.  The date should be ISO formatted (e.g. 2016-12-30). (optional)
    type = 'type_example' # str | If specified, only transactions of the specified type will be included. \"uncategorized\" and \"unapproved\" are currently supported. (optional)
    last_knowledge_of_server = 56 # int | The starting server knowledge.  If provided, only entities that have changed since `last_knowledge_of_server` will be included. (optional)

    try:
        # Get all category transactions
        api_response = api_instance.get_transactions_by_category(plan_id, category_id, since_date=since_date, type=type, last_knowledge_of_server=last_knowledge_of_server)
        print("The response of TransactionsApi->get_transactions_by_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->get_transactions_by_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_id** | **str**| The id of the plan. \&quot;last-used\&quot; can be used to specify the last used plan and \&quot;default\&quot; can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan). | 
 **category_id** | **str**| The id of the category | 
 **since_date** | **date**| If specified, only transactions on or after this date will be included.  The date should be ISO formatted (e.g. 2016-12-30). | [optional] 
 **type** | **str**| If specified, only transactions of the specified type will be included. \&quot;uncategorized\&quot; and \&quot;unapproved\&quot; are currently supported. | [optional] 
 **last_knowledge_of_server** | **int**| The starting server knowledge.  If provided, only entities that have changed since &#x60;last_knowledge_of_server&#x60; will be included. | [optional] 

### Return type

[**HybridTransactionsResponse**](HybridTransactionsResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of requested transactions |  -  |
**404** | No transactions were found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transactions_by_month**
> TransactionsResponse get_transactions_by_month(plan_id, month, since_date=since_date, type=type, last_knowledge_of_server=last_knowledge_of_server)

Get all plan month transactions

Returns all transactions for a specified month, excluding any pending transactions

### Example

* Bearer Authentication (bearer):

```python
import ynab
from ynab.models.transactions_response import TransactionsResponse
from ynab.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ynab.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ynab.Configuration(
    host = "https://api.ynab.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer
configuration = ynab.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with ynab.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ynab.TransactionsApi(api_client)
    plan_id = 'plan_id_example' # str | The id of the plan. \"last-used\" can be used to specify the last used plan and \"default\" can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan).
    month = 'month_example' # str | The plan month in ISO format (e.g. 2016-12-01) (\"current\" can also be used to specify the current calendar month (UTC))
    since_date = '2013-10-20' # date | If specified, only transactions on or after this date will be included.  The date should be ISO formatted (e.g. 2016-12-30). (optional)
    type = 'type_example' # str | If specified, only transactions of the specified type will be included. \"uncategorized\" and \"unapproved\" are currently supported. (optional)
    last_knowledge_of_server = 56 # int | The starting server knowledge.  If provided, only entities that have changed since `last_knowledge_of_server` will be included. (optional)

    try:
        # Get all plan month transactions
        api_response = api_instance.get_transactions_by_month(plan_id, month, since_date=since_date, type=type, last_knowledge_of_server=last_knowledge_of_server)
        print("The response of TransactionsApi->get_transactions_by_month:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->get_transactions_by_month: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_id** | **str**| The id of the plan. \&quot;last-used\&quot; can be used to specify the last used plan and \&quot;default\&quot; can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan). | 
 **month** | **str**| The plan month in ISO format (e.g. 2016-12-01) (\&quot;current\&quot; can also be used to specify the current calendar month (UTC)) | 
 **since_date** | **date**| If specified, only transactions on or after this date will be included.  The date should be ISO formatted (e.g. 2016-12-30). | [optional] 
 **type** | **str**| If specified, only transactions of the specified type will be included. \&quot;uncategorized\&quot; and \&quot;unapproved\&quot; are currently supported. | [optional] 
 **last_knowledge_of_server** | **int**| The starting server knowledge.  If provided, only entities that have changed since &#x60;last_knowledge_of_server&#x60; will be included. | [optional] 

### Return type

[**TransactionsResponse**](TransactionsResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of requested transactions |  -  |
**404** | No transactions were found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transactions_by_payee**
> HybridTransactionsResponse get_transactions_by_payee(plan_id, payee_id, since_date=since_date, type=type, last_knowledge_of_server=last_knowledge_of_server)

Get all payee transactions

Returns all transactions for a specified payee, excluding any pending transactions

### Example

* Bearer Authentication (bearer):

```python
import ynab
from ynab.models.hybrid_transactions_response import HybridTransactionsResponse
from ynab.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ynab.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ynab.Configuration(
    host = "https://api.ynab.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer
configuration = ynab.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with ynab.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ynab.TransactionsApi(api_client)
    plan_id = 'plan_id_example' # str | The id of the plan. \"last-used\" can be used to specify the last used plan and \"default\" can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan).
    payee_id = 'payee_id_example' # str | The id of the payee
    since_date = '2013-10-20' # date | If specified, only transactions on or after this date will be included.  The date should be ISO formatted (e.g. 2016-12-30). (optional)
    type = 'type_example' # str | If specified, only transactions of the specified type will be included. \"uncategorized\" and \"unapproved\" are currently supported. (optional)
    last_knowledge_of_server = 56 # int | The starting server knowledge.  If provided, only entities that have changed since `last_knowledge_of_server` will be included. (optional)

    try:
        # Get all payee transactions
        api_response = api_instance.get_transactions_by_payee(plan_id, payee_id, since_date=since_date, type=type, last_knowledge_of_server=last_knowledge_of_server)
        print("The response of TransactionsApi->get_transactions_by_payee:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->get_transactions_by_payee: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_id** | **str**| The id of the plan. \&quot;last-used\&quot; can be used to specify the last used plan and \&quot;default\&quot; can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan). | 
 **payee_id** | **str**| The id of the payee | 
 **since_date** | **date**| If specified, only transactions on or after this date will be included.  The date should be ISO formatted (e.g. 2016-12-30). | [optional] 
 **type** | **str**| If specified, only transactions of the specified type will be included. \&quot;uncategorized\&quot; and \&quot;unapproved\&quot; are currently supported. | [optional] 
 **last_knowledge_of_server** | **int**| The starting server knowledge.  If provided, only entities that have changed since &#x60;last_knowledge_of_server&#x60; will be included. | [optional] 

### Return type

[**HybridTransactionsResponse**](HybridTransactionsResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of requested transactions |  -  |
**404** | No transactions were found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_transactions**
> TransactionsImportResponse import_transactions(plan_id)

Import transactions

Imports available transactions on all linked accounts for the given plan.  Linked accounts allow transactions to be imported directly from a specified financial institution and this endpoint initiates that import.  Sending a request to this endpoint is the equivalent of clicking "Import" on each account in the web application or tapping the "New Transactions" banner in the mobile applications.  The response for this endpoint contains the transaction ids that have been imported.

### Example

* Bearer Authentication (bearer):

```python
import ynab
from ynab.models.transactions_import_response import TransactionsImportResponse
from ynab.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ynab.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ynab.Configuration(
    host = "https://api.ynab.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer
configuration = ynab.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with ynab.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ynab.TransactionsApi(api_client)
    plan_id = 'plan_id_example' # str | The id of the plan. \"last-used\" can be used to specify the last used plan and \"default\" can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan).

    try:
        # Import transactions
        api_response = api_instance.import_transactions(plan_id)
        print("The response of TransactionsApi->import_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->import_transactions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_id** | **str**| The id of the plan. \&quot;last-used\&quot; can be used to specify the last used plan and \&quot;default\&quot; can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan). | 

### Return type

[**TransactionsImportResponse**](TransactionsImportResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request was successful but there were no transactions to import |  -  |
**201** | One or more transactions were imported successfully |  -  |
**400** | The request could not be understood due to malformed syntax or validation error(s) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_transaction**
> TransactionResponse update_transaction(plan_id, transaction_id, data)

Update a transaction

Updates a single transaction

### Example

* Bearer Authentication (bearer):

```python
import ynab
from ynab.models.put_transaction_wrapper import PutTransactionWrapper
from ynab.models.transaction_response import TransactionResponse
from ynab.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ynab.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ynab.Configuration(
    host = "https://api.ynab.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer
configuration = ynab.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with ynab.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ynab.TransactionsApi(api_client)
    plan_id = 'plan_id_example' # str | The id of the plan. \"last-used\" can be used to specify the last used plan and \"default\" can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan).
    transaction_id = 'transaction_id_example' # str | The id of the transaction
    data = ynab.PutTransactionWrapper() # PutTransactionWrapper | The transaction to update

    try:
        # Update a transaction
        api_response = api_instance.update_transaction(plan_id, transaction_id, data)
        print("The response of TransactionsApi->update_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->update_transaction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_id** | **str**| The id of the plan. \&quot;last-used\&quot; can be used to specify the last used plan and \&quot;default\&quot; can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan). | 
 **transaction_id** | **str**| The id of the transaction | 
 **data** | [**PutTransactionWrapper**](PutTransactionWrapper.md)| The transaction to update | 

### Return type

[**TransactionResponse**](TransactionResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The transaction was successfully updated |  -  |
**400** | The request could not be understood due to malformed syntax or validation error(s) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_transactions**
> SaveTransactionsResponse update_transactions(plan_id, data)

Update multiple transactions

Updates multiple transactions, by `id` or `import_id`.

### Example

* Bearer Authentication (bearer):

```python
import ynab
from ynab.models.patch_transactions_wrapper import PatchTransactionsWrapper
from ynab.models.save_transactions_response import SaveTransactionsResponse
from ynab.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ynab.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ynab.Configuration(
    host = "https://api.ynab.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer
configuration = ynab.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with ynab.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ynab.TransactionsApi(api_client)
    plan_id = 'plan_id_example' # str | The id of the plan. \"last-used\" can be used to specify the last used plan and \"default\" can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan).
    data = ynab.PatchTransactionsWrapper() # PatchTransactionsWrapper | The transactions to update. Each transaction must have either an `id` or `import_id` specified. If `id` is specified as null an `import_id` value can be provided which will allow transaction(s) to be updated by its `import_id`. If an `id` is specified, it will always be used for lookup.  You should not specify both `id` and `import_id`.  Updating an `import_id` on an existing transaction is not allowed; if an `import_id` is specified, it will only be used to lookup the transaction.

    try:
        # Update multiple transactions
        api_response = api_instance.update_transactions(plan_id, data)
        print("The response of TransactionsApi->update_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->update_transactions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_id** | **str**| The id of the plan. \&quot;last-used\&quot; can be used to specify the last used plan and \&quot;default\&quot; can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan). | 
 **data** | [**PatchTransactionsWrapper**](PatchTransactionsWrapper.md)| The transactions to update. Each transaction must have either an &#x60;id&#x60; or &#x60;import_id&#x60; specified. If &#x60;id&#x60; is specified as null an &#x60;import_id&#x60; value can be provided which will allow transaction(s) to be updated by its &#x60;import_id&#x60;. If an &#x60;id&#x60; is specified, it will always be used for lookup.  You should not specify both &#x60;id&#x60; and &#x60;import_id&#x60;.  Updating an &#x60;import_id&#x60; on an existing transaction is not allowed; if an &#x60;import_id&#x60; is specified, it will only be used to lookup the transaction. | 

### Return type

[**SaveTransactionsResponse**](SaveTransactionsResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**209** | The transactions were successfully updated |  -  |
**400** | The request could not be understood due to malformed syntax or validation error(s). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

