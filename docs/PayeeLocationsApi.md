# ynab.PayeeLocationsApi

All URIs are relative to *https://api.ynab.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_payee_location_by_id**](PayeeLocationsApi.md#get_payee_location_by_id) | **GET** /budgets/{plan_id}/payee_locations/{payee_location_id} | Get a payee location
[**get_payee_locations**](PayeeLocationsApi.md#get_payee_locations) | **GET** /budgets/{plan_id}/payee_locations | Get all payee locations
[**get_payee_locations_by_payee**](PayeeLocationsApi.md#get_payee_locations_by_payee) | **GET** /budgets/{plan_id}/payees/{payee_id}/payee_locations | Get all locations for a payee


# **get_payee_location_by_id**
> PayeeLocationResponse get_payee_location_by_id(plan_id, payee_location_id)

Get a payee location

Returns a single payee location

### Example

* Bearer Authentication (bearer):

```python
import ynab
from ynab.models.payee_location_response import PayeeLocationResponse
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
    api_instance = ynab.PayeeLocationsApi(api_client)
    plan_id = 'plan_id_example' # str | The id of the plan. \"last-used\" can be used to specify the last used plan and \"default\" can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan).
    payee_location_id = 'payee_location_id_example' # str | id of payee location

    try:
        # Get a payee location
        api_response = api_instance.get_payee_location_by_id(plan_id, payee_location_id)
        print("The response of PayeeLocationsApi->get_payee_location_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayeeLocationsApi->get_payee_location_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_id** | **str**| The id of the plan. \&quot;last-used\&quot; can be used to specify the last used plan and \&quot;default\&quot; can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan). | 
 **payee_location_id** | **str**| id of payee location | 

### Return type

[**PayeeLocationResponse**](PayeeLocationResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The payee location |  -  |
**404** | The payee location was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payee_locations**
> PayeeLocationsResponse get_payee_locations(plan_id)

Get all payee locations

Returns all payee locations

### Example

* Bearer Authentication (bearer):

```python
import ynab
from ynab.models.payee_locations_response import PayeeLocationsResponse
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
    api_instance = ynab.PayeeLocationsApi(api_client)
    plan_id = 'plan_id_example' # str | The id of the plan. \"last-used\" can be used to specify the last used plan and \"default\" can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan).

    try:
        # Get all payee locations
        api_response = api_instance.get_payee_locations(plan_id)
        print("The response of PayeeLocationsApi->get_payee_locations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayeeLocationsApi->get_payee_locations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_id** | **str**| The id of the plan. \&quot;last-used\&quot; can be used to specify the last used plan and \&quot;default\&quot; can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan). | 

### Return type

[**PayeeLocationsResponse**](PayeeLocationsResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of payee locations |  -  |
**404** | No payees locations were found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payee_locations_by_payee**
> PayeeLocationsResponse get_payee_locations_by_payee(plan_id, payee_id)

Get all locations for a payee

Returns all payee locations for a specified payee

### Example

* Bearer Authentication (bearer):

```python
import ynab
from ynab.models.payee_locations_response import PayeeLocationsResponse
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
    api_instance = ynab.PayeeLocationsApi(api_client)
    plan_id = 'plan_id_example' # str | The id of the plan. \"last-used\" can be used to specify the last used plan and \"default\" can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan).
    payee_id = 'payee_id_example' # str | id of payee

    try:
        # Get all locations for a payee
        api_response = api_instance.get_payee_locations_by_payee(plan_id, payee_id)
        print("The response of PayeeLocationsApi->get_payee_locations_by_payee:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayeeLocationsApi->get_payee_locations_by_payee: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_id** | **str**| The id of the plan. \&quot;last-used\&quot; can be used to specify the last used plan and \&quot;default\&quot; can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan). | 
 **payee_id** | **str**| id of payee | 

### Return type

[**PayeeLocationsResponse**](PayeeLocationsResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of requested payee locations |  -  |
**404** | No payees locations were found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

