# devdraft_ai_sdk.WebhooksApi

All URIs are relative to *https://api.devdraft.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**webhook_controller_create**](WebhooksApi.md#webhook_controller_create) | **POST** /api/v0/webhooks | Create a new webhook
[**webhook_controller_find_all**](WebhooksApi.md#webhook_controller_find_all) | **GET** /api/v0/webhooks | Get all webhooks
[**webhook_controller_find_one**](WebhooksApi.md#webhook_controller_find_one) | **GET** /api/v0/webhooks/{id} | Get a webhook by id
[**webhook_controller_remove**](WebhooksApi.md#webhook_controller_remove) | **DELETE** /api/v0/webhooks/{id} | Delete a webhook
[**webhook_controller_update**](WebhooksApi.md#webhook_controller_update) | **PATCH** /api/v0/webhooks/{id} | Update a webhook

# **webhook_controller_create**
> WebhookResponseDto webhook_controller_create(body)

Create a new webhook

Creates a new webhook endpoint for receiving event notifications. Requires webhook:create scope.

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
api_instance = devdraft_ai_sdk.WebhooksApi(devdraft_ai_sdk.ApiClient(configuration))
body = devdraft_ai_sdk.CreateWebhookDto() # CreateWebhookDto | Webhook configuration details

try:
    # Create a new webhook
    api_response = api_instance.webhook_controller_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->webhook_controller_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateWebhookDto**](CreateWebhookDto.md)| Webhook configuration details | 

### Return type

[**WebhookResponseDto**](WebhookResponseDto.md)

### Authorization

[x-client-key](../README.md#x-client-key), [x-client-secret](../README.md#x-client-secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhook_controller_find_all**
> list[WebhookResponseDto] webhook_controller_find_all(skip=skip, take=take)

Get all webhooks

Retrieves a list of all webhooks for your application. Requires webhook:read scope.

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
api_instance = devdraft_ai_sdk.WebhooksApi(devdraft_ai_sdk.ApiClient(configuration))
skip = 1.2 # float | Number of records to skip (default: 0) (optional)
take = 1.2 # float | Number of records to return (default: 10) (optional)

try:
    # Get all webhooks
    api_response = api_instance.webhook_controller_find_all(skip=skip, take=take)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->webhook_controller_find_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **float**| Number of records to skip (default: 0) | [optional] 
 **take** | **float**| Number of records to return (default: 10) | [optional] 

### Return type

[**list[WebhookResponseDto]**](WebhookResponseDto.md)

### Authorization

[x-client-key](../README.md#x-client-key), [x-client-secret](../README.md#x-client-secret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhook_controller_find_one**
> WebhookResponseDto webhook_controller_find_one(id)

Get a webhook by id

Retrieves details for a specific webhook. Requires webhook:read scope.

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
api_instance = devdraft_ai_sdk.WebhooksApi(devdraft_ai_sdk.ApiClient(configuration))
id = 'id_example' # str | Webhook ID

try:
    # Get a webhook by id
    api_response = api_instance.webhook_controller_find_one(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->webhook_controller_find_one: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Webhook ID | 

### Return type

[**WebhookResponseDto**](WebhookResponseDto.md)

### Authorization

[x-client-key](../README.md#x-client-key), [x-client-secret](../README.md#x-client-secret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhook_controller_remove**
> WebhookResponseDto webhook_controller_remove(id)

Delete a webhook

Deletes a webhook configuration. Requires webhook:delete scope.

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
api_instance = devdraft_ai_sdk.WebhooksApi(devdraft_ai_sdk.ApiClient(configuration))
id = 'id_example' # str | Webhook ID

try:
    # Delete a webhook
    api_response = api_instance.webhook_controller_remove(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->webhook_controller_remove: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Webhook ID | 

### Return type

[**WebhookResponseDto**](WebhookResponseDto.md)

### Authorization

[x-client-key](../README.md#x-client-key), [x-client-secret](../README.md#x-client-secret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhook_controller_update**
> WebhookResponseDto webhook_controller_update(body, id)

Update a webhook

Updates an existing webhook configuration. Requires webhook:update scope.

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
api_instance = devdraft_ai_sdk.WebhooksApi(devdraft_ai_sdk.ApiClient(configuration))
body = devdraft_ai_sdk.UpdateWebhookDto() # UpdateWebhookDto | Webhook update details
id = 'id_example' # str | Webhook ID

try:
    # Update a webhook
    api_response = api_instance.webhook_controller_update(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->webhook_controller_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateWebhookDto**](UpdateWebhookDto.md)| Webhook update details | 
 **id** | **str**| Webhook ID | 

### Return type

[**WebhookResponseDto**](WebhookResponseDto.md)

### Authorization

[x-client-key](../README.md#x-client-key), [x-client-secret](../README.md#x-client-secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

