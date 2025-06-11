# CreateLiquidationAddressDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chain** | **str** | The blockchain chain for the liquidation address | 
**currency** | **str** | The currency for the liquidation address | 
**address** | **str** | The liquidation address on the blockchain | 
**external_account_id** | **str** | External bank account to send funds to | [optional] 
**prefunded_account_id** | **str** | Developer&#x27;s prefunded account id | [optional] 
**bridge_wallet_id** | **str** | Bridge Wallet to send funds to | [optional] 
**destination_payment_rail** | **AllOfCreateLiquidationAddressDtoDestinationPaymentRail** | Payment rail for sending funds | [optional] 
**destination_currency** | **AllOfCreateLiquidationAddressDtoDestinationCurrency** | Currency for sending funds | [optional] 
**destination_wire_message** | **str** | Message for wire transfers | [optional] 
**destination_sepa_reference** | **str** | Reference for SEPA transactions | [optional] 
**destination_ach_reference** | **str** | Reference for ACH transactions | [optional] 
**destination_address** | **str** | Crypto wallet address for crypto transfers | [optional] 
**destination_blockchain_memo** | **str** | Memo for blockchain transactions | [optional] 
**return_address** | **str** | Address to return funds on failed transactions (Not supported on Stellar) | [optional] 
**custom_developer_fee_percent** | **str** | Custom developer fee percentage (Base 100 percentage: 10.2% &#x3D; \&quot;10.2\&quot;) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

