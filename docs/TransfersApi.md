# devdraft_ai_sdk.TransfersApi

All URIs are relative to *https://api.devdraft.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**transfer_controller_create_direct_bank_transfer**](TransfersApi.md#transfer_controller_create_direct_bank_transfer) | **POST** /api/v0/transfers/direct-bank | Create a direct bank transfer
[**transfer_controller_create_direct_wallet_transfer**](TransfersApi.md#transfer_controller_create_direct_wallet_transfer) | **POST** /api/v0/transfers/direct-wallet | Create a direct wallet transfer
[**transfer_controller_create_stablecoin_conversion**](TransfersApi.md#transfer_controller_create_stablecoin_conversion) | **POST** /api/v0/transfers/stablecoin-conversion | Create a stablecoin conversion

# **transfer_controller_create_direct_bank_transfer**
> transfer_controller_create_direct_bank_transfer(body)

Create a direct bank transfer

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
api_instance = devdraft_ai_sdk.TransfersApi(devdraft_ai_sdk.ApiClient(configuration))
body = devdraft_ai_sdk.CreateDirectBankTransferDto() # CreateDirectBankTransferDto | 

try:
    # Create a direct bank transfer
    api_instance.transfer_controller_create_direct_bank_transfer(body)
except ApiException as e:
    print("Exception when calling TransfersApi->transfer_controller_create_direct_bank_transfer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateDirectBankTransferDto**](CreateDirectBankTransferDto.md)|  | 

### Return type

void (empty response body)

### Authorization

[x-client-key](../README.md#x-client-key), [x-client-secret](../README.md#x-client-secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfer_controller_create_direct_wallet_transfer**
> transfer_controller_create_direct_wallet_transfer(body)

Create a direct wallet transfer

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
api_instance = devdraft_ai_sdk.TransfersApi(devdraft_ai_sdk.ApiClient(configuration))
body = devdraft_ai_sdk.CreateDirectWalletTransferDto() # CreateDirectWalletTransferDto | 

try:
    # Create a direct wallet transfer
    api_instance.transfer_controller_create_direct_wallet_transfer(body)
except ApiException as e:
    print("Exception when calling TransfersApi->transfer_controller_create_direct_wallet_transfer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateDirectWalletTransferDto**](CreateDirectWalletTransferDto.md)|  | 

### Return type

void (empty response body)

### Authorization

[x-client-key](../README.md#x-client-key), [x-client-secret](../README.md#x-client-secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfer_controller_create_stablecoin_conversion**
> transfer_controller_create_stablecoin_conversion(body)

Create a stablecoin conversion

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
api_instance = devdraft_ai_sdk.TransfersApi(devdraft_ai_sdk.ApiClient(configuration))
body = devdraft_ai_sdk.CreateStablecoinConversionDto() # CreateStablecoinConversionDto | 

try:
    # Create a stablecoin conversion
    api_instance.transfer_controller_create_stablecoin_conversion(body)
except ApiException as e:
    print("Exception when calling TransfersApi->transfer_controller_create_stablecoin_conversion: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateStablecoinConversionDto**](CreateStablecoinConversionDto.md)|  | 

### Return type

void (empty response body)

### Authorization

[x-client-key](../README.md#x-client-key), [x-client-secret](../README.md#x-client-secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

