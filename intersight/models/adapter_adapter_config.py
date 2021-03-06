# coding: utf-8

"""
    Cisco Intersight OpenAPI specification.

    The Cisco Intersight OpenAPI specification.

    OpenAPI spec version: 1.0.9-1461
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class AdapterAdapterConfig(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'object_type': 'str',
        'dce_interface_settings': 'list[AdapterDceInterfaceSettings]',
        'eth_settings': 'AdapterEthSettings',
        'fc_settings': 'AdapterFcSettings',
        'port_channel_settings': 'AdapterPortChannelSettings',
        'slot_id': 'str'
    }

    attribute_map = {
        'object_type': 'ObjectType',
        'dce_interface_settings': 'DceInterfaceSettings',
        'eth_settings': 'EthSettings',
        'fc_settings': 'FcSettings',
        'port_channel_settings': 'PortChannelSettings',
        'slot_id': 'SlotId'
    }

    def __init__(self, object_type=None, dce_interface_settings=None, eth_settings=None, fc_settings=None, port_channel_settings=None, slot_id=None):
        """
        AdapterAdapterConfig - a model defined in Swagger
        """

        self._object_type = None
        self._dce_interface_settings = None
        self._eth_settings = None
        self._fc_settings = None
        self._port_channel_settings = None
        self._slot_id = None

        if object_type is not None:
          self.object_type = object_type
        if dce_interface_settings is not None:
          self.dce_interface_settings = dce_interface_settings
        if eth_settings is not None:
          self.eth_settings = eth_settings
        if fc_settings is not None:
          self.fc_settings = fc_settings
        if port_channel_settings is not None:
          self.port_channel_settings = port_channel_settings
        if slot_id is not None:
          self.slot_id = slot_id

    @property
    def object_type(self):
        """
        Gets the object_type of this AdapterAdapterConfig.
        The concrete type of this complex type. The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types.

        :return: The object_type of this AdapterAdapterConfig.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this AdapterAdapterConfig.
        The concrete type of this complex type. The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types.

        :param object_type: The object_type of this AdapterAdapterConfig.
        :type: str
        """

        self._object_type = object_type

    @property
    def dce_interface_settings(self):
        """
        Gets the dce_interface_settings of this AdapterAdapterConfig.
        Collection of DCE interface settings for this adapter.

        :return: The dce_interface_settings of this AdapterAdapterConfig.
        :rtype: list[AdapterDceInterfaceSettings]
        """
        return self._dce_interface_settings

    @dce_interface_settings.setter
    def dce_interface_settings(self, dce_interface_settings):
        """
        Sets the dce_interface_settings of this AdapterAdapterConfig.
        Collection of DCE interface settings for this adapter.

        :param dce_interface_settings: The dce_interface_settings of this AdapterAdapterConfig.
        :type: list[AdapterDceInterfaceSettings]
        """

        self._dce_interface_settings = dce_interface_settings

    @property
    def eth_settings(self):
        """
        Gets the eth_settings of this AdapterAdapterConfig.
        Global Ethernet settings for this adapter.

        :return: The eth_settings of this AdapterAdapterConfig.
        :rtype: AdapterEthSettings
        """
        return self._eth_settings

    @eth_settings.setter
    def eth_settings(self, eth_settings):
        """
        Sets the eth_settings of this AdapterAdapterConfig.
        Global Ethernet settings for this adapter.

        :param eth_settings: The eth_settings of this AdapterAdapterConfig.
        :type: AdapterEthSettings
        """

        self._eth_settings = eth_settings

    @property
    def fc_settings(self):
        """
        Gets the fc_settings of this AdapterAdapterConfig.
        Global Fibre Channel settings for this adapter.

        :return: The fc_settings of this AdapterAdapterConfig.
        :rtype: AdapterFcSettings
        """
        return self._fc_settings

    @fc_settings.setter
    def fc_settings(self, fc_settings):
        """
        Sets the fc_settings of this AdapterAdapterConfig.
        Global Fibre Channel settings for this adapter.

        :param fc_settings: The fc_settings of this AdapterAdapterConfig.
        :type: AdapterFcSettings
        """

        self._fc_settings = fc_settings

    @property
    def port_channel_settings(self):
        """
        Gets the port_channel_settings of this AdapterAdapterConfig.
        Port Channel settings for this adapter.

        :return: The port_channel_settings of this AdapterAdapterConfig.
        :rtype: AdapterPortChannelSettings
        """
        return self._port_channel_settings

    @port_channel_settings.setter
    def port_channel_settings(self, port_channel_settings):
        """
        Sets the port_channel_settings of this AdapterAdapterConfig.
        Port Channel settings for this adapter.

        :param port_channel_settings: The port_channel_settings of this AdapterAdapterConfig.
        :type: AdapterPortChannelSettings
        """

        self._port_channel_settings = port_channel_settings

    @property
    def slot_id(self):
        """
        Gets the slot_id of this AdapterAdapterConfig.
        PCIe slot where the VIC adapter is installed. Supported values are (1-15) and MLOM.

        :return: The slot_id of this AdapterAdapterConfig.
        :rtype: str
        """
        return self._slot_id

    @slot_id.setter
    def slot_id(self, slot_id):
        """
        Sets the slot_id of this AdapterAdapterConfig.
        PCIe slot where the VIC adapter is installed. Supported values are (1-15) and MLOM.

        :param slot_id: The slot_id of this AdapterAdapterConfig.
        :type: str
        """

        self._slot_id = slot_id

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, AdapterAdapterConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
