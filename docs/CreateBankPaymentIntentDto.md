# CreateBankPaymentIntentDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_payment_rail** | **AllOfCreateBankPaymentIntentDtoSourcePaymentRail** | The banking payment method to use for the transfer. Determines processing time and fees. | 
**source_currency** | **AllOfCreateBankPaymentIntentDtoSourceCurrency** | The fiat currency to convert FROM. Must match the currency of the source payment rail. | 
**destination_currency** | **AllOfCreateBankPaymentIntentDtoDestinationCurrency** | The stablecoin currency to convert TO. The customer will receive this currency. | 
**destination_network** | **AllOfCreateBankPaymentIntentDtoDestinationNetwork** | The blockchain network where the stablecoin will be delivered. Must support the destination currency. | 
**destination_address** | **str** | Destination wallet address. Supports Ethereum (0x...) and Solana address formats. | [optional] 
**amount** | **str** | Payment amount (optional for flexible amount) | [optional] 
**customer_first_name** | **str** | Customer first name | [optional] 
**customer_last_name** | **str** | Customer last name | [optional] 
**customer_email** | **str** | Customer email address | [optional] 
**customer_address** | **str** | Customer address | [optional] 
**customer_country** | **str** | Customer country | [optional] 
**customer_country_iso** | **str** | Customer country ISO code | [optional] 
**customer_province** | **str** | Customer province/state | [optional] 
**customer_province_iso** | **str** | Customer province/state ISO code | [optional] 
**phone_number** | **str** | Customer phone number | [optional] 
**wire_message** | **str** | Wire transfer message (for WIRE transfers) | [optional] 
**sepa_reference** | **str** | SEPA reference (for SEPA transfers) | [optional] 
**ach_reference** | **str** | ACH reference (for ACH transfers) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

