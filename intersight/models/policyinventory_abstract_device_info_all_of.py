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


class PolicyinventoryAbstractDeviceInfoAllOf(object):
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
        'config_state': 'str',
        'control_action': 'str',
        'error_state': 'str',
        'job_info': 'list[PolicyinventoryJobInfo]',
        'oper_state': 'str',
        'profile_mo_id': 'str',
        'registered_device': 'AssetDeviceRegistration'
    }

    attribute_map = {
        'config_state': 'ConfigState',
        'control_action': 'ControlAction',
        'error_state': 'ErrorState',
        'job_info': 'JobInfo',
        'oper_state': 'OperState',
        'profile_mo_id': 'ProfileMoId',
        'registered_device': 'RegisteredDevice'
    }

    def __init__(self,
                 config_state=None,
                 control_action=None,
                 error_state=None,
                 job_info=None,
                 oper_state=None,
                 profile_mo_id=None,
                 registered_device=None,
                 local_vars_configuration=None):  # noqa: E501
        """PolicyinventoryAbstractDeviceInfoAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._config_state = None
        self._control_action = None
        self._error_state = None
        self._job_info = None
        self._oper_state = None
        self._profile_mo_id = None
        self._registered_device = None
        self.discriminator = None

        if config_state is not None:
            self.config_state = config_state
        if control_action is not None:
            self.control_action = control_action
        if error_state is not None:
            self.error_state = error_state
        if job_info is not None:
            self.job_info = job_info
        if oper_state is not None:
            self.oper_state = oper_state
        if profile_mo_id is not None:
            self.profile_mo_id = profile_mo_id
        if registered_device is not None:
            self.registered_device = registered_device

    @property
    def config_state(self):
        """Gets the config_state of this PolicyinventoryAbstractDeviceInfoAllOf.  # noqa: E501

        Configuration state of server profile config context.    # noqa: E501

        :return: The config_state of this PolicyinventoryAbstractDeviceInfoAllOf.  # noqa: E501
        :rtype: str
        """
        return self._config_state

    @config_state.setter
    def config_state(self, config_state):
        """Sets the config_state of this PolicyinventoryAbstractDeviceInfoAllOf.

        Configuration state of server profile config context.    # noqa: E501

        :param config_state: The config_state of this PolicyinventoryAbstractDeviceInfoAllOf.  # noqa: E501
        :type: str
        """

        self._config_state = config_state

    @property
    def control_action(self):
        """Gets the control_action of this PolicyinventoryAbstractDeviceInfoAllOf.  # noqa: E501

        Control action of server profile config context.    # noqa: E501

        :return: The control_action of this PolicyinventoryAbstractDeviceInfoAllOf.  # noqa: E501
        :rtype: str
        """
        return self._control_action

    @control_action.setter
    def control_action(self, control_action):
        """Sets the control_action of this PolicyinventoryAbstractDeviceInfoAllOf.

        Control action of server profile config context.    # noqa: E501

        :param control_action: The control_action of this PolicyinventoryAbstractDeviceInfoAllOf.  # noqa: E501
        :type: str
        """

        self._control_action = control_action

    @property
    def error_state(self):
        """Gets the error_state of this PolicyinventoryAbstractDeviceInfoAllOf.  # noqa: E501

        Error state of server profile config context.    # noqa: E501

        :return: The error_state of this PolicyinventoryAbstractDeviceInfoAllOf.  # noqa: E501
        :rtype: str
        """
        return self._error_state

    @error_state.setter
    def error_state(self, error_state):
        """Sets the error_state of this PolicyinventoryAbstractDeviceInfoAllOf.

        Error state of server profile config context.    # noqa: E501

        :param error_state: The error_state of this PolicyinventoryAbstractDeviceInfoAllOf.  # noqa: E501
        :type: str
        """

        self._error_state = error_state

    @property
    def job_info(self):
        """Gets the job_info of this PolicyinventoryAbstractDeviceInfoAllOf.  # noqa: E501


        :return: The job_info of this PolicyinventoryAbstractDeviceInfoAllOf.  # noqa: E501
        :rtype: list[PolicyinventoryJobInfo]
        """
        return self._job_info

    @job_info.setter
    def job_info(self, job_info):
        """Sets the job_info of this PolicyinventoryAbstractDeviceInfoAllOf.


        :param job_info: The job_info of this PolicyinventoryAbstractDeviceInfoAllOf.  # noqa: E501
        :type: list[PolicyinventoryJobInfo]
        """

        self._job_info = job_info

    @property
    def oper_state(self):
        """Gets the oper_state of this PolicyinventoryAbstractDeviceInfoAllOf.  # noqa: E501

        Operational state of server profile config context.    # noqa: E501

        :return: The oper_state of this PolicyinventoryAbstractDeviceInfoAllOf.  # noqa: E501
        :rtype: str
        """
        return self._oper_state

    @oper_state.setter
    def oper_state(self, oper_state):
        """Sets the oper_state of this PolicyinventoryAbstractDeviceInfoAllOf.

        Operational state of server profile config context.    # noqa: E501

        :param oper_state: The oper_state of this PolicyinventoryAbstractDeviceInfoAllOf.  # noqa: E501
        :type: str
        """

        self._oper_state = oper_state

    @property
    def profile_mo_id(self):
        """Gets the profile_mo_id of this PolicyinventoryAbstractDeviceInfoAllOf.  # noqa: E501

        Server profile MO ID of the server.     # noqa: E501

        :return: The profile_mo_id of this PolicyinventoryAbstractDeviceInfoAllOf.  # noqa: E501
        :rtype: str
        """
        return self._profile_mo_id

    @profile_mo_id.setter
    def profile_mo_id(self, profile_mo_id):
        """Sets the profile_mo_id of this PolicyinventoryAbstractDeviceInfoAllOf.

        Server profile MO ID of the server.     # noqa: E501

        :param profile_mo_id: The profile_mo_id of this PolicyinventoryAbstractDeviceInfoAllOf.  # noqa: E501
        :type: str
        """

        self._profile_mo_id = profile_mo_id

    @property
    def registered_device(self):
        """Gets the registered_device of this PolicyinventoryAbstractDeviceInfoAllOf.  # noqa: E501


        :return: The registered_device of this PolicyinventoryAbstractDeviceInfoAllOf.  # noqa: E501
        :rtype: AssetDeviceRegistration
        """
        return self._registered_device

    @registered_device.setter
    def registered_device(self, registered_device):
        """Sets the registered_device of this PolicyinventoryAbstractDeviceInfoAllOf.


        :param registered_device: The registered_device of this PolicyinventoryAbstractDeviceInfoAllOf.  # noqa: E501
        :type: AssetDeviceRegistration
        """

        self._registered_device = registered_device

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
        if not isinstance(other, PolicyinventoryAbstractDeviceInfoAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PolicyinventoryAbstractDeviceInfoAllOf):
            return True

        return self.to_dict() != other.to_dict()
