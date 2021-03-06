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


class ContentTextParameter(object):
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
        'accept_single_value': 'bool',
        'complex_type': 'str',
        'item_type': 'str',
        'name': 'str',
        'path': 'str',
        'type': 'str',
        'is_delimiter': 'bool',
        'is_next_capture_on_same_line': 'bool',
        'regex_line': 'str'
    }

    attribute_map = {
        'object_type': 'ObjectType',
        'accept_single_value': 'AcceptSingleValue',
        'complex_type': 'ComplexType',
        'item_type': 'ItemType',
        'name': 'Name',
        'path': 'Path',
        'type': 'Type',
        'is_delimiter': 'IsDelimiter',
        'is_next_capture_on_same_line': 'IsNextCaptureOnSameLine',
        'regex_line': 'RegexLine'
    }

    def __init__(self, object_type=None, accept_single_value=None, complex_type=None, item_type='simple', name=None, path=None, type='simple', is_delimiter=None, is_next_capture_on_same_line=None, regex_line=None):
        """
        ContentTextParameter - a model defined in Swagger
        """

        self._object_type = None
        self._accept_single_value = None
        self._complex_type = None
        self._item_type = None
        self._name = None
        self._path = None
        self._type = None
        self._is_delimiter = None
        self._is_next_capture_on_same_line = None
        self._regex_line = None

        if object_type is not None:
          self.object_type = object_type
        if accept_single_value is not None:
          self.accept_single_value = accept_single_value
        if complex_type is not None:
          self.complex_type = complex_type
        if item_type is not None:
          self.item_type = item_type
        if name is not None:
          self.name = name
        if path is not None:
          self.path = path
        if type is not None:
          self.type = type
        if is_delimiter is not None:
          self.is_delimiter = is_delimiter
        if is_next_capture_on_same_line is not None:
          self.is_next_capture_on_same_line = is_next_capture_on_same_line
        if regex_line is not None:
          self.regex_line = regex_line

    @property
    def object_type(self):
        """
        Gets the object_type of this ContentTextParameter.
        The concrete type of this complex type. The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types.

        :return: The object_type of this ContentTextParameter.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this ContentTextParameter.
        The concrete type of this complex type. The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types.

        :param object_type: The object_type of this ContentTextParameter.
        :type: str
        """

        self._object_type = object_type

    @property
    def accept_single_value(self):
        """
        Gets the accept_single_value of this ContentTextParameter.
        The flag that allows single values in content to be extracted as a single element collection in case the parameter is of Collection type. This flag is applicable for parameters of type Collection only.

        :return: The accept_single_value of this ContentTextParameter.
        :rtype: bool
        """
        return self._accept_single_value

    @accept_single_value.setter
    def accept_single_value(self, accept_single_value):
        """
        Sets the accept_single_value of this ContentTextParameter.
        The flag that allows single values in content to be extracted as a single element collection in case the parameter is of Collection type. This flag is applicable for parameters of type Collection only.

        :param accept_single_value: The accept_single_value of this ContentTextParameter.
        :type: bool
        """

        self._accept_single_value = accept_single_value

    @property
    def complex_type(self):
        """
        Gets the complex_type of this ContentTextParameter.
        The name of the complex type definition in case this is a complex parameter. The content.Grammar object must have a complex type, content.ComplexType, defined with the specified name in types collection property.

        :return: The complex_type of this ContentTextParameter.
        :rtype: str
        """
        return self._complex_type

    @complex_type.setter
    def complex_type(self, complex_type):
        """
        Sets the complex_type of this ContentTextParameter.
        The name of the complex type definition in case this is a complex parameter. The content.Grammar object must have a complex type, content.ComplexType, defined with the specified name in types collection property.

        :param complex_type: The complex_type of this ContentTextParameter.
        :type: str
        """

        self._complex_type = complex_type

    @property
    def item_type(self):
        """
        Gets the item_type of this ContentTextParameter.
        The type of the collection item in case this is a collection parameter.

        :return: The item_type of this ContentTextParameter.
        :rtype: str
        """
        return self._item_type

    @item_type.setter
    def item_type(self, item_type):
        """
        Sets the item_type of this ContentTextParameter.
        The type of the collection item in case this is a collection parameter.

        :param item_type: The item_type of this ContentTextParameter.
        :type: str
        """
        allowed_values = ["simple", "complex", "collection"]
        if item_type not in allowed_values:
            raise ValueError(
                "Invalid value for `item_type` ({0}), must be one of {1}"
                .format(item_type, allowed_values)
            )

        self._item_type = item_type

    @property
    def name(self):
        """
        Gets the name of this ContentTextParameter.
        The name of the parameter.

        :return: The name of this ContentTextParameter.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ContentTextParameter.
        The name of the parameter.

        :param name: The name of this ContentTextParameter.
        :type: str
        """

        self._name = name

    @property
    def path(self):
        """
        Gets the path of this ContentTextParameter.
        The content specific path information that identifies the parameter value within the content. The value is usually a XPath or JSONPath or a regular expression in case of text content.

        :return: The path of this ContentTextParameter.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this ContentTextParameter.
        The content specific path information that identifies the parameter value within the content. The value is usually a XPath or JSONPath or a regular expression in case of text content.

        :param path: The path of this ContentTextParameter.
        :type: str
        """

        self._path = path

    @property
    def type(self):
        """
        Gets the type of this ContentTextParameter.
        The type of the parameter. Accepted values are simple, complex, collection.

        :return: The type of this ContentTextParameter.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this ContentTextParameter.
        The type of the parameter. Accepted values are simple, complex, collection.

        :param type: The type of this ContentTextParameter.
        :type: str
        """
        allowed_values = ["simple", "complex", "collection"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def is_delimiter(self):
        """
        Gets the is_delimiter of this ContentTextParameter.
        Data to be extracted from text content can be simple type or complex type or collection of simple/complex types. Complex types are group of simple or complex type. Delimiter is required to stop parsing list and complex data types. isDelimiter specifies whether given TextParameter is a delimiter or regular rule to capture the text data.

        :return: The is_delimiter of this ContentTextParameter.
        :rtype: bool
        """
        return self._is_delimiter

    @is_delimiter.setter
    def is_delimiter(self, is_delimiter):
        """
        Sets the is_delimiter of this ContentTextParameter.
        Data to be extracted from text content can be simple type or complex type or collection of simple/complex types. Complex types are group of simple or complex type. Delimiter is required to stop parsing list and complex data types. isDelimiter specifies whether given TextParameter is a delimiter or regular rule to capture the text data.

        :param is_delimiter: The is_delimiter of this ContentTextParameter.
        :type: bool
        """

        self._is_delimiter = is_delimiter

    @property
    def is_next_capture_on_same_line(self):
        """
        Gets the is_next_capture_on_same_line of this ContentTextParameter.
        Set to true of the next value to capture resides on the same text line of current match. By default textFSM engine gets the next text line on finding the first match.

        :return: The is_next_capture_on_same_line of this ContentTextParameter.
        :rtype: bool
        """
        return self._is_next_capture_on_same_line

    @is_next_capture_on_same_line.setter
    def is_next_capture_on_same_line(self, is_next_capture_on_same_line):
        """
        Sets the is_next_capture_on_same_line of this ContentTextParameter.
        Set to true of the next value to capture resides on the same text line of current match. By default textFSM engine gets the next text line on finding the first match.

        :param is_next_capture_on_same_line: The is_next_capture_on_same_line of this ContentTextParameter.
        :type: bool
        """

        self._is_next_capture_on_same_line = is_next_capture_on_same_line

    @property
    def regex_line(self):
        """
        Gets the regex_line of this ContentTextParameter.
        Regular expression of the line containing the data to be extracted from text content.

        :return: The regex_line of this ContentTextParameter.
        :rtype: str
        """
        return self._regex_line

    @regex_line.setter
    def regex_line(self, regex_line):
        """
        Sets the regex_line of this ContentTextParameter.
        Regular expression of the line containing the data to be extracted from text content.

        :param regex_line: The regex_line of this ContentTextParameter.
        :type: str
        """

        self._regex_line = regex_line

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
        if not isinstance(other, ContentTextParameter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
