# devdraft_ai_sdk.TaxesApi

All URIs are relative to *https://api.devdraft.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tax_controller_create**](TaxesApi.md#tax_controller_create) | **POST** /api/v0/taxes | Create a new tax
[**tax_controller_find_all**](TaxesApi.md#tax_controller_find_all) | **GET** /api/v0/taxes | Get all taxes
[**tax_controller_find_one**](TaxesApi.md#tax_controller_find_one) | **GET** /api/v0/taxes/{id} | Get a tax by ID
[**tax_controller_remove**](TaxesApi.md#tax_controller_remove) | **DELETE** /api/v0/taxes/{id} | Delete a tax
[**tax_controller_update**](TaxesApi.md#tax_controller_update) | **PUT** /api/v0/taxes/{id} | Update a tax

# **tax_controller_create**
> tax_controller_create(body)

Create a new tax

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
api_instance = devdraft_ai_sdk.TaxesApi(devdraft_ai_sdk.ApiClient(configuration))
body = devdraft_ai_sdk.CreateTaxInput() # CreateTaxInput | 

try:
    # Create a new tax
    api_instance.tax_controller_create(body)
except ApiException as e:
    print("Exception when calling TaxesApi->tax_controller_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateTaxInput**](CreateTaxInput.md)|  | 

### Return type

void (empty response body)

### Authorization

[x-client-key](../README.md#x-client-key), [x-client-secret](../README.md#x-client-secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tax_controller_find_all**
> tax_controller_find_all(skip=skip, take=take)

Get all taxes

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
api_instance = devdraft_ai_sdk.TaxesApi(devdraft_ai_sdk.ApiClient(configuration))
skip = 'skip_example' # str | Number of records to skip (optional)
take = 'take_example' # str | Number of records to take (optional)

try:
    # Get all taxes
    api_instance.tax_controller_find_all(skip=skip, take=take)
except ApiException as e:
    print("Exception when calling TaxesApi->tax_controller_find_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **str**| Number of records to skip | [optional] 
 **take** | **str**| Number of records to take | [optional] 

### Return type

void (empty response body)

### Authorization

[x-client-key](../README.md#x-client-key), [x-client-secret](../README.md#x-client-secret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tax_controller_find_one**
> tax_controller_find_one(id)

Get a tax by ID

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
api_instance = devdraft_ai_sdk.TaxesApi(devdraft_ai_sdk.ApiClient(configuration))
id = 'id_example' # str | Tax ID

try:
    # Get a tax by ID
    api_instance.tax_controller_find_one(id)
except ApiException as e:
    print("Exception when calling TaxesApi->tax_controller_find_one: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Tax ID | 

### Return type

void (empty response body)

### Authorization

[x-client-key](../README.md#x-client-key), [x-client-secret](../README.md#x-client-secret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tax_controller_remove**
> tax_controller_remove(id)

Delete a tax

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
api_instance = devdraft_ai_sdk.TaxesApi(devdraft_ai_sdk.ApiClient(configuration))
id = 'id_example' # str | Tax ID

try:
    # Delete a tax
    api_instance.tax_controller_remove(id)
except ApiException as e:
    print("Exception when calling TaxesApi->tax_controller_remove: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Tax ID | 

### Return type

void (empty response body)

### Authorization

[x-client-key](../README.md#x-client-key), [x-client-secret](../README.md#x-client-secret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tax_controller_update**
> tax_controller_update(body, id)

Update a tax

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
api_instance = devdraft_ai_sdk.TaxesApi(devdraft_ai_sdk.ApiClient(configuration))
body = devdraft_ai_sdk.UpdateTaxInput() # UpdateTaxInput | 
id = 'id_example' # str | Tax ID

try:
    # Update a tax
    api_instance.tax_controller_update(body, id)
except ApiException as e:
    print("Exception when calling TaxesApi->tax_controller_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateTaxInput**](UpdateTaxInput.md)|  | 
 **id** | **str**| Tax ID | 

### Return type

void (empty response body)

### Authorization

[x-client-key](../README.md#x-client-key), [x-client-secret](../README.md#x-client-secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

