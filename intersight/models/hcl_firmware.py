# coding: utf-8

"""
    Intersight REST API

    This is Intersight REST API 

    OpenAPI spec version: 1.0.5-612
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class HclFirmware(object):
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
        'driver_name': 'str',
        'driver_version': 'str',
        'error_code': 'str',
        'firmware_version': 'str',
        'id': 'str'
    }

    attribute_map = {
        'driver_name': 'DriverName',
        'driver_version': 'DriverVersion',
        'error_code': 'ErrorCode',
        'firmware_version': 'FirmwareVersion',
        'id': 'Id'
    }

    def __init__(self, driver_name=None, driver_version=None, error_code='Success', firmware_version=None, id=None):
        """
        HclFirmware - a model defined in Swagger
        """

        self._driver_name = None
        self._driver_version = None
        self._error_code = None
        self._firmware_version = None
        self._id = None

        if driver_name is not None:
          self.driver_name = driver_name
        if driver_version is not None:
          self.driver_version = driver_version
        if error_code is not None:
          self.error_code = error_code
        if firmware_version is not None:
          self.firmware_version = firmware_version
        if id is not None:
          self.id = id

    @property
    def driver_name(self):
        """
        Gets the driver_name of this HclFirmware.
        Protocol for which the driver is provided.Ex enic, fnic,lsi_mr3  

        :return: The driver_name of this HclFirmware.
        :rtype: str
        """
        return self._driver_name

    @driver_name.setter
    def driver_name(self, driver_name):
        """
        Sets the driver_name of this HclFirmware.
        Protocol for which the driver is provided.Ex enic, fnic,lsi_mr3  

        :param driver_name: The driver_name of this HclFirmware.
        :type: str
        """

        self._driver_name = driver_name

    @property
    def driver_version(self):
        """
        Gets the driver_version of this HclFirmware.
        Version of the Driver  

        :return: The driver_version of this HclFirmware.
        :rtype: str
        """
        return self._driver_version

    @driver_version.setter
    def driver_version(self, driver_version):
        """
        Sets the driver_version of this HclFirmware.
        Version of the Driver  

        :param driver_version: The driver_version of this HclFirmware.
        :type: str
        """

        self._driver_version = driver_version

    @property
    def error_code(self):
        """
        Gets the error_code of this HclFirmware.
        Error code for the support status  

        :return: The error_code of this HclFirmware.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """
        Sets the error_code of this HclFirmware.
        Error code for the support status  

        :param error_code: The error_code of this HclFirmware.
        :type: str
        """
        allowed_values = ["Success", "Unknown", "InvalidUcsVersion", "UcsVersionServerOSCombinationNotSupported", "ProductNotSupported", "DriverNameNotSupported", "FirmwareNotSupported", "DriverVersionNotSupported", "FirmwareDriverVersionCombinationNotSupported", "FirmwareAndDriverNotSupported", "InternalError", "MarshallingError"]
        if error_code not in allowed_values:
            raise ValueError(
                "Invalid value for `error_code` ({0}), must be one of {1}"
                .format(error_code, allowed_values)
            )

        self._error_code = error_code

    @property
    def firmware_version(self):
        """
        Gets the firmware_version of this HclFirmware.
        firmware version of the product/adapter supported  

        :return: The firmware_version of this HclFirmware.
        :rtype: str
        """
        return self._firmware_version

    @firmware_version.setter
    def firmware_version(self, firmware_version):
        """
        Sets the firmware_version of this HclFirmware.
        firmware version of the product/adapter supported  

        :param firmware_version: The firmware_version of this HclFirmware.
        :type: str
        """

        self._firmware_version = firmware_version

    @property
    def id(self):
        """
        Gets the id of this HclFirmware.

        :return: The id of this HclFirmware.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this HclFirmware.

        :param id: The id of this HclFirmware.
        :type: str
        """

        self._id = id

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
        if not isinstance(other, HclFirmware):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
