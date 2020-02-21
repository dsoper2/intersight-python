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


class StorageDiskUtilization(object):
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
        'available': 'int',
        'free': 'int',
        'total': 'int',
        'used': 'int'
    }

    attribute_map = {
        'object_type': 'ObjectType',
        'available': 'Available',
        'free': 'Free',
        'total': 'Total',
        'used': 'Used'
    }

    def __init__(self, object_type=None, available=None, free=None, total=None, used=None):
        """
        StorageDiskUtilization - a model defined in Swagger
        """

        self._object_type = None
        self._available = None
        self._free = None
        self._total = None
        self._used = None

        if object_type is not None:
          self.object_type = object_type
        if available is not None:
          self.available = available
        if free is not None:
          self.free = free
        if total is not None:
          self.total = total
        if used is not None:
          self.used = used

    @property
    def object_type(self):
        """
        Gets the object_type of this StorageDiskUtilization.
        The concrete type of this complex type.  The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types.    

        :return: The object_type of this StorageDiskUtilization.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this StorageDiskUtilization.
        The concrete type of this complex type.  The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types.    

        :param object_type: The object_type of this StorageDiskUtilization.
        :type: str
        """

        self._object_type = object_type

    @property
    def available(self):
        """
        Gets the available of this StorageDiskUtilization.
        Total consumable storage capacity represented in bytes. System may reserve some space for internal purpose which is excluded from total capacity.  

        :return: The available of this StorageDiskUtilization.
        :rtype: int
        """
        return self._available

    @available.setter
    def available(self, available):
        """
        Sets the available of this StorageDiskUtilization.
        Total consumable storage capacity represented in bytes. System may reserve some space for internal purpose which is excluded from total capacity.  

        :param available: The available of this StorageDiskUtilization.
        :type: int
        """

        self._available = available

    @property
    def free(self):
        """
        Gets the free of this StorageDiskUtilization.
        Unused space available for user to consume, represented in bytes.  

        :return: The free of this StorageDiskUtilization.
        :rtype: int
        """
        return self._free

    @free.setter
    def free(self, free):
        """
        Sets the free of this StorageDiskUtilization.
        Unused space available for user to consume, represented in bytes.  

        :param free: The free of this StorageDiskUtilization.
        :type: int
        """

        self._free = free

    @property
    def total(self):
        """
        Gets the total of this StorageDiskUtilization.
        Total storage capacity, represented in bytes. It is set by the component manufacture.  

        :return: The total of this StorageDiskUtilization.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """
        Sets the total of this StorageDiskUtilization.
        Total storage capacity, represented in bytes. It is set by the component manufacture.  

        :param total: The total of this StorageDiskUtilization.
        :type: int
        """

        self._total = total

    @property
    def used(self):
        """
        Gets the used of this StorageDiskUtilization.
        Used or consumed storage capacity, represented in bytes.   

        :return: The used of this StorageDiskUtilization.
        :rtype: int
        """
        return self._used

    @used.setter
    def used(self, used):
        """
        Sets the used of this StorageDiskUtilization.
        Used or consumed storage capacity, represented in bytes.   

        :param used: The used of this StorageDiskUtilization.
        :type: int
        """

        self._used = used

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
        if not isinstance(other, StorageDiskUtilization):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other