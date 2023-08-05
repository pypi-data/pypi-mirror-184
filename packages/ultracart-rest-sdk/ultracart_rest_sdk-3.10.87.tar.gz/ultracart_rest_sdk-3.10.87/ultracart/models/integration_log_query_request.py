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


class IntegrationLogQueryRequest(object):
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
        'action': 'str',
        'direction': 'str',
        'email': 'str',
        'file_names': 'list[str]',
        'item_id': 'str',
        'item_ipn_oid': 'int',
        'log_dts_begin': 'str',
        'log_dts_end': 'str',
        'log_type': 'str',
        'logger_id': 'str',
        'logger_name': 'str',
        'order_ids': 'list[str]',
        'status': 'str'
    }

    attribute_map = {
        'action': 'action',
        'direction': 'direction',
        'email': 'email',
        'file_names': 'file_names',
        'item_id': 'item_id',
        'item_ipn_oid': 'item_ipn_oid',
        'log_dts_begin': 'log_dts_begin',
        'log_dts_end': 'log_dts_end',
        'log_type': 'log_type',
        'logger_id': 'logger_id',
        'logger_name': 'logger_name',
        'order_ids': 'order_ids',
        'status': 'status'
    }

    def __init__(self, action=None, direction=None, email=None, file_names=None, item_id=None, item_ipn_oid=None, log_dts_begin=None, log_dts_end=None, log_type=None, logger_id=None, logger_name=None, order_ids=None, status=None):  # noqa: E501
        """IntegrationLogQueryRequest - a model defined in Swagger"""  # noqa: E501

        self._action = None
        self._direction = None
        self._email = None
        self._file_names = None
        self._item_id = None
        self._item_ipn_oid = None
        self._log_dts_begin = None
        self._log_dts_end = None
        self._log_type = None
        self._logger_id = None
        self._logger_name = None
        self._order_ids = None
        self._status = None
        self.discriminator = None

        if action is not None:
            self.action = action
        if direction is not None:
            self.direction = direction
        if email is not None:
            self.email = email
        if file_names is not None:
            self.file_names = file_names
        if item_id is not None:
            self.item_id = item_id
        if item_ipn_oid is not None:
            self.item_ipn_oid = item_ipn_oid
        if log_dts_begin is not None:
            self.log_dts_begin = log_dts_begin
        if log_dts_end is not None:
            self.log_dts_end = log_dts_end
        if log_type is not None:
            self.log_type = log_type
        if logger_id is not None:
            self.logger_id = logger_id
        if logger_name is not None:
            self.logger_name = logger_name
        if order_ids is not None:
            self.order_ids = order_ids
        if status is not None:
            self.status = status

    @property
    def action(self):
        """Gets the action of this IntegrationLogQueryRequest.  # noqa: E501


        :return: The action of this IntegrationLogQueryRequest.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this IntegrationLogQueryRequest.


        :param action: The action of this IntegrationLogQueryRequest.  # noqa: E501
        :type: str
        """

        self._action = action

    @property
    def direction(self):
        """Gets the direction of this IntegrationLogQueryRequest.  # noqa: E501


        :return: The direction of this IntegrationLogQueryRequest.  # noqa: E501
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """Sets the direction of this IntegrationLogQueryRequest.


        :param direction: The direction of this IntegrationLogQueryRequest.  # noqa: E501
        :type: str
        """

        self._direction = direction

    @property
    def email(self):
        """Gets the email of this IntegrationLogQueryRequest.  # noqa: E501


        :return: The email of this IntegrationLogQueryRequest.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this IntegrationLogQueryRequest.


        :param email: The email of this IntegrationLogQueryRequest.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def file_names(self):
        """Gets the file_names of this IntegrationLogQueryRequest.  # noqa: E501


        :return: The file_names of this IntegrationLogQueryRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._file_names

    @file_names.setter
    def file_names(self, file_names):
        """Sets the file_names of this IntegrationLogQueryRequest.


        :param file_names: The file_names of this IntegrationLogQueryRequest.  # noqa: E501
        :type: list[str]
        """

        self._file_names = file_names

    @property
    def item_id(self):
        """Gets the item_id of this IntegrationLogQueryRequest.  # noqa: E501


        :return: The item_id of this IntegrationLogQueryRequest.  # noqa: E501
        :rtype: str
        """
        return self._item_id

    @item_id.setter
    def item_id(self, item_id):
        """Sets the item_id of this IntegrationLogQueryRequest.


        :param item_id: The item_id of this IntegrationLogQueryRequest.  # noqa: E501
        :type: str
        """

        self._item_id = item_id

    @property
    def item_ipn_oid(self):
        """Gets the item_ipn_oid of this IntegrationLogQueryRequest.  # noqa: E501


        :return: The item_ipn_oid of this IntegrationLogQueryRequest.  # noqa: E501
        :rtype: int
        """
        return self._item_ipn_oid

    @item_ipn_oid.setter
    def item_ipn_oid(self, item_ipn_oid):
        """Sets the item_ipn_oid of this IntegrationLogQueryRequest.


        :param item_ipn_oid: The item_ipn_oid of this IntegrationLogQueryRequest.  # noqa: E501
        :type: int
        """

        self._item_ipn_oid = item_ipn_oid

    @property
    def log_dts_begin(self):
        """Gets the log_dts_begin of this IntegrationLogQueryRequest.  # noqa: E501

        Log date/time begin  # noqa: E501

        :return: The log_dts_begin of this IntegrationLogQueryRequest.  # noqa: E501
        :rtype: str
        """
        return self._log_dts_begin

    @log_dts_begin.setter
    def log_dts_begin(self, log_dts_begin):
        """Sets the log_dts_begin of this IntegrationLogQueryRequest.

        Log date/time begin  # noqa: E501

        :param log_dts_begin: The log_dts_begin of this IntegrationLogQueryRequest.  # noqa: E501
        :type: str
        """

        self._log_dts_begin = log_dts_begin

    @property
    def log_dts_end(self):
        """Gets the log_dts_end of this IntegrationLogQueryRequest.  # noqa: E501

        Log date/time end  # noqa: E501

        :return: The log_dts_end of this IntegrationLogQueryRequest.  # noqa: E501
        :rtype: str
        """
        return self._log_dts_end

    @log_dts_end.setter
    def log_dts_end(self, log_dts_end):
        """Sets the log_dts_end of this IntegrationLogQueryRequest.

        Log date/time end  # noqa: E501

        :param log_dts_end: The log_dts_end of this IntegrationLogQueryRequest.  # noqa: E501
        :type: str
        """

        self._log_dts_end = log_dts_end

    @property
    def log_type(self):
        """Gets the log_type of this IntegrationLogQueryRequest.  # noqa: E501


        :return: The log_type of this IntegrationLogQueryRequest.  # noqa: E501
        :rtype: str
        """
        return self._log_type

    @log_type.setter
    def log_type(self, log_type):
        """Sets the log_type of this IntegrationLogQueryRequest.


        :param log_type: The log_type of this IntegrationLogQueryRequest.  # noqa: E501
        :type: str
        """

        self._log_type = log_type

    @property
    def logger_id(self):
        """Gets the logger_id of this IntegrationLogQueryRequest.  # noqa: E501


        :return: The logger_id of this IntegrationLogQueryRequest.  # noqa: E501
        :rtype: str
        """
        return self._logger_id

    @logger_id.setter
    def logger_id(self, logger_id):
        """Sets the logger_id of this IntegrationLogQueryRequest.


        :param logger_id: The logger_id of this IntegrationLogQueryRequest.  # noqa: E501
        :type: str
        """

        self._logger_id = logger_id

    @property
    def logger_name(self):
        """Gets the logger_name of this IntegrationLogQueryRequest.  # noqa: E501


        :return: The logger_name of this IntegrationLogQueryRequest.  # noqa: E501
        :rtype: str
        """
        return self._logger_name

    @logger_name.setter
    def logger_name(self, logger_name):
        """Sets the logger_name of this IntegrationLogQueryRequest.


        :param logger_name: The logger_name of this IntegrationLogQueryRequest.  # noqa: E501
        :type: str
        """

        self._logger_name = logger_name

    @property
    def order_ids(self):
        """Gets the order_ids of this IntegrationLogQueryRequest.  # noqa: E501


        :return: The order_ids of this IntegrationLogQueryRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._order_ids

    @order_ids.setter
    def order_ids(self, order_ids):
        """Sets the order_ids of this IntegrationLogQueryRequest.


        :param order_ids: The order_ids of this IntegrationLogQueryRequest.  # noqa: E501
        :type: list[str]
        """

        self._order_ids = order_ids

    @property
    def status(self):
        """Gets the status of this IntegrationLogQueryRequest.  # noqa: E501


        :return: The status of this IntegrationLogQueryRequest.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this IntegrationLogQueryRequest.


        :param status: The status of this IntegrationLogQueryRequest.  # noqa: E501
        :type: str
        """

        self._status = status

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
        if issubclass(IntegrationLogQueryRequest, dict):
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
        if not isinstance(other, IntegrationLogQueryRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
