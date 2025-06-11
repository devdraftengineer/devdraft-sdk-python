# devdraft_ai_sdk.PaymentLinksApi

All URIs are relative to *https://api.devdraft.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**payment_links_controller_create**](PaymentLinksApi.md#payment_links_controller_create) | **POST** /api/v0/payment-links | Create a new payment link
[**payment_links_controller_find_all**](PaymentLinksApi.md#payment_links_controller_find_all) | **GET** /api/v0/payment-links | Get all payment links
[**payment_links_controller_find_one**](PaymentLinksApi.md#payment_links_controller_find_one) | **GET** /api/v0/payment-links/{id} | Get a payment link by ID
[**payment_links_controller_update**](PaymentLinksApi.md#payment_links_controller_update) | **PUT** /api/v0/payment-links/{id} | Update a payment link

# **payment_links_controller_create**
> payment_links_controller_create(body)

Create a new payment link

Creates a new payment link with the provided details. Supports both simple one-time payments and complex product bundles.

### Example
```python
from __future__ import print_function
import time
import devdraft_ai_sdk
from devdraft_ai_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: x-client-key
configuration = devdraft_ai_sdk.Configuration()
configuration.api_key['x-client-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-client-key'] = 'Bearer'
# Configure API key authorization: x-client-secret
configuration = devdraft_ai_sdk.Configuration()
configuration.api_key['x-client-secret'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-client-secret'] = 'Bearer'

# create an instance of the API class
api_instance = devdraft_ai_sdk.PaymentLinksApi(devdraft_ai_sdk.ApiClient(configuration))
body = devdraft_ai_sdk.CreatePaymentLinkDto() # CreatePaymentLinkDto | Payment link creation data

try:
    # Create a new payment link
    api_instance.payment_links_controller_create(body)
except ApiException as e:
    print("Exception when calling PaymentLinksApi->payment_links_controller_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreatePaymentLinkDto**](CreatePaymentLinkDto.md)| Payment link creation data | 

### Return type

void (empty response body)

### Authorization

[x-client-key](../README.md#x-client-key), [x-client-secret](../README.md#x-client-secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payment_links_controller_find_all**
> payment_links_controller_find_all(skip=skip, take=take)

Get all payment links

### Example
```python
from __future__ import print_function
import time
import devdraft_ai_sdk
from devdraft_ai_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: x-client-key
configuration = devdraft_ai_sdk.Configuration()
configuration.api_key['x-client-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-client-key'] = 'Bearer'
# Configure API key authorization: x-client-secret
configuration = devdraft_ai_sdk.Configuration()
configuration.api_key['x-client-secret'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-client-secret'] = 'Bearer'

# create an instance of the API class
api_instance = devdraft_ai_sdk.PaymentLinksApi(devdraft_ai_sdk.ApiClient(configuration))
skip = 'skip_example' # str | Number of records to skip (must be non-negative) (optional)
take = 'take_example' # str | Number of records to take (must be positive) (optional)

try:
    # Get all payment links
    api_instance.payment_links_controller_find_all(skip=skip, take=take)
except ApiException as e:
    print("Exception when calling PaymentLinksApi->payment_links_controller_find_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **str**| Number of records to skip (must be non-negative) | [optional] 
 **take** | **str**| Number of records to take (must be positive) | [optional] 

### Return type

void (empty response body)

### Authorization

[x-client-key](../README.md#x-client-key), [x-client-secret](../README.md#x-client-secret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payment_links_controller_find_one**
> payment_links_controller_find_one(id)

Get a payment link by ID

### Example
```python
from __future__ import print_function
import time
import devdraft_ai_sdk
from devdraft_ai_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: x-client-key
configuration = devdraft_ai_sdk.Configuration()
configuration.api_key['x-client-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-client-key'] = 'Bearer'
# Configure API key authorization: x-client-secret
configuration = devdraft_ai_sdk.Configuration()
configuration.api_key['x-client-secret'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-client-secret'] = 'Bearer'

# create an instance of the API class
api_instance = devdraft_ai_sdk.PaymentLinksApi(devdraft_ai_sdk.ApiClient(configuration))
id = 'id_example' # str | Payment Link ID

try:
    # Get a payment link by ID
    api_instance.payment_links_controller_find_one(id)
except ApiException as e:
    print("Exception when calling PaymentLinksApi->payment_links_controller_find_one: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Payment Link ID | 

### Return type

void (empty response body)

### Authorization

[x-client-key](../README.md#x-client-key), [x-client-secret](../README.md#x-client-secret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payment_links_controller_update**
> payment_links_controller_update(body, id)

Update a payment link

### Example
```python
from __future__ import print_function
import time
import devdraft_ai_sdk
from devdraft_ai_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: x-client-key
configuration = devdraft_ai_sdk.Configuration()
configuration.api_key['x-client-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-client-key'] = 'Bearer'
# Configure API key authorization: x-client-secret
configuration = devdraft_ai_sdk.Configuration()
configuration.api_key['x-client-secret'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-client-secret'] = 'Bearer'

# create an instance of the API class
api_instance = devdraft_ai_sdk.PaymentLinksApi(devdraft_ai_sdk.ApiClient(configuration))
body = devdraft_ai_sdk.UpdatePaymentLinkDto() # UpdatePaymentLinkDto | 
id = 'id_example' # str | Payment Link ID

try:
    # Update a payment link
    api_instance.payment_links_controller_update(body, id)
except ApiException as e:
    print("Exception when calling PaymentLinksApi->payment_links_controller_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdatePaymentLinkDto**](UpdatePaymentLinkDto.md)|  | 
 **id** | **str**| Payment Link ID | 

### Return type

void (empty response body)

### Authorization

[x-client-key](../README.md#x-client-key), [x-client-secret](../README.md#x-client-secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

