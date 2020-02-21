# coding: utf-8

"""
    Cisco Intersight OpenAPI specification.

    The Cisco Intersight OpenAPI specification.

    OpenAPI spec version: 1.0.9-1415
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class BootPchStorage(object):
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
        'enabled': 'bool',
        'name': 'str',
        'lun': 'int'
    }

    attribute_map = {
        'object_type': 'ObjectType',
        'enabled': 'Enabled',
        'name': 'Name',
        'lun': 'Lun'
    }

    def __init__(self, object_type=None, enabled=None, name=None, lun=None):
        """
        BootPchStorage - a model defined in Swagger
        """

        self._object_type = None
        self._enabled = None
        self._name = None
        self._lun = None

        if object_type is not None:
          self.object_type = object_type
        if enabled is not None:
          self.enabled = enabled
        if name is not None:
          self.name = name
        if lun is not None:
          self.lun = lun

    @property
    def object_type(self):
        """
        Gets the object_type of this BootPchStorage.
        The concrete type of this complex type.  The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types.    

        :return: The object_type of this BootPchStorage.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this BootPchStorage.
        The concrete type of this complex type.  The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types.    

        :param object_type: The object_type of this BootPchStorage.
        :type: str
        """

        self._object_type = object_type

    @property
    def enabled(self):
        """
        Gets the enabled of this BootPchStorage.
        Specifies if the boot device is enabled or disabled.  

        :return: The enabled of this BootPchStorage.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this BootPchStorage.
        Specifies if the boot device is enabled or disabled.  

        :param enabled: The enabled of this BootPchStorage.
        :type: bool
        """

        self._enabled = enabled

    @property
    def name(self):
        """
        Gets the name of this BootPchStorage.
        A name that helps identify a boot device. It can be any string that adheres to the following constraints. It should start and end with an alphanumeric character. It can have underscores and hyphens. It cannot be more than 30 characters.   

        :return: The name of this BootPchStorage.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this BootPchStorage.
        A name that helps identify a boot device. It can be any string that adheres to the following constraints. It should start and end with an alphanumeric character. It can have underscores and hyphens. It cannot be more than 30 characters.   

        :param name: The name of this BootPchStorage.
        :type: str
        """

        self._name = name

    @property
    def lun(self):
        """
        Gets the lun of this BootPchStorage.
        The Logical Unit Number (LUN) of the device. It is the Virtual Drive number for Cisco UCS C-Series Servers. Virtual Drive number is found in storage inventory.   

        :return: The lun of this BootPchStorage.
        :rtype: int
        """
        return self._lun

    @lun.setter
    def lun(self, lun):
        """
        Sets the lun of this BootPchStorage.
        The Logical Unit Number (LUN) of the device. It is the Virtual Drive number for Cisco UCS C-Series Servers. Virtual Drive number is found in storage inventory.   

        :param lun: The lun of this BootPchStorage.
        :type: int
        """

        self._lun = lun

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
        if not isinstance(other, BootPchStorage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other