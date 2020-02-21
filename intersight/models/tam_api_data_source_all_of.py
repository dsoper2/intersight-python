# coding: utf-8
"""
    Cisco Intersight

    Cisco Intersight is a management platform delivered as a service with embedded analytics for your Cisco and 3rd party IT infrastructure. This platform offers an intelligent level of management that enables IT organizations to analyze, simplify, and automate their environments in more advanced ways than the prior generations of tools. Cisco Intersight provides an integrated and intuitive management experience for resources in the traditional data center as well as at the edge. With flexible deployment options to address complex security needs, getting started with Intersight is quick and easy. Cisco Intersight has deep integration with Cisco UCS and HyperFlex systems allowing for remote deployment, configuration, and ongoing maintenance. The model-based deployment works for a single system in a remote location or hundreds of systems in a data center and enables rapid, standardized configuration and deployment. It also streamlines maintaining those systems whether you are working with small or very large configurations.   # noqa: E501

    The version of the OpenAPI document: 1.0.9-1295
    Contact: intersight@cisco.com
    Generated by: https://openapi-generator.tech
"""

import pprint
import re  # noqa: F401

import six

from intersight.configuration import Configuration


class TamApiDataSourceAllOf(object):
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
    openapi_types = {'mo_type': 'str', 'queries': 'list[TamQueryEntry]'}

    attribute_map = {'mo_type': 'MoType', 'queries': 'Queries'}

    def __init__(self,
                 mo_type=None,
                 queries=None,
                 local_vars_configuration=None):  # noqa: E501
        """TamApiDataSourceAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._mo_type = None
        self._queries = None
        self.discriminator = None

        if mo_type is not None:
            self.mo_type = mo_type
        if queries is not None:
            self.queries = queries

    @property
    def mo_type(self):
        """Gets the mo_type of this TamApiDataSourceAllOf.  # noqa: E501

        Type of Intersight managed object used as data source.    # noqa: E501

        :return: The mo_type of this TamApiDataSourceAllOf.  # noqa: E501
        :rtype: str
        """
        return self._mo_type

    @mo_type.setter
    def mo_type(self, mo_type):
        """Sets the mo_type of this TamApiDataSourceAllOf.

        Type of Intersight managed object used as data source.    # noqa: E501

        :param mo_type: The mo_type of this TamApiDataSourceAllOf.  # noqa: E501
        :type: str
        """

        self._mo_type = mo_type

    @property
    def queries(self):
        """Gets the queries of this TamApiDataSourceAllOf.  # noqa: E501


        :return: The queries of this TamApiDataSourceAllOf.  # noqa: E501
        :rtype: list[TamQueryEntry]
        """
        return self._queries

    @queries.setter
    def queries(self, queries):
        """Sets the queries of this TamApiDataSourceAllOf.


        :param queries: The queries of this TamApiDataSourceAllOf.  # noqa: E501
        :type: list[TamQueryEntry]
        """

        self._queries = queries

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict()
                        if hasattr(x, "to_dict") else x, value))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict") else item,
                        value.items()))
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
        if not isinstance(other, TamApiDataSourceAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TamApiDataSourceAllOf):
            return True

        return self.to_dict() != other.to_dict()