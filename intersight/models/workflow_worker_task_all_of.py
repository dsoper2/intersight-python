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


class WorkflowWorkerTaskAllOf(object):
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
        'catalog_moid': 'str',
        'task_definition_id': 'str',
        'task_definition_name': 'str',
        'version': 'int'
    }

    attribute_map = {
        'catalog_moid': 'CatalogMoid',
        'task_definition_id': 'TaskDefinitionId',
        'task_definition_name': 'TaskDefinitionName',
        'version': 'Version'
    }

    def __init__(self,
                 catalog_moid=None,
                 task_definition_id=None,
                 task_definition_name=None,
                 version=None,
                 local_vars_configuration=None):  # noqa: E501
        """WorkflowWorkerTaskAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._catalog_moid = None
        self._task_definition_id = None
        self._task_definition_name = None
        self._version = None
        self.discriminator = None

        if catalog_moid is not None:
            self.catalog_moid = catalog_moid
        if task_definition_id is not None:
            self.task_definition_id = task_definition_id
        if task_definition_name is not None:
            self.task_definition_name = task_definition_name
        if version is not None:
            self.version = version

    @property
    def catalog_moid(self):
        """Gets the catalog_moid of this WorkflowWorkerTaskAllOf.  # noqa: E501

        Specify the catalog moid that this task belongs.    # noqa: E501

        :return: The catalog_moid of this WorkflowWorkerTaskAllOf.  # noqa: E501
        :rtype: str
        """
        return self._catalog_moid

    @catalog_moid.setter
    def catalog_moid(self, catalog_moid):
        """Sets the catalog_moid of this WorkflowWorkerTaskAllOf.

        Specify the catalog moid that this task belongs.    # noqa: E501

        :param catalog_moid: The catalog_moid of this WorkflowWorkerTaskAllOf.  # noqa: E501
        :type: str
        """

        self._catalog_moid = catalog_moid

    @property
    def task_definition_id(self):
        """Gets the task_definition_id of this WorkflowWorkerTaskAllOf.  # noqa: E501

        The resolved referenced task definition managed object.    # noqa: E501

        :return: The task_definition_id of this WorkflowWorkerTaskAllOf.  # noqa: E501
        :rtype: str
        """
        return self._task_definition_id

    @task_definition_id.setter
    def task_definition_id(self, task_definition_id):
        """Sets the task_definition_id of this WorkflowWorkerTaskAllOf.

        The resolved referenced task definition managed object.    # noqa: E501

        :param task_definition_id: The task_definition_id of this WorkflowWorkerTaskAllOf.  # noqa: E501
        :type: str
        """

        self._task_definition_id = task_definition_id

    @property
    def task_definition_name(self):
        """Gets the task_definition_name of this WorkflowWorkerTaskAllOf.  # noqa: E501

        The qualified name of task that should be executed.    # noqa: E501

        :return: The task_definition_name of this WorkflowWorkerTaskAllOf.  # noqa: E501
        :rtype: str
        """
        return self._task_definition_name

    @task_definition_name.setter
    def task_definition_name(self, task_definition_name):
        """Sets the task_definition_name of this WorkflowWorkerTaskAllOf.

        The qualified name of task that should be executed.    # noqa: E501

        :param task_definition_name: The task_definition_name of this WorkflowWorkerTaskAllOf.  # noqa: E501
        :type: str
        """

        self._task_definition_name = task_definition_name

    @property
    def version(self):
        """Gets the version of this WorkflowWorkerTaskAllOf.  # noqa: E501

        The task definition version to use in this workflow. When no version is specified then the default version of the task at the time of creating or updating this workflow is used.     # noqa: E501

        :return: The version of this WorkflowWorkerTaskAllOf.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this WorkflowWorkerTaskAllOf.

        The task definition version to use in this workflow. When no version is specified then the default version of the task at the time of creating or updating this workflow is used.     # noqa: E501

        :param version: The version of this WorkflowWorkerTaskAllOf.  # noqa: E501
        :type: int
        """

        self._version = version

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
        if not isinstance(other, WorkflowWorkerTaskAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WorkflowWorkerTaskAllOf):
            return True

        return self.to_dict() != other.to_dict()