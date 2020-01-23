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


class InlineObject133(object):
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
        'uuid': 'str',
        'tags': 'list[str]',
        'title': 'str',
        'is_mssp': 'bool',
        'search_customer_ids': 'list[str]',
        'is_public': 'bool',
        'is_hidden': 'bool',
        'description': 'str'
    }

    attribute_map = {
        'uuid': 'uuid',
        'tags': 'tags',
        'title': 'title',
        'is_mssp': 'is_mssp',
        'search_customer_ids': 'search_customer_ids',
        'is_public': 'is_public',
        'is_hidden': 'is_hidden',
        'description': 'description'
    }

    def __init__(self, uuid=None, tags=None, title=None, is_mssp=None, search_customer_ids=None, is_public=None, is_hidden=None, description=None, local_vars_configuration=None):  # noqa: E501
        """InlineObject133 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._uuid = None
        self._tags = None
        self._title = None
        self._is_mssp = None
        self._search_customer_ids = None
        self._is_public = None
        self._is_hidden = None
        self._description = None
        self.discriminator = None

        if uuid is not None:
            self.uuid = uuid
        if tags is not None:
            self.tags = tags
        if title is not None:
            self.title = title
        if is_mssp is not None:
            self.is_mssp = is_mssp
        if search_customer_ids is not None:
            self.search_customer_ids = search_customer_ids
        if is_public is not None:
            self.is_public = is_public
        if is_hidden is not None:
            self.is_hidden = is_hidden
        if description is not None:
            self.description = description

    @property
    def uuid(self):
        """Gets the uuid of this InlineObject133.  # noqa: E501

          # noqa: E501

        :return: The uuid of this InlineObject133.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this InlineObject133.

          # noqa: E501

        :param uuid: The uuid of this InlineObject133.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def tags(self):
        """Gets the tags of this InlineObject133.  # noqa: E501

          # noqa: E501

        :return: The tags of this InlineObject133.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this InlineObject133.

          # noqa: E501

        :param tags: The tags of this InlineObject133.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def title(self):
        """Gets the title of this InlineObject133.  # noqa: E501

          # noqa: E501

        :return: The title of this InlineObject133.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this InlineObject133.

          # noqa: E501

        :param title: The title of this InlineObject133.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def is_mssp(self):
        """Gets the is_mssp of this InlineObject133.  # noqa: E501

          # noqa: E501

        :return: The is_mssp of this InlineObject133.  # noqa: E501
        :rtype: bool
        """
        return self._is_mssp

    @is_mssp.setter
    def is_mssp(self, is_mssp):
        """Sets the is_mssp of this InlineObject133.

          # noqa: E501

        :param is_mssp: The is_mssp of this InlineObject133.  # noqa: E501
        :type: bool
        """

        self._is_mssp = is_mssp

    @property
    def search_customer_ids(self):
        """Gets the search_customer_ids of this InlineObject133.  # noqa: E501

          # noqa: E501

        :return: The search_customer_ids of this InlineObject133.  # noqa: E501
        :rtype: list[str]
        """
        return self._search_customer_ids

    @search_customer_ids.setter
    def search_customer_ids(self, search_customer_ids):
        """Sets the search_customer_ids of this InlineObject133.

          # noqa: E501

        :param search_customer_ids: The search_customer_ids of this InlineObject133.  # noqa: E501
        :type: list[str]
        """

        self._search_customer_ids = search_customer_ids

    @property
    def is_public(self):
        """Gets the is_public of this InlineObject133.  # noqa: E501

          # noqa: E501

        :return: The is_public of this InlineObject133.  # noqa: E501
        :rtype: bool
        """
        return self._is_public

    @is_public.setter
    def is_public(self, is_public):
        """Sets the is_public of this InlineObject133.

          # noqa: E501

        :param is_public: The is_public of this InlineObject133.  # noqa: E501
        :type: bool
        """

        self._is_public = is_public

    @property
    def is_hidden(self):
        """Gets the is_hidden of this InlineObject133.  # noqa: E501

          # noqa: E501

        :return: The is_hidden of this InlineObject133.  # noqa: E501
        :rtype: bool
        """
        return self._is_hidden

    @is_hidden.setter
    def is_hidden(self, is_hidden):
        """Sets the is_hidden of this InlineObject133.

          # noqa: E501

        :param is_hidden: The is_hidden of this InlineObject133.  # noqa: E501
        :type: bool
        """

        self._is_hidden = is_hidden

    @property
    def description(self):
        """Gets the description of this InlineObject133.  # noqa: E501

          # noqa: E501

        :return: The description of this InlineObject133.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this InlineObject133.

          # noqa: E501

        :param description: The description of this InlineObject133.  # noqa: E501
        :type: str
        """

        self._description = description

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
        if not isinstance(other, InlineObject133):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineObject133):
            return True

        return self.to_dict() != other.to_dict()