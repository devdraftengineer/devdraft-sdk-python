# coding: utf-8

"""
    Devdraft Payment & Business Management API

     A comprehensive payment processing and business management API that enables seamless integration of cryptocurrency and traditional payment methods.       # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class CreateProductDto(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'description': 'str',
        'price': 'float',
        'currency': 'str',
        'type': 'str',
        'weight': 'float',
        'unit': 'str',
        'quantity': 'float',
        'stock_count': 'float',
        'status': 'str',
        'product_type': 'str',
        'images': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'price': 'price',
        'currency': 'currency',
        'type': 'type',
        'weight': 'weight',
        'unit': 'unit',
        'quantity': 'quantity',
        'stock_count': 'stockCount',
        'status': 'status',
        'product_type': 'productType',
        'images': 'images'
    }

    def __init__(self, name=None, description=None, price=None, currency='USD', type=None, weight=None, unit=None, quantity=None, stock_count=None, status=None, product_type=None, images=None):  # noqa: E501
        """CreateProductDto - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._description = None
        self._price = None
        self._currency = None
        self._type = None
        self._weight = None
        self._unit = None
        self._quantity = None
        self._stock_count = None
        self._status = None
        self._product_type = None
        self._images = None
        self.discriminator = None
        self.name = name
        self.description = description
        self.price = price
        if currency is not None:
            self.currency = currency
        if type is not None:
            self.type = type
        if weight is not None:
            self.weight = weight
        if unit is not None:
            self.unit = unit
        if quantity is not None:
            self.quantity = quantity
        if stock_count is not None:
            self.stock_count = stock_count
        if status is not None:
            self.status = status
        if product_type is not None:
            self.product_type = product_type
        if images is not None:
            self.images = images

    @property
    def name(self):
        """Gets the name of this CreateProductDto.  # noqa: E501

        Product name as it will appear to customers. Should be clear and descriptive.  # noqa: E501

        :return: The name of this CreateProductDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateProductDto.

        Product name as it will appear to customers. Should be clear and descriptive.  # noqa: E501

        :param name: The name of this CreateProductDto.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this CreateProductDto.  # noqa: E501

        Detailed description of the product. Supports markdown formatting for rich text display.  # noqa: E501

        :return: The description of this CreateProductDto.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateProductDto.

        Detailed description of the product. Supports markdown formatting for rich text display.  # noqa: E501

        :param description: The description of this CreateProductDto.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def price(self):
        """Gets the price of this CreateProductDto.  # noqa: E501

        Product price in the specified currency. Must be greater than 0.  # noqa: E501

        :return: The price of this CreateProductDto.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this CreateProductDto.

        Product price in the specified currency. Must be greater than 0.  # noqa: E501

        :param price: The price of this CreateProductDto.  # noqa: E501
        :type: float
        """
        if price is None:
            raise ValueError("Invalid value for `price`, must not be `None`")  # noqa: E501

        self._price = price

    @property
    def currency(self):
        """Gets the currency of this CreateProductDto.  # noqa: E501

        Currency code for the price. Defaults to USD if not specified.  # noqa: E501

        :return: The currency of this CreateProductDto.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this CreateProductDto.

        Currency code for the price. Defaults to USD if not specified.  # noqa: E501

        :param currency: The currency of this CreateProductDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["USD", "EUR", "GBP", "CAD", "AUD", "JPY"]  # noqa: E501
        if currency not in allowed_values:
            raise ValueError(
                "Invalid value for `currency` ({0}), must be one of {1}"  # noqa: E501
                .format(currency, allowed_values)
            )

        self._currency = currency

    @property
    def type(self):
        """Gets the type of this CreateProductDto.  # noqa: E501

        Product type  # noqa: E501

        :return: The type of this CreateProductDto.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreateProductDto.

        Product type  # noqa: E501

        :param type: The type of this CreateProductDto.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def weight(self):
        """Gets the weight of this CreateProductDto.  # noqa: E501

        Weight of the product  # noqa: E501

        :return: The weight of this CreateProductDto.  # noqa: E501
        :rtype: float
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this CreateProductDto.

        Weight of the product  # noqa: E501

        :param weight: The weight of this CreateProductDto.  # noqa: E501
        :type: float
        """

        self._weight = weight

    @property
    def unit(self):
        """Gets the unit of this CreateProductDto.  # noqa: E501

        Unit of measurement  # noqa: E501

        :return: The unit of this CreateProductDto.  # noqa: E501
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this CreateProductDto.

        Unit of measurement  # noqa: E501

        :param unit: The unit of this CreateProductDto.  # noqa: E501
        :type: str
        """

        self._unit = unit

    @property
    def quantity(self):
        """Gets the quantity of this CreateProductDto.  # noqa: E501

        Quantity available  # noqa: E501

        :return: The quantity of this CreateProductDto.  # noqa: E501
        :rtype: float
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this CreateProductDto.

        Quantity available  # noqa: E501

        :param quantity: The quantity of this CreateProductDto.  # noqa: E501
        :type: float
        """

        self._quantity = quantity

    @property
    def stock_count(self):
        """Gets the stock_count of this CreateProductDto.  # noqa: E501

        Stock count  # noqa: E501

        :return: The stock_count of this CreateProductDto.  # noqa: E501
        :rtype: float
        """
        return self._stock_count

    @stock_count.setter
    def stock_count(self, stock_count):
        """Sets the stock_count of this CreateProductDto.

        Stock count  # noqa: E501

        :param stock_count: The stock_count of this CreateProductDto.  # noqa: E501
        :type: float
        """

        self._stock_count = stock_count

    @property
    def status(self):
        """Gets the status of this CreateProductDto.  # noqa: E501

        Product status  # noqa: E501

        :return: The status of this CreateProductDto.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CreateProductDto.

        Product status  # noqa: E501

        :param status: The status of this CreateProductDto.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def product_type(self):
        """Gets the product_type of this CreateProductDto.  # noqa: E501

        Product type  # noqa: E501

        :return: The product_type of this CreateProductDto.  # noqa: E501
        :rtype: str
        """
        return self._product_type

    @product_type.setter
    def product_type(self, product_type):
        """Sets the product_type of this CreateProductDto.

        Product type  # noqa: E501

        :param product_type: The product_type of this CreateProductDto.  # noqa: E501
        :type: str
        """

        self._product_type = product_type

    @property
    def images(self):
        """Gets the images of this CreateProductDto.  # noqa: E501

        Array of image URLs  # noqa: E501

        :return: The images of this CreateProductDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._images

    @images.setter
    def images(self, images):
        """Sets the images of this CreateProductDto.

        Array of image URLs  # noqa: E501

        :param images: The images of this CreateProductDto.  # noqa: E501
        :type: list[str]
        """

        self._images = images

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(CreateProductDto, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateProductDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
