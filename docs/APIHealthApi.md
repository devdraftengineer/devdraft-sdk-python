# devdraft_ai_sdk.APIHealthApi

All URIs are relative to *https://api.devdraft.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**health_controller_check_v0**](APIHealthApi.md#health_controller_check_v0) | **GET** /api/v0/health | Authenticated health check endpoint
[**health_controller_public_health_check_v0**](APIHealthApi.md#health_controller_public_health_check_v0) | **GET** /api/v0/health/public | Public health check endpoint

# **health_controller_check_v0**
> HealthResponseDto health_controller_check_v0()

Authenticated health check endpoint

### Example
```python
from __future__ import print_function
import time
import devdraft_ai_sdk
from devdraft_ai_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = devdraft_ai_sdk.APIHealthApi()

try:
    # Authenticated health check endpoint
    api_response = api_instance.health_controller_check_v0()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIHealthApi->health_controller_check_v0: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**HealthResponseDto**](HealthResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **health_controller_public_health_check_v0**
> PublicHealthResponseDto health_controller_public_health_check_v0()

Public health check endpoint

### Example
```python
from __future__ import print_function
import time
import devdraft_ai_sdk
from devdraft_ai_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = devdraft_ai_sdk.APIHealthApi()

try:
    # Public health check endpoint
    api_response = api_instance.health_controller_public_health_check_v0()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIHealthApi->health_controller_public_health_check_v0: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PublicHealthResponseDto**](PublicHealthResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

