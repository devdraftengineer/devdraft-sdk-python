# UpdateProductDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Product name as it will appear to customers. Should be clear and descriptive. | [optional] 
**description** | **str** | Detailed description of the product. Supports markdown formatting for rich text display. | [optional] 
**price** | **float** | Product price in the specified currency. Must be greater than 0. | [optional] 
**currency** | **str** | Currency code for the price. Defaults to USD if not specified. | [optional] [default to 'USD']
**type** | **str** | Product type | [optional] 
**weight** | **float** | Weight of the product | [optional] 
**unit** | **str** | Unit of measurement | [optional] 
**quantity** | **float** | Quantity available | [optional] 
**stock_count** | **float** | Stock count | [optional] 
**status** | **str** | Product status | [optional] 
**product_type** | **str** | Product type | [optional] 
**images** | **list[str]** | Array of image URLs | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

