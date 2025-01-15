# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: release-1.32
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from kubernetes.client.configuration import Configuration


class V1FieldSelectorAttributes(object):
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
        'raw_selector': 'str',
        'requirements': 'list[V1FieldSelectorRequirement]'
    }

    attribute_map = {
        'raw_selector': 'rawSelector',
        'requirements': 'requirements'
    }

    def __init__(self, raw_selector=None, requirements=None, local_vars_configuration=None):  # noqa: E501
        """V1FieldSelectorAttributes - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._raw_selector = None
        self._requirements = None
        self.discriminator = None

        if raw_selector is not None:
            self.raw_selector = raw_selector
        if requirements is not None:
            self.requirements = requirements

    @property
    def raw_selector(self):
        """Gets the raw_selector of this V1FieldSelectorAttributes.  # noqa: E501

        rawSelector is the serialization of a field selector that would be included in a query parameter. Webhook implementations are encouraged to ignore rawSelector. The kube-apiserver's *SubjectAccessReview will parse the rawSelector as long as the requirements are not present.  # noqa: E501

        :return: The raw_selector of this V1FieldSelectorAttributes.  # noqa: E501
        :rtype: str
        """
        return self._raw_selector

    @raw_selector.setter
    def raw_selector(self, raw_selector):
        """Sets the raw_selector of this V1FieldSelectorAttributes.

        rawSelector is the serialization of a field selector that would be included in a query parameter. Webhook implementations are encouraged to ignore rawSelector. The kube-apiserver's *SubjectAccessReview will parse the rawSelector as long as the requirements are not present.  # noqa: E501

        :param raw_selector: The raw_selector of this V1FieldSelectorAttributes.  # noqa: E501
        :type: str
        """

        self._raw_selector = raw_selector

    @property
    def requirements(self):
        """Gets the requirements of this V1FieldSelectorAttributes.  # noqa: E501

        requirements is the parsed interpretation of a field selector. All requirements must be met for a resource instance to match the selector. Webhook implementations should handle requirements, but how to handle them is up to the webhook. Since requirements can only limit the request, it is safe to authorize as unlimited request if the requirements are not understood.  # noqa: E501

        :return: The requirements of this V1FieldSelectorAttributes.  # noqa: E501
        :rtype: list[V1FieldSelectorRequirement]
        """
        return self._requirements

    @requirements.setter
    def requirements(self, requirements):
        """Sets the requirements of this V1FieldSelectorAttributes.

        requirements is the parsed interpretation of a field selector. All requirements must be met for a resource instance to match the selector. Webhook implementations should handle requirements, but how to handle them is up to the webhook. Since requirements can only limit the request, it is safe to authorize as unlimited request if the requirements are not understood.  # noqa: E501

        :param requirements: The requirements of this V1FieldSelectorAttributes.  # noqa: E501
        :type: list[V1FieldSelectorRequirement]
        """

        self._requirements = requirements

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
        if not isinstance(other, V1FieldSelectorAttributes):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1FieldSelectorAttributes):
            return True

        return self.to_dict() != other.to_dict()