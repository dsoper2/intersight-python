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


class IamDomainGroupAllOf(object):
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
        'name': 'str',
        'partition1': 'int',
        'partition2': 'int',
        'partition3': 'int',
        'partition_key': 'str',
        'usage': 'int',
        'account': 'IamAccount'
    }

    attribute_map = {
        'name': 'Name',
        'partition1': 'Partition1',
        'partition2': 'Partition2',
        'partition3': 'Partition3',
        'partition_key': 'PartitionKey',
        'usage': 'Usage',
        'account': 'Account'
    }

    def __init__(self,
                 name=None,
                 partition1=None,
                 partition2=None,
                 partition3=None,
                 partition_key=None,
                 usage=None,
                 account=None,
                 local_vars_configuration=None):  # noqa: E501
        """IamDomainGroupAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._partition1 = None
        self._partition2 = None
        self._partition3 = None
        self._partition_key = None
        self._usage = None
        self._account = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if partition1 is not None:
            self.partition1 = partition1
        if partition2 is not None:
            self.partition2 = partition2
        if partition3 is not None:
            self.partition3 = partition3
        if partition_key is not None:
            self.partition_key = partition_key
        if usage is not None:
            self.usage = usage
        if account is not None:
            self.account = account

    @property
    def name(self):
        """Gets the name of this IamDomainGroupAllOf.  # noqa: E501

        The name of the domain-group.     # noqa: E501

        :return: The name of this IamDomainGroupAllOf.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IamDomainGroupAllOf.

        The name of the domain-group.     # noqa: E501

        :param name: The name of this IamDomainGroupAllOf.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def partition1(self):
        """Gets the partition1 of this IamDomainGroupAllOf.  # noqa: E501

        The partition number domain group related messages are produced for 'Partition1' category service topics.     # noqa: E501

        :return: The partition1 of this IamDomainGroupAllOf.  # noqa: E501
        :rtype: int
        """
        return self._partition1

    @partition1.setter
    def partition1(self, partition1):
        """Sets the partition1 of this IamDomainGroupAllOf.

        The partition number domain group related messages are produced for 'Partition1' category service topics.     # noqa: E501

        :param partition1: The partition1 of this IamDomainGroupAllOf.  # noqa: E501
        :type: int
        """

        self._partition1 = partition1

    @property
    def partition2(self):
        """Gets the partition2 of this IamDomainGroupAllOf.  # noqa: E501

        In a cloud environment this parameter will indicate to which partition number domain group related messages are produced for 'Partition2' category service topics.     # noqa: E501

        :return: The partition2 of this IamDomainGroupAllOf.  # noqa: E501
        :rtype: int
        """
        return self._partition2

    @partition2.setter
    def partition2(self, partition2):
        """Sets the partition2 of this IamDomainGroupAllOf.

        In a cloud environment this parameter will indicate to which partition number domain group related messages are produced for 'Partition2' category service topics.     # noqa: E501

        :param partition2: The partition2 of this IamDomainGroupAllOf.  # noqa: E501
        :type: int
        """

        self._partition2 = partition2

    @property
    def partition3(self):
        """Gets the partition3 of this IamDomainGroupAllOf.  # noqa: E501

        In a cloud environment this parameter will indicate to which partition number domain group related messages are produced for 'Partition3' category service topics.     # noqa: E501

        :return: The partition3 of this IamDomainGroupAllOf.  # noqa: E501
        :rtype: int
        """
        return self._partition3

    @partition3.setter
    def partition3(self, partition3):
        """Sets the partition3 of this IamDomainGroupAllOf.

        In a cloud environment this parameter will indicate to which partition number domain group related messages are produced for 'Partition3' category service topics.     # noqa: E501

        :param partition3: The partition3 of this IamDomainGroupAllOf.  # noqa: E501
        :type: int
        """

        self._partition3 = partition3

    @property
    def partition_key(self):
        """Gets the partition_key of this IamDomainGroupAllOf.  # noqa: E501

        Partition key used for producing messages to Kafka partitions. By default Domain-group id will be used as parition key. For Domain-groups belonging to Early adopters domain-group id will be prefixed with 'H' and used as partition key, such partition key will be treated differently and messages will always be produced to partition 0.     # noqa: E501

        :return: The partition_key of this IamDomainGroupAllOf.  # noqa: E501
        :rtype: str
        """
        return self._partition_key

    @partition_key.setter
    def partition_key(self, partition_key):
        """Sets the partition_key of this IamDomainGroupAllOf.

        Partition key used for producing messages to Kafka partitions. By default Domain-group id will be used as parition key. For Domain-groups belonging to Early adopters domain-group id will be prefixed with 'H' and used as partition key, such partition key will be treated differently and messages will always be produced to partition 0.     # noqa: E501

        :param partition_key: The partition_key of this IamDomainGroupAllOf.  # noqa: E501
        :type: str
        """

        self._partition_key = partition_key

    @property
    def usage(self):
        """Gets the usage of this IamDomainGroupAllOf.  # noqa: E501

        The number of devices in the domain-group. Device registration notifications are processed to update the usage of the domain-group. The on-boarding account will have multiple domain-groups, and during the device registration least used domain-group will be selected for the device.      # noqa: E501

        :return: The usage of this IamDomainGroupAllOf.  # noqa: E501
        :rtype: int
        """
        return self._usage

    @usage.setter
    def usage(self, usage):
        """Sets the usage of this IamDomainGroupAllOf.

        The number of devices in the domain-group. Device registration notifications are processed to update the usage of the domain-group. The on-boarding account will have multiple domain-groups, and during the device registration least used domain-group will be selected for the device.      # noqa: E501

        :param usage: The usage of this IamDomainGroupAllOf.  # noqa: E501
        :type: int
        """

        self._usage = usage

    @property
    def account(self):
        """Gets the account of this IamDomainGroupAllOf.  # noqa: E501


        :return: The account of this IamDomainGroupAllOf.  # noqa: E501
        :rtype: IamAccount
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this IamDomainGroupAllOf.


        :param account: The account of this IamDomainGroupAllOf.  # noqa: E501
        :type: IamAccount
        """

        self._account = account

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
        if not isinstance(other, IamDomainGroupAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IamDomainGroupAllOf):
            return True

        return self.to_dict() != other.to_dict()