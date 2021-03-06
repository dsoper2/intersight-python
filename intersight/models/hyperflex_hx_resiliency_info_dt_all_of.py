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


class HyperflexHxResiliencyInfoDtAllOf(object):
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
        'data_replication_factor': 'str',
        'hdd_failures_tolerable': 'int',
        'messages': 'list[str]',
        'node_failures_tolerable': 'int',
        'policy_compliance': 'str',
        'resiliency_state': 'str',
        'ssd_failures_tolerable': 'int'
    }

    attribute_map = {
        'data_replication_factor': 'DataReplicationFactor',
        'hdd_failures_tolerable': 'HddFailuresTolerable',
        'messages': 'Messages',
        'node_failures_tolerable': 'NodeFailuresTolerable',
        'policy_compliance': 'PolicyCompliance',
        'resiliency_state': 'ResiliencyState',
        'ssd_failures_tolerable': 'SsdFailuresTolerable'
    }

    def __init__(self,
                 data_replication_factor='ONE_COPY',
                 hdd_failures_tolerable=None,
                 messages=None,
                 node_failures_tolerable=None,
                 policy_compliance='UNKNOWN',
                 resiliency_state='UNKNOWN',
                 ssd_failures_tolerable=None,
                 local_vars_configuration=None):  # noqa: E501
        """HyperflexHxResiliencyInfoDtAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._data_replication_factor = None
        self._hdd_failures_tolerable = None
        self._messages = None
        self._node_failures_tolerable = None
        self._policy_compliance = None
        self._resiliency_state = None
        self._ssd_failures_tolerable = None
        self.discriminator = None

        if data_replication_factor is not None:
            self.data_replication_factor = data_replication_factor
        if hdd_failures_tolerable is not None:
            self.hdd_failures_tolerable = hdd_failures_tolerable
        if messages is not None:
            self.messages = messages
        if node_failures_tolerable is not None:
            self.node_failures_tolerable = node_failures_tolerable
        if policy_compliance is not None:
            self.policy_compliance = policy_compliance
        if resiliency_state is not None:
            self.resiliency_state = resiliency_state
        if ssd_failures_tolerable is not None:
            self.ssd_failures_tolerable = ssd_failures_tolerable

    @property
    def data_replication_factor(self):
        """Gets the data_replication_factor of this HyperflexHxResiliencyInfoDtAllOf.  # noqa: E501


        :return: The data_replication_factor of this HyperflexHxResiliencyInfoDtAllOf.  # noqa: E501
        :rtype: str
        """
        return self._data_replication_factor

    @data_replication_factor.setter
    def data_replication_factor(self, data_replication_factor):
        """Sets the data_replication_factor of this HyperflexHxResiliencyInfoDtAllOf.


        :param data_replication_factor: The data_replication_factor of this HyperflexHxResiliencyInfoDtAllOf.  # noqa: E501
        :type: str
        """
        allowed_values = [
            "ONE_COPY", "TWO_COPIES", "THREE_COPIES", "FOUR_COPIES",
            "SIX_COPIES"
        ]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and data_replication_factor not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `data_replication_factor` ({0}), must be one of {1}"  # noqa: E501
                .format(data_replication_factor, allowed_values))

        self._data_replication_factor = data_replication_factor

    @property
    def hdd_failures_tolerable(self):
        """Gets the hdd_failures_tolerable of this HyperflexHxResiliencyInfoDtAllOf.  # noqa: E501


        :return: The hdd_failures_tolerable of this HyperflexHxResiliencyInfoDtAllOf.  # noqa: E501
        :rtype: int
        """
        return self._hdd_failures_tolerable

    @hdd_failures_tolerable.setter
    def hdd_failures_tolerable(self, hdd_failures_tolerable):
        """Sets the hdd_failures_tolerable of this HyperflexHxResiliencyInfoDtAllOf.


        :param hdd_failures_tolerable: The hdd_failures_tolerable of this HyperflexHxResiliencyInfoDtAllOf.  # noqa: E501
        :type: int
        """

        self._hdd_failures_tolerable = hdd_failures_tolerable

    @property
    def messages(self):
        """Gets the messages of this HyperflexHxResiliencyInfoDtAllOf.  # noqa: E501


        :return: The messages of this HyperflexHxResiliencyInfoDtAllOf.  # noqa: E501
        :rtype: list[str]
        """
        return self._messages

    @messages.setter
    def messages(self, messages):
        """Sets the messages of this HyperflexHxResiliencyInfoDtAllOf.


        :param messages: The messages of this HyperflexHxResiliencyInfoDtAllOf.  # noqa: E501
        :type: list[str]
        """

        self._messages = messages

    @property
    def node_failures_tolerable(self):
        """Gets the node_failures_tolerable of this HyperflexHxResiliencyInfoDtAllOf.  # noqa: E501


        :return: The node_failures_tolerable of this HyperflexHxResiliencyInfoDtAllOf.  # noqa: E501
        :rtype: int
        """
        return self._node_failures_tolerable

    @node_failures_tolerable.setter
    def node_failures_tolerable(self, node_failures_tolerable):
        """Sets the node_failures_tolerable of this HyperflexHxResiliencyInfoDtAllOf.


        :param node_failures_tolerable: The node_failures_tolerable of this HyperflexHxResiliencyInfoDtAllOf.  # noqa: E501
        :type: int
        """

        self._node_failures_tolerable = node_failures_tolerable

    @property
    def policy_compliance(self):
        """Gets the policy_compliance of this HyperflexHxResiliencyInfoDtAllOf.  # noqa: E501


        :return: The policy_compliance of this HyperflexHxResiliencyInfoDtAllOf.  # noqa: E501
        :rtype: str
        """
        return self._policy_compliance

    @policy_compliance.setter
    def policy_compliance(self, policy_compliance):
        """Sets the policy_compliance of this HyperflexHxResiliencyInfoDtAllOf.


        :param policy_compliance: The policy_compliance of this HyperflexHxResiliencyInfoDtAllOf.  # noqa: E501
        :type: str
        """
        allowed_values = ["UNKNOWN", "COMPLIANT",
                          "NON_COMPLIANT"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and policy_compliance not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `policy_compliance` ({0}), must be one of {1}"  # noqa: E501
                .format(policy_compliance, allowed_values))

        self._policy_compliance = policy_compliance

    @property
    def resiliency_state(self):
        """Gets the resiliency_state of this HyperflexHxResiliencyInfoDtAllOf.  # noqa: E501


        :return: The resiliency_state of this HyperflexHxResiliencyInfoDtAllOf.  # noqa: E501
        :rtype: str
        """
        return self._resiliency_state

    @resiliency_state.setter
    def resiliency_state(self, resiliency_state):
        """Sets the resiliency_state of this HyperflexHxResiliencyInfoDtAllOf.


        :param resiliency_state: The resiliency_state of this HyperflexHxResiliencyInfoDtAllOf.  # noqa: E501
        :type: str
        """
        allowed_values = ["UNKNOWN", "HEALTHY", "WARNING",
                          "OFFLINE"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and resiliency_state not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `resiliency_state` ({0}), must be one of {1}"  # noqa: E501
                .format(resiliency_state, allowed_values))

        self._resiliency_state = resiliency_state

    @property
    def ssd_failures_tolerable(self):
        """Gets the ssd_failures_tolerable of this HyperflexHxResiliencyInfoDtAllOf.  # noqa: E501


        :return: The ssd_failures_tolerable of this HyperflexHxResiliencyInfoDtAllOf.  # noqa: E501
        :rtype: int
        """
        return self._ssd_failures_tolerable

    @ssd_failures_tolerable.setter
    def ssd_failures_tolerable(self, ssd_failures_tolerable):
        """Sets the ssd_failures_tolerable of this HyperflexHxResiliencyInfoDtAllOf.


        :param ssd_failures_tolerable: The ssd_failures_tolerable of this HyperflexHxResiliencyInfoDtAllOf.  # noqa: E501
        :type: int
        """

        self._ssd_failures_tolerable = ssd_failures_tolerable

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
        if not isinstance(other, HyperflexHxResiliencyInfoDtAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, HyperflexHxResiliencyInfoDtAllOf):
            return True

        return self.to_dict() != other.to_dict()
