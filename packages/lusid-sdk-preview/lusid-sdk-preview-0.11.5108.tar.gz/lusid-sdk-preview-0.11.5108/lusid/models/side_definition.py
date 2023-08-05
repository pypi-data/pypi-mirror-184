# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.5108
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from lusid.configuration import Configuration


class SideDefinition(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
      required_map (dict): The key is attribute name
                           and the value is whether it is 'required' or 'optional'.
    """
    openapi_types = {
        'side': 'str',
        'security': 'str',
        'currency': 'str',
        'rate': 'str',
        'units': 'str',
        'amount': 'str',
        'notional_amount': 'str',
        'links': 'list[Link]'
    }

    attribute_map = {
        'side': 'side',
        'security': 'security',
        'currency': 'currency',
        'rate': 'rate',
        'units': 'units',
        'amount': 'amount',
        'notional_amount': 'notionalAmount',
        'links': 'links'
    }

    required_map = {
        'side': 'required',
        'security': 'required',
        'currency': 'required',
        'rate': 'required',
        'units': 'required',
        'amount': 'required',
        'notional_amount': 'optional',
        'links': 'optional'
    }

    def __init__(self, side=None, security=None, currency=None, rate=None, units=None, amount=None, notional_amount=None, links=None, local_vars_configuration=None):  # noqa: E501
        """SideDefinition - a model defined in OpenAPI"
        
        :param side:  A unique label identifying the side definition. (required)
        :type side: str
        :param security:  The field or property key defining the side's security, or instrument. (required)
        :type security: str
        :param currency:  The field or property key defining the side's currency. (required)
        :type currency: str
        :param rate:  The field or property key defining the side's rate. (required)
        :type rate: str
        :param units:  The value, field or property key defining the side's units. (required)
        :type units: str
        :param amount:  The value, field or property key defining the side's amount (required)
        :type amount: str
        :param notional_amount:  The value, field or property key defining the side's notional amount
        :type notional_amount: str
        :param links:  Collection of links.
        :type links: list[lusid.Link]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._side = None
        self._security = None
        self._currency = None
        self._rate = None
        self._units = None
        self._amount = None
        self._notional_amount = None
        self._links = None
        self.discriminator = None

        self.side = side
        self.security = security
        self.currency = currency
        self.rate = rate
        self.units = units
        self.amount = amount
        self.notional_amount = notional_amount
        self.links = links

    @property
    def side(self):
        """Gets the side of this SideDefinition.  # noqa: E501

        A unique label identifying the side definition.  # noqa: E501

        :return: The side of this SideDefinition.  # noqa: E501
        :rtype: str
        """
        return self._side

    @side.setter
    def side(self, side):
        """Sets the side of this SideDefinition.

        A unique label identifying the side definition.  # noqa: E501

        :param side: The side of this SideDefinition.  # noqa: E501
        :type side: str
        """
        if self.local_vars_configuration.client_side_validation and side is None:  # noqa: E501
            raise ValueError("Invalid value for `side`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                side is not None and len(side) > 64):
            raise ValueError("Invalid value for `side`, length must be less than or equal to `64`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                side is not None and len(side) < 1):
            raise ValueError("Invalid value for `side`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                side is not None and not re.search(r'^[a-zA-Z0-9\-_]+$', side)):  # noqa: E501
            raise ValueError(r"Invalid value for `side`, must be a follow pattern or equal to `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501

        self._side = side

    @property
    def security(self):
        """Gets the security of this SideDefinition.  # noqa: E501

        The field or property key defining the side's security, or instrument.  # noqa: E501

        :return: The security of this SideDefinition.  # noqa: E501
        :rtype: str
        """
        return self._security

    @security.setter
    def security(self, security):
        """Sets the security of this SideDefinition.

        The field or property key defining the side's security, or instrument.  # noqa: E501

        :param security: The security of this SideDefinition.  # noqa: E501
        :type security: str
        """
        if self.local_vars_configuration.client_side_validation and security is None:  # noqa: E501
            raise ValueError("Invalid value for `security`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                security is not None and len(security) > 64):
            raise ValueError("Invalid value for `security`, length must be less than or equal to `64`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                security is not None and len(security) < 1):
            raise ValueError("Invalid value for `security`, length must be greater than or equal to `1`")  # noqa: E501

        self._security = security

    @property
    def currency(self):
        """Gets the currency of this SideDefinition.  # noqa: E501

        The field or property key defining the side's currency.  # noqa: E501

        :return: The currency of this SideDefinition.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this SideDefinition.

        The field or property key defining the side's currency.  # noqa: E501

        :param currency: The currency of this SideDefinition.  # noqa: E501
        :type currency: str
        """
        if self.local_vars_configuration.client_side_validation and currency is None:  # noqa: E501
            raise ValueError("Invalid value for `currency`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                currency is not None and len(currency) > 64):
            raise ValueError("Invalid value for `currency`, length must be less than or equal to `64`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                currency is not None and len(currency) < 1):
            raise ValueError("Invalid value for `currency`, length must be greater than or equal to `1`")  # noqa: E501

        self._currency = currency

    @property
    def rate(self):
        """Gets the rate of this SideDefinition.  # noqa: E501

        The field or property key defining the side's rate.  # noqa: E501

        :return: The rate of this SideDefinition.  # noqa: E501
        :rtype: str
        """
        return self._rate

    @rate.setter
    def rate(self, rate):
        """Sets the rate of this SideDefinition.

        The field or property key defining the side's rate.  # noqa: E501

        :param rate: The rate of this SideDefinition.  # noqa: E501
        :type rate: str
        """
        if self.local_vars_configuration.client_side_validation and rate is None:  # noqa: E501
            raise ValueError("Invalid value for `rate`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                rate is not None and len(rate) > 64):
            raise ValueError("Invalid value for `rate`, length must be less than or equal to `64`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                rate is not None and len(rate) < 1):
            raise ValueError("Invalid value for `rate`, length must be greater than or equal to `1`")  # noqa: E501

        self._rate = rate

    @property
    def units(self):
        """Gets the units of this SideDefinition.  # noqa: E501

        The value, field or property key defining the side's units.  # noqa: E501

        :return: The units of this SideDefinition.  # noqa: E501
        :rtype: str
        """
        return self._units

    @units.setter
    def units(self, units):
        """Sets the units of this SideDefinition.

        The value, field or property key defining the side's units.  # noqa: E501

        :param units: The units of this SideDefinition.  # noqa: E501
        :type units: str
        """
        if self.local_vars_configuration.client_side_validation and units is None:  # noqa: E501
            raise ValueError("Invalid value for `units`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                units is not None and len(units) > 64):
            raise ValueError("Invalid value for `units`, length must be less than or equal to `64`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                units is not None and len(units) < 1):
            raise ValueError("Invalid value for `units`, length must be greater than or equal to `1`")  # noqa: E501

        self._units = units

    @property
    def amount(self):
        """Gets the amount of this SideDefinition.  # noqa: E501

        The value, field or property key defining the side's amount  # noqa: E501

        :return: The amount of this SideDefinition.  # noqa: E501
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this SideDefinition.

        The value, field or property key defining the side's amount  # noqa: E501

        :param amount: The amount of this SideDefinition.  # noqa: E501
        :type amount: str
        """
        if self.local_vars_configuration.client_side_validation and amount is None:  # noqa: E501
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                amount is not None and len(amount) > 64):
            raise ValueError("Invalid value for `amount`, length must be less than or equal to `64`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                amount is not None and len(amount) < 1):
            raise ValueError("Invalid value for `amount`, length must be greater than or equal to `1`")  # noqa: E501

        self._amount = amount

    @property
    def notional_amount(self):
        """Gets the notional_amount of this SideDefinition.  # noqa: E501

        The value, field or property key defining the side's notional amount  # noqa: E501

        :return: The notional_amount of this SideDefinition.  # noqa: E501
        :rtype: str
        """
        return self._notional_amount

    @notional_amount.setter
    def notional_amount(self, notional_amount):
        """Sets the notional_amount of this SideDefinition.

        The value, field or property key defining the side's notional amount  # noqa: E501

        :param notional_amount: The notional_amount of this SideDefinition.  # noqa: E501
        :type notional_amount: str
        """
        if (self.local_vars_configuration.client_side_validation and
                notional_amount is not None and len(notional_amount) > 64):
            raise ValueError("Invalid value for `notional_amount`, length must be less than or equal to `64`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                notional_amount is not None and len(notional_amount) < 1):
            raise ValueError("Invalid value for `notional_amount`, length must be greater than or equal to `1`")  # noqa: E501

        self._notional_amount = notional_amount

    @property
    def links(self):
        """Gets the links of this SideDefinition.  # noqa: E501

        Collection of links.  # noqa: E501

        :return: The links of this SideDefinition.  # noqa: E501
        :rtype: list[lusid.Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this SideDefinition.

        Collection of links.  # noqa: E501

        :param links: The links of this SideDefinition.  # noqa: E501
        :type links: list[lusid.Link]
        """

        self._links = links

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SideDefinition):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SideDefinition):
            return True

        return self.to_dict() != other.to_dict()
