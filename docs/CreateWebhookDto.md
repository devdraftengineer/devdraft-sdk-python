# CreateWebhookDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the webhook for identification purposes | 
**url** | **str** | URL where webhook events will be sent | 
**is_active** | **bool** | Whether the webhook is active and will receive events | [default to True]
**signing_secret** | **str** | Secret key used to sign webhook payloads for verification | [optional] 
**encrypted** | **bool** | Whether webhook payloads should be encrypted | [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

