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

from fireeye.helix.configuration import Configuration


class InlineObject25(object):
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
        'title': 'str',
        'is_hidden': 'bool',
        'customer_id': 'str',
        'description': 'str',
        'tags': 'list[str]'
    }

    attribute_map = {
        'title': 'title',
        'is_hidden': 'is_hidden',
        'customer_id': 'customer_id',
        'description': 'description',
        'tags': 'tags'
    }

    def __init__(self, title=None, is_hidden=None, customer_id=None, description=None, tags=None, local_vars_configuration=None):  # noqa: E501
        """InlineObject25 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._title = None
        self._is_hidden = None
        self._customer_id = None
        self._description = None
        self._tags = None
        self.discriminator = None

        self.title = title
        if is_hidden is not None:
            self.is_hidden = is_hidden
        if customer_id is not None:
            self.customer_id = customer_id
        if description is not None:
            self.description = description
        if tags is not None:
            self.tags = tags

    @property
    def title(self):
        """Gets the title of this InlineObject25.  # noqa: E501

          # noqa: E501

        :return: The title of this InlineObject25.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this InlineObject25.

          # noqa: E501

        :param title: The title of this InlineObject25.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and title is None:  # noqa: E501
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def is_hidden(self):
        """Gets the is_hidden of this InlineObject25.  # noqa: E501

          # noqa: E501

        :return: The is_hidden of this InlineObject25.  # noqa: E501
        :rtype: bool
        """
        return self._is_hidden

    @is_hidden.setter
    def is_hidden(self, is_hidden):
        """Sets the is_hidden of this InlineObject25.

          # noqa: E501

        :param is_hidden: The is_hidden of this InlineObject25.  # noqa: E501
        :type: bool
        """

        self._is_hidden = is_hidden

    @property
    def customer_id(self):
        """Gets the customer_id of this InlineObject25.  # noqa: E501

          # noqa: E501

        :return: The customer_id of this InlineObject25.  # noqa: E501
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this InlineObject25.

          # noqa: E501

        :param customer_id: The customer_id of this InlineObject25.  # noqa: E501
        :type: str
        """

        self._customer_id = customer_id

    @property
    def description(self):
        """Gets the description of this InlineObject25.  # noqa: E501

          # noqa: E501

        :return: The description of this InlineObject25.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this InlineObject25.

          # noqa: E501

        :param description: The description of this InlineObject25.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def tags(self):
        """Gets the tags of this InlineObject25.  # noqa: E501

          # noqa: E501

        :return: The tags of this InlineObject25.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this InlineObject25.

          # noqa: E501

        :param tags: The tags of this InlineObject25.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

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
        if not isinstance(other, InlineObject25):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineObject25):
            return True

        return self.to_dict() != other.to_dict()