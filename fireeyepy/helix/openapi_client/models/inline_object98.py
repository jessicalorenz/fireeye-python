# coding: utf-8

"""
    Helix API Documentation

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class InlineObject98(object):
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
    """
    openapi_types = {
        'created_by': 'str',
        'target_type': 'str',
        'create_date': 'str',
        'target_id': 'str',
        'is_enabled': 'bool',
        'update_date': 'str',
        'customer_id': 'str',
        'updated_by': 'str'
    }

    attribute_map = {
        'created_by': '_createdBy',
        'target_type': 'targetType',
        'create_date': 'createDate',
        'target_id': 'targetId',
        'is_enabled': 'isEnabled',
        'update_date': 'updateDate',
        'customer_id': 'customer_id',
        'updated_by': '_updatedBy'
    }

    def __init__(self, created_by=None, target_type=None, create_date=None, target_id=None, is_enabled=None, update_date=None, customer_id=None, updated_by=None, local_vars_configuration=None):  # noqa: E501
        """InlineObject98 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._created_by = None
        self._target_type = None
        self._create_date = None
        self._target_id = None
        self._is_enabled = None
        self._update_date = None
        self._customer_id = None
        self._updated_by = None
        self.discriminator = None

        if created_by is not None:
            self.created_by = created_by
        if target_type is not None:
            self.target_type = target_type
        if create_date is not None:
            self.create_date = create_date
        if target_id is not None:
            self.target_id = target_id
        if is_enabled is not None:
            self.is_enabled = is_enabled
        if update_date is not None:
            self.update_date = update_date
        if customer_id is not None:
            self.customer_id = customer_id
        if updated_by is not None:
            self.updated_by = updated_by

    @property
    def created_by(self):
        """Gets the created_by of this InlineObject98.  # noqa: E501

          # noqa: E501

        :return: The created_by of this InlineObject98.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this InlineObject98.

          # noqa: E501

        :param created_by: The created_by of this InlineObject98.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def target_type(self):
        """Gets the target_type of this InlineObject98.  # noqa: E501

          # noqa: E501

        :return: The target_type of this InlineObject98.  # noqa: E501
        :rtype: str
        """
        return self._target_type

    @target_type.setter
    def target_type(self, target_type):
        """Sets the target_type of this InlineObject98.

          # noqa: E501

        :param target_type: The target_type of this InlineObject98.  # noqa: E501
        :type: str
        """

        self._target_type = target_type

    @property
    def create_date(self):
        """Gets the create_date of this InlineObject98.  # noqa: E501

          # noqa: E501

        :return: The create_date of this InlineObject98.  # noqa: E501
        :rtype: str
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        """Sets the create_date of this InlineObject98.

          # noqa: E501

        :param create_date: The create_date of this InlineObject98.  # noqa: E501
        :type: str
        """

        self._create_date = create_date

    @property
    def target_id(self):
        """Gets the target_id of this InlineObject98.  # noqa: E501

          # noqa: E501

        :return: The target_id of this InlineObject98.  # noqa: E501
        :rtype: str
        """
        return self._target_id

    @target_id.setter
    def target_id(self, target_id):
        """Sets the target_id of this InlineObject98.

          # noqa: E501

        :param target_id: The target_id of this InlineObject98.  # noqa: E501
        :type: str
        """

        self._target_id = target_id

    @property
    def is_enabled(self):
        """Gets the is_enabled of this InlineObject98.  # noqa: E501

          # noqa: E501

        :return: The is_enabled of this InlineObject98.  # noqa: E501
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """Sets the is_enabled of this InlineObject98.

          # noqa: E501

        :param is_enabled: The is_enabled of this InlineObject98.  # noqa: E501
        :type: bool
        """

        self._is_enabled = is_enabled

    @property
    def update_date(self):
        """Gets the update_date of this InlineObject98.  # noqa: E501

          # noqa: E501

        :return: The update_date of this InlineObject98.  # noqa: E501
        :rtype: str
        """
        return self._update_date

    @update_date.setter
    def update_date(self, update_date):
        """Sets the update_date of this InlineObject98.

          # noqa: E501

        :param update_date: The update_date of this InlineObject98.  # noqa: E501
        :type: str
        """

        self._update_date = update_date

    @property
    def customer_id(self):
        """Gets the customer_id of this InlineObject98.  # noqa: E501

          # noqa: E501

        :return: The customer_id of this InlineObject98.  # noqa: E501
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this InlineObject98.

          # noqa: E501

        :param customer_id: The customer_id of this InlineObject98.  # noqa: E501
        :type: str
        """

        self._customer_id = customer_id

    @property
    def updated_by(self):
        """Gets the updated_by of this InlineObject98.  # noqa: E501

          # noqa: E501

        :return: The updated_by of this InlineObject98.  # noqa: E501
        :rtype: str
        """
        return self._updated_by

    @updated_by.setter
    def updated_by(self, updated_by):
        """Sets the updated_by of this InlineObject98.

          # noqa: E501

        :param updated_by: The updated_by of this InlineObject98.  # noqa: E501
        :type: str
        """

        self._updated_by = updated_by

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InlineObject98):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineObject98):
            return True

        return self.to_dict() != other.to_dict()