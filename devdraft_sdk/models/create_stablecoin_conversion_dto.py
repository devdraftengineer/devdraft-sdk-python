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

class CreateStablecoinConversionDto(object):
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
        'wallet_id': 'str',
        'source_network': 'str',
        'source_currency': 'str',
        'destination_currency': 'str',
        'amount': 'float'
    }

    attribute_map = {
        'wallet_id': 'walletId',
        'source_network': 'sourceNetwork',
        'source_currency': 'sourceCurrency',
        'destination_currency': 'destinationCurrency',
        'amount': 'amount'
    }

    def __init__(self, wallet_id=None, source_network=None, source_currency=None, destination_currency=None, amount=None):  # noqa: E501
        """CreateStablecoinConversionDto - a model defined in Swagger"""  # noqa: E501
        self._wallet_id = None
        self._source_network = None
        self._source_currency = None
        self._destination_currency = None
        self._amount = None
        self.discriminator = None
        self.wallet_id = wallet_id
        self.source_network = source_network
        self.source_currency = source_currency
        self.destination_currency = destination_currency
        self.amount = amount

    @property
    def wallet_id(self):
        """Gets the wallet_id of this CreateStablecoinConversionDto.  # noqa: E501

        The ID of the bridge wallet to use  # noqa: E501

        :return: The wallet_id of this CreateStablecoinConversionDto.  # noqa: E501
        :rtype: str
        """
        return self._wallet_id

    @wallet_id.setter
    def wallet_id(self, wallet_id):
        """Sets the wallet_id of this CreateStablecoinConversionDto.

        The ID of the bridge wallet to use  # noqa: E501

        :param wallet_id: The wallet_id of this CreateStablecoinConversionDto.  # noqa: E501
        :type: str
        """
        if wallet_id is None:
            raise ValueError("Invalid value for `wallet_id`, must not be `None`")  # noqa: E501

        self._wallet_id = wallet_id

    @property
    def source_network(self):
        """Gets the source_network of this CreateStablecoinConversionDto.  # noqa: E501

        The source network  # noqa: E501

        :return: The source_network of this CreateStablecoinConversionDto.  # noqa: E501
        :rtype: str
        """
        return self._source_network

    @source_network.setter
    def source_network(self, source_network):
        """Sets the source_network of this CreateStablecoinConversionDto.

        The source network  # noqa: E501

        :param source_network: The source_network of this CreateStablecoinConversionDto.  # noqa: E501
        :type: str
        """
        if source_network is None:
            raise ValueError("Invalid value for `source_network`, must not be `None`")  # noqa: E501

        self._source_network = source_network

    @property
    def source_currency(self):
        """Gets the source_currency of this CreateStablecoinConversionDto.  # noqa: E501

        The source currency  # noqa: E501

        :return: The source_currency of this CreateStablecoinConversionDto.  # noqa: E501
        :rtype: str
        """
        return self._source_currency

    @source_currency.setter
    def source_currency(self, source_currency):
        """Sets the source_currency of this CreateStablecoinConversionDto.

        The source currency  # noqa: E501

        :param source_currency: The source_currency of this CreateStablecoinConversionDto.  # noqa: E501
        :type: str
        """
        if source_currency is None:
            raise ValueError("Invalid value for `source_currency`, must not be `None`")  # noqa: E501

        self._source_currency = source_currency

    @property
    def destination_currency(self):
        """Gets the destination_currency of this CreateStablecoinConversionDto.  # noqa: E501

        The destination currency  # noqa: E501

        :return: The destination_currency of this CreateStablecoinConversionDto.  # noqa: E501
        :rtype: str
        """
        return self._destination_currency

    @destination_currency.setter
    def destination_currency(self, destination_currency):
        """Sets the destination_currency of this CreateStablecoinConversionDto.

        The destination currency  # noqa: E501

        :param destination_currency: The destination_currency of this CreateStablecoinConversionDto.  # noqa: E501
        :type: str
        """
        if destination_currency is None:
            raise ValueError("Invalid value for `destination_currency`, must not be `None`")  # noqa: E501

        self._destination_currency = destination_currency

    @property
    def amount(self):
        """Gets the amount of this CreateStablecoinConversionDto.  # noqa: E501

        The amount to convert  # noqa: E501

        :return: The amount of this CreateStablecoinConversionDto.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this CreateStablecoinConversionDto.

        The amount to convert  # noqa: E501

        :param amount: The amount of this CreateStablecoinConversionDto.  # noqa: E501
        :type: float
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

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
        if issubclass(CreateStablecoinConversionDto, dict):
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
        if not isinstance(other, CreateStablecoinConversionDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
