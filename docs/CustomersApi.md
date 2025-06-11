# devdraft_ai_sdk.CustomersApi

All URIs are relative to *https://api.devdraft.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**customer_controller_create**](CustomersApi.md#customer_controller_create) | **POST** /api/v0/customers | Create a new customer
[**customer_controller_find_all**](CustomersApi.md#customer_controller_find_all) | **GET** /api/v0/customers | Get all customers with filters
[**customer_controller_find_one**](CustomersApi.md#customer_controller_find_one) | **GET** /api/v0/customers/{id} | Get a customer by ID
[**customer_controller_update**](CustomersApi.md#customer_controller_update) | **PATCH** /api/v0/customers/{id} | Update a customer

# **customer_controller_create**
> customer_controller_create(body)

Create a new customer

Creates a new customer in the system with their personal and contact information.      This endpoint allows you to register new customers and store their details for future transactions.  ## Use Cases - Register new customers for payment processing - Store customer information for recurring payments - Maintain customer profiles for transaction history  ## Example: Create New Customer ```json {   \"firstName\": \"John\",   \"lastName\": \"Doe\",   \"email\": \"john.doe@example.com\",   \"phone\": \"+1234567890\",   \"address\": {     \"street\": \"123 Main St\",     \"city\": \"New York\",     \"state\": \"NY\",     \"zipCode\": \"10001\",     \"country\": \"USA\"   } } ```  ## Required Fields - `firstName`: Customer's first name - `lastName`: Customer's last name - `email`: Valid email address (must be unique)  ## Optional Fields - `phone`: Contact phone number - `address`: Complete address information   - `street`: Street address   - `city`: City name   - `state`: State/province   - `zipCode`: Postal/ZIP code   - `country`: Country name

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
api_instance = devdraft_ai_sdk.CustomersApi(devdraft_ai_sdk.ApiClient(configuration))
body = devdraft_ai_sdk.CreateCustomerDto() # CreateCustomerDto | Customer creation data

try:
    # Create a new customer
    api_instance.customer_controller_create(body)
except ApiException as e:
    print("Exception when calling CustomersApi->customer_controller_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateCustomerDto**](CreateCustomerDto.md)| Customer creation data | 

### Return type

void (empty response body)

### Authorization

[x-client-key](../README.md#x-client-key), [x-client-secret](../README.md#x-client-secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customer_controller_find_all**
> customer_controller_find_all(status=status, name=name, email=email, take=take, skip=skip)

Get all customers with filters

Retrieves a list of customers with optional filtering and pagination.      This endpoint allows you to search and filter customers based on various criteria.  ## Use Cases - List all customers with pagination - Search customers by name or email - Filter customers by status - Export customer data  ## Query Parameters - `skip`: Number of records to skip (default: 0) - `take`: Number of records to take (default: 10) - `status`: Filter by customer status (ACTIVE, INACTIVE, SUSPENDED) - `name`: Filter by customer name (partial match) - `email`: Filter by customer email (exact match)  ## Example Response ```json {   \"data\": [     {       \"id\": \"cust_123456\",       \"firstName\": \"John\",       \"lastName\": \"Doe\",       \"email\": \"john.doe@example.com\",       \"status\": \"ACTIVE\",       \"createdAt\": \"2024-03-20T10:00:00Z\"     }   ],   \"total\": 100,   \"skip\": 0,   \"take\": 10 } ```

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
api_instance = devdraft_ai_sdk.CustomersApi(devdraft_ai_sdk.ApiClient(configuration))
status = 'status_example' # str | Filter by customer status (optional)
name = 'name_example' # str | Filter by customer name (optional)
email = 'email_example' # str | Filter by customer email (optional)
take = 1.2 # float | Number of records to take (optional)
skip = 1.2 # float | Number of records to skip (optional)

try:
    # Get all customers with filters
    api_instance.customer_controller_find_all(status=status, name=name, email=email, take=take, skip=skip)
except ApiException as e:
    print("Exception when calling CustomersApi->customer_controller_find_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **str**| Filter by customer status | [optional] 
 **name** | **str**| Filter by customer name | [optional] 
 **email** | **str**| Filter by customer email | [optional] 
 **take** | **float**| Number of records to take | [optional] 
 **skip** | **float**| Number of records to skip | [optional] 

### Return type

void (empty response body)

### Authorization

[x-client-key](../README.md#x-client-key), [x-client-secret](../README.md#x-client-secret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customer_controller_find_one**
> customer_controller_find_one(id)

Get a customer by ID

Retrieves detailed information about a specific customer.      This endpoint allows you to fetch complete customer details including their address and contact information.  ## Use Cases - View customer details - Verify customer information - Update customer records  ## Example Response ```json {   \"id\": \"cust_123456\",   \"firstName\": \"John\",   \"lastName\": \"Doe\",   \"email\": \"john.doe@example.com\",   \"phone\": \"+1234567890\",   \"status\": \"ACTIVE\",   \"address\": {     \"street\": \"123 Main St\",     \"city\": \"New York\",     \"state\": \"NY\",     \"zipCode\": \"10001\",     \"country\": \"USA\"   },   \"createdAt\": \"2024-03-20T10:00:00Z\",   \"updatedAt\": \"2024-03-20T10:00:00Z\" } ```

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
api_instance = devdraft_ai_sdk.CustomersApi(devdraft_ai_sdk.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Get a customer by ID
    api_instance.customer_controller_find_one(id)
except ApiException as e:
    print("Exception when calling CustomersApi->customer_controller_find_one: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[x-client-key](../README.md#x-client-key), [x-client-secret](../README.md#x-client-secret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customer_controller_update**
> customer_controller_update(body, id)

Update a customer

Updates an existing customer's information.      This endpoint allows you to modify customer details while preserving their core information.  ## Use Cases - Update customer contact information - Change customer address - Modify customer status  ## Example Request ```json {   \"firstName\": \"John\",   \"lastName\": \"Smith\",   \"phone\": \"+1987654321\",   \"address\": {     \"street\": \"456 Oak St\",     \"city\": \"Los Angeles\",     \"state\": \"CA\",     \"zipCode\": \"90001\",     \"country\": \"USA\"   } } ```  ## Notes - Only include fields that need to be updated - Email address cannot be changed - Status changes may require additional verification

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
api_instance = devdraft_ai_sdk.CustomersApi(devdraft_ai_sdk.ApiClient(configuration))
body = devdraft_ai_sdk.UpdateCustomerDto() # UpdateCustomerDto | Customer update data
id = 'id_example' # str | 

try:
    # Update a customer
    api_instance.customer_controller_update(body, id)
except ApiException as e:
    print("Exception when calling CustomersApi->customer_controller_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateCustomerDto**](UpdateCustomerDto.md)| Customer update data | 
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[x-client-key](../README.md#x-client-key), [x-client-secret](../README.md#x-client-secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

