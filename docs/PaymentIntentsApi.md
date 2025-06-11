# devdraft_ai_sdk.PaymentIntentsApi

All URIs are relative to *https://api.devdraft.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**payment_intent_controller_create_bank_payment_intent**](PaymentIntentsApi.md#payment_intent_controller_create_bank_payment_intent) | **POST** /api/v0/payment-intents/bank | Create a bank payment intent
[**payment_intent_controller_create_stable_payment_intent**](PaymentIntentsApi.md#payment_intent_controller_create_stable_payment_intent) | **POST** /api/v0/payment-intents/stablecoin | Create a stable payment intent

# **payment_intent_controller_create_bank_payment_intent**
> payment_intent_controller_create_bank_payment_intent(body, idempotency_key)

Create a bank payment intent

Creates a new bank payment intent for fiat-to-stablecoin transfers.      This endpoint allows you to create payment intents for bank transfers (ACH, Wire, SEPA) that convert to stablecoins. Perfect for onboarding users from traditional banking to crypto.  ## Supported Payment Rails - **ACH_PUSH**: US bank transfers (same-day or standard) - **WIRE**: International wire transfers - **SEPA**: European bank transfers  ## Use Cases - USD bank account to USDC conversion - EUR bank account to EURC conversion - MXN bank account to stablecoin conversion - Flexible amount payment intents for variable pricing  ## Supported Source Currencies - **USD**: US Dollar - **EUR**: Euro - **MXN**: Mexican Peso  ## Example: USD Bank to USDC ```json {   \"sourcePaymentRail\": \"ach_push\",   \"sourceCurrency\": \"usd\",   \"destinationCurrency\": \"usdc\",   \"destinationNetwork\": \"ethereum\",   \"destinationAddress\": \"0x742d35Cc6634C0532925a3b8D4C9db96c4b4d8e1\",   \"amount\": \"1000.00\",   \"customer_first_name\": \"John\",   \"customer_last_name\": \"Doe\",   \"customer_email\": \"john.doe@example.com\",   \"ach_reference\": \"INV12345\" } ```  ## Reference Fields Use appropriate reference fields based on the payment rail: - `ach_reference`: For ACH transfers (max 10 chars, alphanumeric + spaces) - `wire_message`: For wire transfers (max 256 chars) - `sepa_reference`: For SEPA transfers (6-140 chars, specific character set)  ## Idempotency Include an `idempotency-key` header with a unique UUID v4 to prevent duplicate payments. Subsequent requests with the same key will return the original response.

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
api_instance = devdraft_ai_sdk.PaymentIntentsApi(devdraft_ai_sdk.ApiClient(configuration))
body = devdraft_ai_sdk.CreateBankPaymentIntentDto() # CreateBankPaymentIntentDto | Bank payment intent creation data
idempotency_key = 'idempotency_key_example' # str | Unique UUID v4 for idempotent requests. Prevents duplicate payments.

try:
    # Create a bank payment intent
    api_instance.payment_intent_controller_create_bank_payment_intent(body, idempotency_key)
except ApiException as e:
    print("Exception when calling PaymentIntentsApi->payment_intent_controller_create_bank_payment_intent: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateBankPaymentIntentDto**](CreateBankPaymentIntentDto.md)| Bank payment intent creation data | 
 **idempotency_key** | **str**| Unique UUID v4 for idempotent requests. Prevents duplicate payments. | 

### Return type

void (empty response body)

### Authorization

[x-client-key](../README.md#x-client-key), [x-client-secret](../README.md#x-client-secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payment_intent_controller_create_stable_payment_intent**
> payment_intent_controller_create_stable_payment_intent(body, idempotency_key)

Create a stable payment intent

Creates a new stable payment intent for stablecoin-to-stablecoin transfers.      This endpoint allows you to create payment intents for transfers between different stablecoins and networks. Perfect for cross-chain stablecoin swaps and conversions.  ## Use Cases - USDC to EURC conversions - Cross-chain stablecoin transfers (e.g., Ethereum USDC to Polygon USDC) - Flexible amount payment intents for dynamic pricing  ## Example: USDC to EURC Conversion ```json {   \"sourceCurrency\": \"usdc\",   \"sourceNetwork\": \"ethereum\",   \"destinationCurrency\": \"eurc\",   \"destinationNetwork\": \"polygon\",   \"destinationAddress\": \"0x742d35Cc6634C0532925a3b8D4C9db96c4b4d8e1\",   \"amount\": \"100.00\",   \"customer_first_name\": \"John\",   \"customer_last_name\": \"Doe\",   \"customer_email\": \"john.doe@example.com\" } ```  ## Flexible Amount Payments Omit the `amount` field to create a flexible payment intent where users can specify the amount during payment.  ## Idempotency Include an `idempotency-key` header with a unique UUID v4 to prevent duplicate payments. Subsequent requests with the same key will return the original response.

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
api_instance = devdraft_ai_sdk.PaymentIntentsApi(devdraft_ai_sdk.ApiClient(configuration))
body = devdraft_ai_sdk.CreateStablePaymentIntentDto() # CreateStablePaymentIntentDto | Stable payment intent creation data
idempotency_key = 'idempotency_key_example' # str | Unique UUID v4 for idempotent requests. Prevents duplicate payments.

try:
    # Create a stable payment intent
    api_instance.payment_intent_controller_create_stable_payment_intent(body, idempotency_key)
except ApiException as e:
    print("Exception when calling PaymentIntentsApi->payment_intent_controller_create_stable_payment_intent: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateStablePaymentIntentDto**](CreateStablePaymentIntentDto.md)| Stable payment intent creation data | 
 **idempotency_key** | **str**| Unique UUID v4 for idempotent requests. Prevents duplicate payments. | 

### Return type

void (empty response body)

### Authorization

[x-client-key](../README.md#x-client-key), [x-client-secret](../README.md#x-client-secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

