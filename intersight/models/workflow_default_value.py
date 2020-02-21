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


class WorkflowDefaultValue(object):
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
        'override': 'bool',
        'value': 'object'
    }

    attribute_map = {
        'object_type': 'ObjectType',
        'override': 'Override',
        'value': 'Value'
    }

    def __init__(self, object_type=None, override=None, value=None):
        """
        WorkflowDefaultValue - a model defined in Swagger
        """

        self._object_type = None
        self._override = None
        self._value = None

        if object_type is not None:
          self.object_type = object_type
        if override is not None:
          self.override = override
        if value is not None:
          self.value = value

    @property
    def object_type(self):
        """
        Gets the object_type of this WorkflowDefaultValue.
        The concrete type of this complex type.  The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types.    

        :return: The object_type of this WorkflowDefaultValue.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this WorkflowDefaultValue.
        The concrete type of this complex type.  The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types.    

        :param object_type: The object_type of this WorkflowDefaultValue.
        :type: str
        """

        self._object_type = object_type

    @property
    def override(self):
        """
        Gets the override of this WorkflowDefaultValue.
        Override the default value provided for the data type. When true, allow the user to enter value for the data type.  

        :return: The override of this WorkflowDefaultValue.
        :rtype: bool
        """
        return self._override

    @override.setter
    def override(self, override):
        """
        Sets the override of this WorkflowDefaultValue.
        Override the default value provided for the data type. When true, allow the user to enter value for the data type.  

        :param override: The override of this WorkflowDefaultValue.
        :type: bool
        """

        self._override = override

    @property
    def value(self):
        """
        Gets the value of this WorkflowDefaultValue.
        Default value for the data type. If default value was provided and the input was required the default value will be used as the input.   

        :return: The value of this WorkflowDefaultValue.
        :rtype: object
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this WorkflowDefaultValue.
        Default value for the data type. If default value was provided and the input was required the default value will be used as the input.   

        :param value: The value of this WorkflowDefaultValue.
        :type: object
        """

        self._value = value

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
        if not isinstance(other, WorkflowDefaultValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other