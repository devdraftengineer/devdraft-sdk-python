# devdraft_ai_sdk.LiquidationAddressesApi

All URIs are relative to *https://api.devdraft.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**liquidation_address_controller_create_liquidation_address**](LiquidationAddressesApi.md#liquidation_address_controller_create_liquidation_address) | **POST** /api/v0/customers/{customerId}/liquidation_addresses | Create a new liquidation address for a customer
[**liquidation_address_controller_get_liquidation_address**](LiquidationAddressesApi.md#liquidation_address_controller_get_liquidation_address) | **GET** /api/v0/customers/{customerId}/liquidation_addresses/{liquidationAddressId} | Get a specific liquidation address
[**liquidation_address_controller_get_liquidation_addresses**](LiquidationAddressesApi.md#liquidation_address_controller_get_liquidation_addresses) | **GET** /api/v0/customers/{customerId}/liquidation_addresses | Get all liquidation addresses for a customer

# **liquidation_address_controller_create_liquidation_address**
> LiquidationAddressResponseDto liquidation_address_controller_create_liquidation_address(body, customer_id)

Create a new liquidation address for a customer

       Create a new liquidation address for a customer. Liquidation addresses allow        customers to automatically liquidate cryptocurrency holdings to fiat or other        stablecoins based on configured parameters.        **Required fields:**       - chain: Blockchain network (ethereum, polygon, arbitrum, base)       - currency: Stablecoin currency (usdc, eurc, dai, pyusd, usdt)       - address: Valid blockchain address        **At least one destination must be specified:**       - external_account_id: External bank account       - prefunded_account_id: Developer's prefunded account       - bridge_wallet_id: Bridge wallet       - destination_address: Crypto wallet address        **Payment Rails:**       Different payment rails have different requirements:       - ACH: Requires external_account_id, supports destination_ach_reference       - SEPA: Requires external_account_id, supports destination_sepa_reference       - Wire: Requires external_account_id, supports destination_wire_message       - Crypto: Requires destination_address, supports destination_blockchain_memo     

### Example
```python
from __future__ import print_function
import time
import devdraft_ai_sdk
from devdraft_ai_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = devdraft_ai_sdk.LiquidationAddressesApi()
body = devdraft_ai_sdk.CreateLiquidationAddressDto() # CreateLiquidationAddressDto | 
customer_id = 'customer_id_example' # str | Unique identifier for the customer

try:
    # Create a new liquidation address for a customer
    api_response = api_instance.liquidation_address_controller_create_liquidation_address(body, customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LiquidationAddressesApi->liquidation_address_controller_create_liquidation_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateLiquidationAddressDto**](CreateLiquidationAddressDto.md)|  | 
 **customer_id** | **str**| Unique identifier for the customer | 

### Return type

[**LiquidationAddressResponseDto**](LiquidationAddressResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **liquidation_address_controller_get_liquidation_address**
> LiquidationAddressResponseDto liquidation_address_controller_get_liquidation_address(customer_id, liquidation_address_id)

Get a specific liquidation address

Retrieve a specific liquidation address by its ID for a given customer.

### Example
```python
from __future__ import print_function
import time
import devdraft_ai_sdk
from devdraft_ai_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = devdraft_ai_sdk.LiquidationAddressesApi()
customer_id = 'customer_id_example' # str | Unique identifier for the customer
liquidation_address_id = 'liquidation_address_id_example' # str | Unique identifier for the liquidation address

try:
    # Get a specific liquidation address
    api_response = api_instance.liquidation_address_controller_get_liquidation_address(customer_id, liquidation_address_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LiquidationAddressesApi->liquidation_address_controller_get_liquidation_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| Unique identifier for the customer | 
 **liquidation_address_id** | **str**| Unique identifier for the liquidation address | 

### Return type

[**LiquidationAddressResponseDto**](LiquidationAddressResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **liquidation_address_controller_get_liquidation_addresses**
> list[LiquidationAddressResponseDto] liquidation_address_controller_get_liquidation_addresses(customer_id)

Get all liquidation addresses for a customer

Retrieve all liquidation addresses associated with a specific customer.

### Example
```python
from __future__ import print_function
import time
import devdraft_ai_sdk
from devdraft_ai_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = devdraft_ai_sdk.LiquidationAddressesApi()
customer_id = 'customer_id_example' # str | Unique identifier for the customer

try:
    # Get all liquidation addresses for a customer
    api_response = api_instance.liquidation_address_controller_get_liquidation_addresses(customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LiquidationAddressesApi->liquidation_address_controller_get_liquidation_addresses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| Unique identifier for the customer | 

### Return type

[**list[LiquidationAddressResponseDto]**](LiquidationAddressResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

