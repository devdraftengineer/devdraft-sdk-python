# CreateInvoiceDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the invoice | 
**email** | **str** | Email address | 
**customer_id** | **str** | Customer ID | 
**currency** | **str** | Currency for the invoice | 
**items** | [**list[InvoiceProductDto]**](InvoiceProductDto.md) | Array of products in the invoice | 
**due_date** | **datetime** | Due date of the invoice | 
**delivery** | **str** | Delivery method | 
**payment_link** | **bool** | Whether to generate a payment link | 
**payment_methods** | **list[str]** | Array of accepted payment methods | 
**status** | **str** | Invoice status | 
**address** | **str** | Address | [optional] 
**phone_number** | **str** | Phone number | [optional] 
**send_date** | **datetime** | Send date | [optional] 
**logo** | **str** | Logo URL | [optional] 
**partial_payment** | **bool** | Allow partial payments | 
**tax_id** | **str** | Tax ID | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

