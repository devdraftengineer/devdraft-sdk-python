# devdraft_ai_sdk.AppBalancesApi

All URIs are relative to *https://api.devdraft.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**balance_controller_get_all_balances**](AppBalancesApi.md#balance_controller_get_all_balances) | **GET** /api/v0/balance | Get all stablecoin balances for an app
[**balance_controller_get_eurc_balance**](AppBalancesApi.md#balance_controller_get_eurc_balance) | **GET** /api/v0/balance/eurc | Get EURC balance for an app
[**balance_controller_get_usdc_balance**](AppBalancesApi.md#balance_controller_get_usdc_balance) | **GET** /api/v0/balance/usdc | Get USDC balance for an app

# **balance_controller_get_all_balances**
> AllBalancesResponse balance_controller_get_all_balances()

Get all stablecoin balances for an app

Retrieves both USDC and EURC balances across all wallets for the specified app.      This comprehensive endpoint provides: - Complete USDC balance aggregation with detailed breakdown - Complete EURC balance aggregation with detailed breakdown - Total USD equivalent value across both currencies - Individual wallet and chain-specific balance details  ## Use Cases - Complete financial dashboard overview - Multi-currency balance reporting - Comprehensive wallet management - Cross-currency analytics and reporting  ## Response Format The response includes separate aggregations for each currency plus a combined USD value estimate, providing complete visibility into stablecoin holdings.

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
api_instance = devdraft_ai_sdk.AppBalancesApi(devdraft_ai_sdk.ApiClient(configuration))

try:
    # Get all stablecoin balances for an app
    api_response = api_instance.balance_controller_get_all_balances()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppBalancesApi->balance_controller_get_all_balances: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AllBalancesResponse**](AllBalancesResponse.md)

### Authorization

[x-client-key](../README.md#x-client-key), [x-client-secret](../README.md#x-client-secret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **balance_controller_get_eurc_balance**
> AggregatedBalanceResponse balance_controller_get_eurc_balance()

Get EURC balance for an app

Retrieves the total EURC balance across all wallets for the specified app.      This endpoint aggregates EURC balances from all associated wallets and provides: - Total EURC balance across all chains and wallets - Detailed breakdown by individual wallet and blockchain network - Contract addresses and wallet identifiers for each balance  ## Use Cases - Dashboard balance display - European market operations - Euro-denominated financial reporting - Cross-currency balance tracking  ## Response Format The response includes both the aggregated total and detailed breakdown, enabling comprehensive euro stablecoin balance management.

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
api_instance = devdraft_ai_sdk.AppBalancesApi(devdraft_ai_sdk.ApiClient(configuration))

try:
    # Get EURC balance for an app
    api_response = api_instance.balance_controller_get_eurc_balance()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppBalancesApi->balance_controller_get_eurc_balance: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AggregatedBalanceResponse**](AggregatedBalanceResponse.md)

### Authorization

[x-client-key](../README.md#x-client-key), [x-client-secret](../README.md#x-client-secret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **balance_controller_get_usdc_balance**
> AggregatedBalanceResponse balance_controller_get_usdc_balance()

Get USDC balance for an app

Retrieves the total USDC balance across all wallets for the specified app.      This endpoint aggregates USDC balances from all associated wallets and provides: - Total USDC balance across all chains and wallets - Detailed breakdown by individual wallet and blockchain network - Contract addresses and wallet identifiers for each balance  ## Use Cases - Dashboard balance display - Financial reporting and reconciliation - Real-time balance monitoring - Multi-chain balance aggregation  ## Response Format The response includes both the aggregated total and detailed breakdown, allowing for comprehensive balance tracking and wallet-specific analysis.

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
api_instance = devdraft_ai_sdk.AppBalancesApi(devdraft_ai_sdk.ApiClient(configuration))

try:
    # Get USDC balance for an app
    api_response = api_instance.balance_controller_get_usdc_balance()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppBalancesApi->balance_controller_get_usdc_balance: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AggregatedBalanceResponse**](AggregatedBalanceResponse.md)

### Authorization

[x-client-key](../README.md#x-client-key), [x-client-secret](../README.md#x-client-secret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

