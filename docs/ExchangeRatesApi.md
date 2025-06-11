# devdraft_ai_sdk.ExchangeRatesApi

All URIs are relative to *https://api.devdraft.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**exchange_rate_controller_get_eurto_usd_rate**](ExchangeRatesApi.md#exchange_rate_controller_get_eurto_usd_rate) | **GET** /api/v0/exchange-rate/eur-to-usd | Get EUR to USD exchange rate
[**exchange_rate_controller_get_exchange_rate**](ExchangeRatesApi.md#exchange_rate_controller_get_exchange_rate) | **GET** /api/v0/exchange-rate | Get exchange rate between specified currencies
[**exchange_rate_controller_get_usdto_eur_rate**](ExchangeRatesApi.md#exchange_rate_controller_get_usdto_eur_rate) | **GET** /api/v0/exchange-rate/usd-to-eur | Get USD to EUR exchange rate

# **exchange_rate_controller_get_eurto_usd_rate**
> ExchangeRateResponseDto exchange_rate_controller_get_eurto_usd_rate()

Get EUR to USD exchange rate

Retrieves the current exchange rate for converting EUR to USD (EURC to USDC).      This endpoint provides real-time exchange rate information for stablecoin conversions: - Mid-market rate for reference pricing - Buy rate for actual conversion calculations - Sell rate for reverse conversion scenarios  ## Use Cases - Display current exchange rates in dashboards - Calculate conversion amounts for EURC to USDC transfers - Financial reporting and analytics - Real-time pricing for multi-currency operations  ## Rate Information - **Mid-market rate**: The theoretical middle rate between buy and sell - **Buy rate**: Rate used when converting FROM EUR TO USD (what you get) - **Sell rate**: Rate used when converting FROM USD TO EUR (what you pay)  The rates are updated in real-time and reflect current market conditions.

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
api_instance = devdraft_ai_sdk.ExchangeRatesApi(devdraft_ai_sdk.ApiClient(configuration))

try:
    # Get EUR to USD exchange rate
    api_response = api_instance.exchange_rate_controller_get_eurto_usd_rate()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExchangeRatesApi->exchange_rate_controller_get_eurto_usd_rate: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ExchangeRateResponseDto**](ExchangeRateResponseDto.md)

### Authorization

[x-client-key](../README.md#x-client-key), [x-client-secret](../README.md#x-client-secret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exchange_rate_controller_get_exchange_rate**
> ExchangeRateResponseDto exchange_rate_controller_get_exchange_rate(_from, to)

Get exchange rate between specified currencies

Retrieves the current exchange rate between two specified currencies.      This flexible endpoint allows you to get exchange rates for any supported currency pair: - Supports USD and EUR currency codes - Provides comprehensive rate information - Real-time market data  ## Supported Currency Pairs - USD to EUR (USDC to EURC) - EUR to USD (EURC to USDC)  ## Query Parameters - **from**: Source currency code (usd, eur) - **to**: Target currency code (usd, eur)  ## Use Cases - Flexible exchange rate queries - Multi-currency application support - Dynamic currency conversion calculations - Financial analytics and reporting  ## Rate Information All rates are provided with full market context including mid-market, buy, and sell rates.

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
api_instance = devdraft_ai_sdk.ExchangeRatesApi(devdraft_ai_sdk.ApiClient(configuration))
_from = '_from_example' # str | Source currency code (e.g., usd)
to = 'to_example' # str | Target currency code (e.g., eur)

try:
    # Get exchange rate between specified currencies
    api_response = api_instance.exchange_rate_controller_get_exchange_rate(_from, to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExchangeRatesApi->exchange_rate_controller_get_exchange_rate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **str**| Source currency code (e.g., usd) | 
 **to** | **str**| Target currency code (e.g., eur) | 

### Return type

[**ExchangeRateResponseDto**](ExchangeRateResponseDto.md)

### Authorization

[x-client-key](../README.md#x-client-key), [x-client-secret](../README.md#x-client-secret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exchange_rate_controller_get_usdto_eur_rate**
> ExchangeRateResponseDto exchange_rate_controller_get_usdto_eur_rate()

Get USD to EUR exchange rate

Retrieves the current exchange rate for converting USD to EUR (USDC to EURC).      This endpoint provides real-time exchange rate information for stablecoin conversions: - Mid-market rate for reference pricing - Buy rate for actual conversion calculations - Sell rate for reverse conversion scenarios  ## Use Cases - Display current exchange rates in dashboards - Calculate conversion amounts for USDC to EURC transfers - Financial reporting and analytics - Real-time pricing for multi-currency operations  ## Rate Information - **Mid-market rate**: The theoretical middle rate between buy and sell - **Buy rate**: Rate used when converting FROM USD TO EUR (what you get) - **Sell rate**: Rate used when converting FROM EUR TO USD (what you pay)  The rates are updated in real-time and reflect current market conditions.

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
api_instance = devdraft_ai_sdk.ExchangeRatesApi(devdraft_ai_sdk.ApiClient(configuration))

try:
    # Get USD to EUR exchange rate
    api_response = api_instance.exchange_rate_controller_get_usdto_eur_rate()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExchangeRatesApi->exchange_rate_controller_get_usdto_eur_rate: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ExchangeRateResponseDto**](ExchangeRateResponseDto.md)

### Authorization

[x-client-key](../README.md#x-client-key), [x-client-secret](../README.md#x-client-secret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

