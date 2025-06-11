# devdraft_ai_sdk.TestPaymentsApi

All URIs are relative to *https://api.devdraft.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**test_payment_controller_create_payment_v0**](TestPaymentsApi.md#test_payment_controller_create_payment_v0) | **POST** /api/v0/test-payment | Process a test payment
[**test_payment_controller_get_payment_v0**](TestPaymentsApi.md#test_payment_controller_get_payment_v0) | **GET** /api/v0/test-payment/{id} | Get payment details by ID
[**test_payment_controller_refund_payment_v0**](TestPaymentsApi.md#test_payment_controller_refund_payment_v0) | **POST** /api/v0/test-payment/{id}/refund | Refund a payment

# **test_payment_controller_create_payment_v0**
> PaymentResponseDto test_payment_controller_create_payment_v0(body, idempotency_key)

Process a test payment

Creates a new payment. Requires an idempotency key to prevent duplicate payments on retry.      ## Idempotency Key Best Practices  1. **Generate unique keys**: Use UUIDs or similar unique identifiers, prefixed with a descriptive operation name 2. **Store keys client-side**: Save the key with the original request so you can retry with the same key 3. **Key format**: Between 6-64 alphanumeric characters 4. **Expiration**: Keys expire after 24 hours by default 5. **Use case**: Perfect for ensuring payment operations are never processed twice, even during network failures  ## Example Request (curl)  ```bash curl -X POST \\   https://api.example.com/rest-api/v0/test-payment \\   -H 'Content-Type: application/json' \\   -H 'Client-Key: your-api-key' \\   -H 'Client-Secret: your-api-secret' \\   -H 'Idempotency-Key: payment_123456_unique_key' \\   -d '{     \"amount\": 100.00,     \"currency\": \"USD\",     \"description\": \"Test payment for order #12345\",     \"customerId\": \"cus_12345\"   }' ```  ## Example Response (First Request)  ```json {   \"id\": \"pay_abc123xyz456\",   \"amount\": 100.00,   \"currency\": \"USD\",   \"status\": \"succeeded\",   \"timestamp\": \"2023-07-01T12:00:00.000Z\" } ```  ## Example Response (Duplicate Request)  The exact same response will be returned for any duplicate request with the same idempotency key, without creating a new payment.  ## Retry Scenario Example  Network failure during payment submission: 1. Client creates payment request with idempotency key: \"payment_123456_unique_key\" 2. Request begins processing, but network connection fails before response received 3. Client retries the exact same request with the same idempotency key 4. Server detects duplicate idempotency key and returns the result of the first request 5. No duplicate payment is created  If you retry with same key but different parameters (e.g., different amount), you'll receive a 409 Conflict error.

### Example
```python
from __future__ import print_function
import time
import devdraft_ai_sdk
from devdraft_ai_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = devdraft_ai_sdk.TestPaymentsApi()
body = devdraft_ai_sdk.PaymentRequestDto() # PaymentRequestDto | 
idempotency_key = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique key to ensure the request is idempotent. If a request with the same key is sent multiple times, only the first will be processed, and subsequent requests will return the same response.

try:
    # Process a test payment
    api_response = api_instance.test_payment_controller_create_payment_v0(body, idempotency_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestPaymentsApi->test_payment_controller_create_payment_v0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PaymentRequestDto**](PaymentRequestDto.md)|  | 
 **idempotency_key** | [**str**](.md)| Unique key to ensure the request is idempotent. If a request with the same key is sent multiple times, only the first will be processed, and subsequent requests will return the same response. | 

### Return type

[**PaymentResponseDto**](PaymentResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_payment_controller_get_payment_v0**
> PaymentResponseDto test_payment_controller_get_payment_v0(id)

Get payment details by ID

### Example
```python
from __future__ import print_function
import time
import devdraft_ai_sdk
from devdraft_ai_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = devdraft_ai_sdk.TestPaymentsApi()
id = 'id_example' # str | Payment ID

try:
    # Get payment details by ID
    api_response = api_instance.test_payment_controller_get_payment_v0(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestPaymentsApi->test_payment_controller_get_payment_v0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Payment ID | 

### Return type

[**PaymentResponseDto**](PaymentResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_payment_controller_refund_payment_v0**
> RefundResponseDto test_payment_controller_refund_payment_v0(id, idempotency_key)

Refund a payment

Refunds an existing payment. Requires an idempotency key to prevent duplicate refunds on retry.      ## Idempotency Key Benefits for Refunds  Refunds are critical financial operations where duplicates can cause serious issues. Using idempotency keys ensures:  1. **Prevent duplicate refunds**: Even if a request times out or fails, retrying with the same key won't issue multiple refunds 2. **Safe retries**: Network failures or timeouts won't risk creating multiple refunds 3. **Consistent response**: Always get the same response for the same operation  ## Example Request (curl)  ```bash curl -X POST \\   https://api.example.com/rest-api/v0/test-payment/pay_abc123xyz456/refund \\   -H 'Content-Type: application/json' \\   -H 'Client-Key: your-api-key' \\   -H 'Client-Secret: your-api-secret' \\   -H 'Idempotency-Key: refund_123456_unique_key' ```  ## Example Response (First Request)  ```json {   \"id\": \"ref_xyz789\",   \"paymentId\": \"pay_abc123xyz456\",   \"amount\": 100.00,   \"status\": \"succeeded\",   \"timestamp\": \"2023-07-01T14:30:00.000Z\" } ```  ## Example Response (Duplicate Request)  The exact same response will be returned for any duplicate request with the same idempotency key, without creating a new refund.  ## Idempotency Key Guidelines  - Use a unique key for each distinct refund operation - Store keys client-side to ensure you can retry with the same key if needed - Keys expire after 24 hours by default

### Example
```python
from __future__ import print_function
import time
import devdraft_ai_sdk
from devdraft_ai_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = devdraft_ai_sdk.TestPaymentsApi()
id = 'id_example' # str | Payment ID to refund
idempotency_key = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique key to ensure the refund request is idempotent. If a request with the same key is sent multiple times, only the first will be processed, and subsequent requests will return the same response.

try:
    # Refund a payment
    api_response = api_instance.test_payment_controller_refund_payment_v0(id, idempotency_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestPaymentsApi->test_payment_controller_refund_payment_v0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Payment ID to refund | 
 **idempotency_key** | [**str**](.md)| Unique key to ensure the refund request is idempotent. If a request with the same key is sent multiple times, only the first will be processed, and subsequent requests will return the same response. | 

### Return type

[**RefundResponseDto**](RefundResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

