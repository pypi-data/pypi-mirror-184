# coding: utf-8

"""
    UltraCart Rest API V2

    UltraCart REST API Version 2  # noqa: E501

    OpenAPI spec version: 2.0.0
    Contact: support@ultracart.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class CartKitComponentOption(object):
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
        'cost_if_specified': 'Currency',
        'cost_per_letter': 'Currency',
        'cost_per_line': 'Currency',
        'ignore_if_default': 'bool',
        'item_id': 'str',
        'item_oid': 'int',
        'label': 'str',
        'name': 'str',
        'one_time_fee': 'bool',
        'option_oid': 'int',
        'required': 'bool',
        'selected_value': 'str',
        'type': 'str',
        'values': 'list[CartItemOptionValue]'
    }

    attribute_map = {
        'cost_if_specified': 'cost_if_specified',
        'cost_per_letter': 'cost_per_letter',
        'cost_per_line': 'cost_per_line',
        'ignore_if_default': 'ignore_if_default',
        'item_id': 'item_id',
        'item_oid': 'item_oid',
        'label': 'label',
        'name': 'name',
        'one_time_fee': 'one_time_fee',
        'option_oid': 'option_oid',
        'required': 'required',
        'selected_value': 'selected_value',
        'type': 'type',
        'values': 'values'
    }

    def __init__(self, cost_if_specified=None, cost_per_letter=None, cost_per_line=None, ignore_if_default=None, item_id=None, item_oid=None, label=None, name=None, one_time_fee=None, option_oid=None, required=None, selected_value=None, type=None, values=None):  # noqa: E501
        """CartKitComponentOption - a model defined in Swagger"""  # noqa: E501

        self._cost_if_specified = None
        self._cost_per_letter = None
        self._cost_per_line = None
        self._ignore_if_default = None
        self._item_id = None
        self._item_oid = None
        self._label = None
        self._name = None
        self._one_time_fee = None
        self._option_oid = None
        self._required = None
        self._selected_value = None
        self._type = None
        self._values = None
        self.discriminator = None

        if cost_if_specified is not None:
            self.cost_if_specified = cost_if_specified
        if cost_per_letter is not None:
            self.cost_per_letter = cost_per_letter
        if cost_per_line is not None:
            self.cost_per_line = cost_per_line
        if ignore_if_default is not None:
            self.ignore_if_default = ignore_if_default
        if item_id is not None:
            self.item_id = item_id
        if item_oid is not None:
            self.item_oid = item_oid
        if label is not None:
            self.label = label
        if name is not None:
            self.name = name
        if one_time_fee is not None:
            self.one_time_fee = one_time_fee
        if option_oid is not None:
            self.option_oid = option_oid
        if required is not None:
            self.required = required
        if selected_value is not None:
            self.selected_value = selected_value
        if type is not None:
            self.type = type
        if values is not None:
            self.values = values

    @property
    def cost_if_specified(self):
        """Gets the cost_if_specified of this CartKitComponentOption.  # noqa: E501


        :return: The cost_if_specified of this CartKitComponentOption.  # noqa: E501
        :rtype: Currency
        """
        return self._cost_if_specified

    @cost_if_specified.setter
    def cost_if_specified(self, cost_if_specified):
        """Sets the cost_if_specified of this CartKitComponentOption.


        :param cost_if_specified: The cost_if_specified of this CartKitComponentOption.  # noqa: E501
        :type: Currency
        """

        self._cost_if_specified = cost_if_specified

    @property
    def cost_per_letter(self):
        """Gets the cost_per_letter of this CartKitComponentOption.  # noqa: E501


        :return: The cost_per_letter of this CartKitComponentOption.  # noqa: E501
        :rtype: Currency
        """
        return self._cost_per_letter

    @cost_per_letter.setter
    def cost_per_letter(self, cost_per_letter):
        """Sets the cost_per_letter of this CartKitComponentOption.


        :param cost_per_letter: The cost_per_letter of this CartKitComponentOption.  # noqa: E501
        :type: Currency
        """

        self._cost_per_letter = cost_per_letter

    @property
    def cost_per_line(self):
        """Gets the cost_per_line of this CartKitComponentOption.  # noqa: E501


        :return: The cost_per_line of this CartKitComponentOption.  # noqa: E501
        :rtype: Currency
        """
        return self._cost_per_line

    @cost_per_line.setter
    def cost_per_line(self, cost_per_line):
        """Sets the cost_per_line of this CartKitComponentOption.


        :param cost_per_line: The cost_per_line of this CartKitComponentOption.  # noqa: E501
        :type: Currency
        """

        self._cost_per_line = cost_per_line

    @property
    def ignore_if_default(self):
        """Gets the ignore_if_default of this CartKitComponentOption.  # noqa: E501

        True if the default answer is ignored  # noqa: E501

        :return: The ignore_if_default of this CartKitComponentOption.  # noqa: E501
        :rtype: bool
        """
        return self._ignore_if_default

    @ignore_if_default.setter
    def ignore_if_default(self, ignore_if_default):
        """Sets the ignore_if_default of this CartKitComponentOption.

        True if the default answer is ignored  # noqa: E501

        :param ignore_if_default: The ignore_if_default of this CartKitComponentOption.  # noqa: E501
        :type: bool
        """

        self._ignore_if_default = ignore_if_default

    @property
    def item_id(self):
        """Gets the item_id of this CartKitComponentOption.  # noqa: E501

        Kit component item id  # noqa: E501

        :return: The item_id of this CartKitComponentOption.  # noqa: E501
        :rtype: str
        """
        return self._item_id

    @item_id.setter
    def item_id(self, item_id):
        """Sets the item_id of this CartKitComponentOption.

        Kit component item id  # noqa: E501

        :param item_id: The item_id of this CartKitComponentOption.  # noqa: E501
        :type: str
        """

        self._item_id = item_id

    @property
    def item_oid(self):
        """Gets the item_oid of this CartKitComponentOption.  # noqa: E501

        Unique identifier for the kit component item  # noqa: E501

        :return: The item_oid of this CartKitComponentOption.  # noqa: E501
        :rtype: int
        """
        return self._item_oid

    @item_oid.setter
    def item_oid(self, item_oid):
        """Sets the item_oid of this CartKitComponentOption.

        Unique identifier for the kit component item  # noqa: E501

        :param item_oid: The item_oid of this CartKitComponentOption.  # noqa: E501
        :type: int
        """

        self._item_oid = item_oid

    @property
    def label(self):
        """Gets the label of this CartKitComponentOption.  # noqa: E501

        Display label for the option  # noqa: E501

        :return: The label of this CartKitComponentOption.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this CartKitComponentOption.

        Display label for the option  # noqa: E501

        :param label: The label of this CartKitComponentOption.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def name(self):
        """Gets the name of this CartKitComponentOption.  # noqa: E501

        Name of the option  # noqa: E501

        :return: The name of this CartKitComponentOption.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CartKitComponentOption.

        Name of the option  # noqa: E501

        :param name: The name of this CartKitComponentOption.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def one_time_fee(self):
        """Gets the one_time_fee of this CartKitComponentOption.  # noqa: E501

        Charge the fee a single time instead of multiplying by the quantity  # noqa: E501

        :return: The one_time_fee of this CartKitComponentOption.  # noqa: E501
        :rtype: bool
        """
        return self._one_time_fee

    @one_time_fee.setter
    def one_time_fee(self, one_time_fee):
        """Sets the one_time_fee of this CartKitComponentOption.

        Charge the fee a single time instead of multiplying by the quantity  # noqa: E501

        :param one_time_fee: The one_time_fee of this CartKitComponentOption.  # noqa: E501
        :type: bool
        """

        self._one_time_fee = one_time_fee

    @property
    def option_oid(self):
        """Gets the option_oid of this CartKitComponentOption.  # noqa: E501

        Unique identifier for the option  # noqa: E501

        :return: The option_oid of this CartKitComponentOption.  # noqa: E501
        :rtype: int
        """
        return self._option_oid

    @option_oid.setter
    def option_oid(self, option_oid):
        """Sets the option_oid of this CartKitComponentOption.

        Unique identifier for the option  # noqa: E501

        :param option_oid: The option_oid of this CartKitComponentOption.  # noqa: E501
        :type: int
        """

        self._option_oid = option_oid

    @property
    def required(self):
        """Gets the required of this CartKitComponentOption.  # noqa: E501

        True if the customer is required to select a value  # noqa: E501

        :return: The required of this CartKitComponentOption.  # noqa: E501
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        """Sets the required of this CartKitComponentOption.

        True if the customer is required to select a value  # noqa: E501

        :param required: The required of this CartKitComponentOption.  # noqa: E501
        :type: bool
        """

        self._required = required

    @property
    def selected_value(self):
        """Gets the selected_value of this CartKitComponentOption.  # noqa: E501

        The value of the option specified by the customer  # noqa: E501

        :return: The selected_value of this CartKitComponentOption.  # noqa: E501
        :rtype: str
        """
        return self._selected_value

    @selected_value.setter
    def selected_value(self, selected_value):
        """Sets the selected_value of this CartKitComponentOption.

        The value of the option specified by the customer  # noqa: E501

        :param selected_value: The selected_value of this CartKitComponentOption.  # noqa: E501
        :type: str
        """
        if selected_value is not None and len(selected_value) > 1024:
            raise ValueError("Invalid value for `selected_value`, length must be less than or equal to `1024`")  # noqa: E501

        self._selected_value = selected_value

    @property
    def type(self):
        """Gets the type of this CartKitComponentOption.  # noqa: E501

        Type of option  # noqa: E501

        :return: The type of this CartKitComponentOption.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CartKitComponentOption.

        Type of option  # noqa: E501

        :param type: The type of this CartKitComponentOption.  # noqa: E501
        :type: str
        """
        allowed_values = ["single", "multiline", "dropdown", "hidden", "radio", "fixed"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def values(self):
        """Gets the values of this CartKitComponentOption.  # noqa: E501

        Values that the customer can select from for radio or select type options  # noqa: E501

        :return: The values of this CartKitComponentOption.  # noqa: E501
        :rtype: list[CartItemOptionValue]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this CartKitComponentOption.

        Values that the customer can select from for radio or select type options  # noqa: E501

        :param values: The values of this CartKitComponentOption.  # noqa: E501
        :type: list[CartItemOptionValue]
        """

        self._values = values

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
        if issubclass(CartKitComponentOption, dict):
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
        if not isinstance(other, CartKitComponentOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
