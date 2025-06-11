# CreateStablePaymentIntentDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_currency** | **AllOfCreateStablePaymentIntentDtoSourceCurrency** | The stablecoin currency to convert FROM. This is the currency the customer will pay with. | 
**source_network** | **AllOfCreateStablePaymentIntentDtoSourceNetwork** | The blockchain network where the source currency resides. Determines gas fees and transaction speed. | 
**destination_currency** | **AllOfCreateStablePaymentIntentDtoDestinationCurrency** | The stablecoin currency to convert TO. If omitted, defaults to the same as source currency (cross-chain transfer). | [optional] 
**destination_network** | **AllOfCreateStablePaymentIntentDtoDestinationNetwork** | The blockchain network where the converted currency will be delivered. Must support the destination currency. | 
**destination_address** | **str** | The wallet address where converted funds will be sent. Supports Ethereum (0x...) and Solana address formats. | [optional] 
**amount** | **str** | Payment amount in the source currency. Omit for flexible amount payments where users specify the amount during checkout. | [optional] 
**customer_first_name** | **str** | Customer&#x27;s first name. Used for transaction records and compliance. Required for amounts over $1000. | [optional] 
**customer_last_name** | **str** | Customer&#x27;s last name. Used for transaction records and compliance. Required for amounts over $1000. | [optional] 
**customer_email** | **str** | Customer&#x27;s email address. Used for transaction notifications and receipts. Highly recommended for all transactions. | [optional] 
**customer_address** | **str** | Customer&#x27;s full address. Required for compliance in certain jurisdictions and high-value transactions. | [optional] 
**customer_country** | **str** | Customer&#x27;s country of residence. Used for compliance and tax reporting. | [optional] 
**customer_country_iso** | **str** | Customer&#x27;s country ISO 3166-1 alpha-2 code. Used for automated compliance checks. | [optional] 
**customer_province** | **str** | Customer&#x27;s state or province. Required for US and Canadian customers. | [optional] 
**customer_province_iso** | **str** | Customer&#x27;s state or province ISO code. Used for automated tax calculations. | [optional] 
**phone_number** | **str** | Customer&#x27;s phone number with country code. Used for SMS notifications and verification. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

