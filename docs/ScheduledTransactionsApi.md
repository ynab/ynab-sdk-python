# ynab.ScheduledTransactionsApi

All URIs are relative to *https://api.ynab.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_scheduled_transaction**](ScheduledTransactionsApi.md#create_scheduled_transaction) | **POST** /budgets/{plan_id}/scheduled_transactions | Create a scheduled transaction
[**delete_scheduled_transaction**](ScheduledTransactionsApi.md#delete_scheduled_transaction) | **DELETE** /budgets/{plan_id}/scheduled_transactions/{scheduled_transaction_id} | Delete a scheduled transaction
[**get_scheduled_transaction_by_id**](ScheduledTransactionsApi.md#get_scheduled_transaction_by_id) | **GET** /budgets/{plan_id}/scheduled_transactions/{scheduled_transaction_id} | Get a scheduled transaction
[**get_scheduled_transactions**](ScheduledTransactionsApi.md#get_scheduled_transactions) | **GET** /budgets/{plan_id}/scheduled_transactions | Get all scheduled transactions
[**update_scheduled_transaction**](ScheduledTransactionsApi.md#update_scheduled_transaction) | **PUT** /budgets/{plan_id}/scheduled_transactions/{scheduled_transaction_id} | Update a scheduled transaction


# **create_scheduled_transaction**
> ScheduledTransactionResponse create_scheduled_transaction(plan_id, data)

Create a scheduled transaction

Creates a single scheduled transaction (a transaction with a future date).

### Example

* Bearer Authentication (bearer):

```python
import ynab
from ynab.models.post_scheduled_transaction_wrapper import PostScheduledTransactionWrapper
from ynab.models.scheduled_transaction_response import ScheduledTransactionResponse
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
    api_instance = ynab.ScheduledTransactionsApi(api_client)
    plan_id = 'plan_id_example' # str | The id of the plan. \"last-used\" can be used to specify the last used plan and \"default\" can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan).
    data = ynab.PostScheduledTransactionWrapper() # PostScheduledTransactionWrapper | The scheduled transaction to create

    try:
        # Create a scheduled transaction
        api_response = api_instance.create_scheduled_transaction(plan_id, data)
        print("The response of ScheduledTransactionsApi->create_scheduled_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScheduledTransactionsApi->create_scheduled_transaction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_id** | **str**| The id of the plan. \&quot;last-used\&quot; can be used to specify the last used plan and \&quot;default\&quot; can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan). | 
 **data** | [**PostScheduledTransactionWrapper**](PostScheduledTransactionWrapper.md)| The scheduled transaction to create | 

### Return type

[**ScheduledTransactionResponse**](ScheduledTransactionResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The scheduled transaction was successfully created |  -  |
**400** | The request could not be understood due to malformed syntax or validation error(s). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_scheduled_transaction**
> ScheduledTransactionResponse delete_scheduled_transaction(plan_id, scheduled_transaction_id)

Delete a scheduled transaction

Deletes a scheduled transaction

### Example

* Bearer Authentication (bearer):

```python
import ynab
from ynab.models.scheduled_transaction_response import ScheduledTransactionResponse
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
    api_instance = ynab.ScheduledTransactionsApi(api_client)
    plan_id = 'plan_id_example' # str | The id of the plan. \"last-used\" can be used to specify the last used plan and \"default\" can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan).
    scheduled_transaction_id = 'scheduled_transaction_id_example' # str | The id of the scheduled transaction

    try:
        # Delete a scheduled transaction
        api_response = api_instance.delete_scheduled_transaction(plan_id, scheduled_transaction_id)
        print("The response of ScheduledTransactionsApi->delete_scheduled_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScheduledTransactionsApi->delete_scheduled_transaction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_id** | **str**| The id of the plan. \&quot;last-used\&quot; can be used to specify the last used plan and \&quot;default\&quot; can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan). | 
 **scheduled_transaction_id** | **str**| The id of the scheduled transaction | 

### Return type

[**ScheduledTransactionResponse**](ScheduledTransactionResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The scheduled transaction was successfully deleted |  -  |
**404** | The scheduled transaction was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scheduled_transaction_by_id**
> ScheduledTransactionResponse get_scheduled_transaction_by_id(plan_id, scheduled_transaction_id)

Get a scheduled transaction

Returns a single scheduled transaction

### Example

* Bearer Authentication (bearer):

```python
import ynab
from ynab.models.scheduled_transaction_response import ScheduledTransactionResponse
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
    api_instance = ynab.ScheduledTransactionsApi(api_client)
    plan_id = 'plan_id_example' # str | The id of the plan. \"last-used\" can be used to specify the last used plan and \"default\" can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan).
    scheduled_transaction_id = 'scheduled_transaction_id_example' # str | The id of the scheduled transaction

    try:
        # Get a scheduled transaction
        api_response = api_instance.get_scheduled_transaction_by_id(plan_id, scheduled_transaction_id)
        print("The response of ScheduledTransactionsApi->get_scheduled_transaction_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScheduledTransactionsApi->get_scheduled_transaction_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_id** | **str**| The id of the plan. \&quot;last-used\&quot; can be used to specify the last used plan and \&quot;default\&quot; can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan). | 
 **scheduled_transaction_id** | **str**| The id of the scheduled transaction | 

### Return type

[**ScheduledTransactionResponse**](ScheduledTransactionResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Scheduled Transaction |  -  |
**404** | The scheduled transaction was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scheduled_transactions**
> ScheduledTransactionsResponse get_scheduled_transactions(plan_id, last_knowledge_of_server=last_knowledge_of_server)

Get all scheduled transactions

Returns all scheduled transactions

### Example

* Bearer Authentication (bearer):

```python
import ynab
from ynab.models.scheduled_transactions_response import ScheduledTransactionsResponse
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
    api_instance = ynab.ScheduledTransactionsApi(api_client)
    plan_id = 'plan_id_example' # str | The id of the plan. \"last-used\" can be used to specify the last used plan and \"default\" can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan).
    last_knowledge_of_server = 56 # int | The starting server knowledge.  If provided, only entities that have changed since `last_knowledge_of_server` will be included. (optional)

    try:
        # Get all scheduled transactions
        api_response = api_instance.get_scheduled_transactions(plan_id, last_knowledge_of_server=last_knowledge_of_server)
        print("The response of ScheduledTransactionsApi->get_scheduled_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScheduledTransactionsApi->get_scheduled_transactions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_id** | **str**| The id of the plan. \&quot;last-used\&quot; can be used to specify the last used plan and \&quot;default\&quot; can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan). | 
 **last_knowledge_of_server** | **int**| The starting server knowledge.  If provided, only entities that have changed since &#x60;last_knowledge_of_server&#x60; will be included. | [optional] 

### Return type

[**ScheduledTransactionsResponse**](ScheduledTransactionsResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of requested scheduled transactions |  -  |
**404** | No scheduled transactions were found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_scheduled_transaction**
> ScheduledTransactionResponse update_scheduled_transaction(plan_id, scheduled_transaction_id, put_scheduled_transaction_wrapper)

Update a scheduled transaction

Updates a single scheduled transaction

### Example

* Bearer Authentication (bearer):

```python
import ynab
from ynab.models.put_scheduled_transaction_wrapper import PutScheduledTransactionWrapper
from ynab.models.scheduled_transaction_response import ScheduledTransactionResponse
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
    api_instance = ynab.ScheduledTransactionsApi(api_client)
    plan_id = 'plan_id_example' # str | The id of the plan. \"last-used\" can be used to specify the last used plan and \"default\" can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan).
    scheduled_transaction_id = 'scheduled_transaction_id_example' # str | The id of the scheduled transaction
    put_scheduled_transaction_wrapper = ynab.PutScheduledTransactionWrapper() # PutScheduledTransactionWrapper | The scheduled transaction to update

    try:
        # Update a scheduled transaction
        api_response = api_instance.update_scheduled_transaction(plan_id, scheduled_transaction_id, put_scheduled_transaction_wrapper)
        print("The response of ScheduledTransactionsApi->update_scheduled_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScheduledTransactionsApi->update_scheduled_transaction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_id** | **str**| The id of the plan. \&quot;last-used\&quot; can be used to specify the last used plan and \&quot;default\&quot; can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan). | 
 **scheduled_transaction_id** | **str**| The id of the scheduled transaction | 
 **put_scheduled_transaction_wrapper** | [**PutScheduledTransactionWrapper**](PutScheduledTransactionWrapper.md)| The scheduled transaction to update | 

### Return type

[**ScheduledTransactionResponse**](ScheduledTransactionResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The scheduled transaction was successfully updated |  -  |
**400** | The request could not be understood due to malformed syntax or validation error(s) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

