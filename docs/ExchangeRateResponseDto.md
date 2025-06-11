# ExchangeRateResponseDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_from** | **str** | Source currency code (USD for USDC) | 
**to** | **str** | Target currency code (EUR for EURC) | 
**midmarket_rate** | **str** | Mid-market exchange rate from source to target currency | 
**buy_rate** | **str** | Rate for buying target currency (what you get when converting from source to target) | 
**sell_rate** | **str** | Rate for selling target currency (what you pay when converting from target to source) | 
**timestamp** | **str** | Timestamp when the exchange rate was last updated | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

