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


class StorageFlexUtilPhysicalDrive(object):
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
        'account_moid': 'str',
        'ancestors': 'list[MoBaseMoRef]',
        'create_time': 'datetime',
        'mod_time': 'datetime',
        'moid': 'str',
        'object_type': 'str',
        'owners': 'list[str]',
        'parent': 'MoBaseMoRef',
        'tags': 'list[MoTag]',
        'device_mo_id': 'str',
        'dn': 'str',
        'rn': 'str',
        'model': 'str',
        'revision': 'str',
        'serial': 'str',
        'vendor': 'str',
        'block_size': 'str',
        'capacity': 'str',
        'controller': 'str',
        'drives_enabled': 'str',
        'health': 'str',
        'manufacturer_date': 'str',
        'manufacturer_id': 'str',
        'oem_id': 'str',
        'partition_count': 'str',
        'pd_status': 'str',
        'physical_drive': 'str',
        'product_name': 'str',
        'product_revision': 'str',
        'read_error_count': 'str',
        'read_error_threshold': 'str',
        'registered_device': 'AssetDeviceRegistrationRef',
        'storage_flex_util_controller': 'StorageFlexUtilControllerRef',
        'write_enabled': 'str',
        'write_error_count': 'str',
        'write_error_threshold': 'str'
    }

    attribute_map = {
        'account_moid': 'AccountMoid',
        'ancestors': 'Ancestors',
        'create_time': 'CreateTime',
        'mod_time': 'ModTime',
        'moid': 'Moid',
        'object_type': 'ObjectType',
        'owners': 'Owners',
        'parent': 'Parent',
        'tags': 'Tags',
        'device_mo_id': 'DeviceMoId',
        'dn': 'Dn',
        'rn': 'Rn',
        'model': 'Model',
        'revision': 'Revision',
        'serial': 'Serial',
        'vendor': 'Vendor',
        'block_size': 'BlockSize',
        'capacity': 'Capacity',
        'controller': 'Controller',
        'drives_enabled': 'DrivesEnabled',
        'health': 'Health',
        'manufacturer_date': 'ManufacturerDate',
        'manufacturer_id': 'ManufacturerId',
        'oem_id': 'OemId',
        'partition_count': 'PartitionCount',
        'pd_status': 'PdStatus',
        'physical_drive': 'PhysicalDrive',
        'product_name': 'ProductName',
        'product_revision': 'ProductRevision',
        'read_error_count': 'ReadErrorCount',
        'read_error_threshold': 'ReadErrorThreshold',
        'registered_device': 'RegisteredDevice',
        'storage_flex_util_controller': 'StorageFlexUtilController',
        'write_enabled': 'WriteEnabled',
        'write_error_count': 'WriteErrorCount',
        'write_error_threshold': 'WriteErrorThreshold'
    }

    def __init__(self, account_moid=None, ancestors=None, create_time=None, mod_time=None, moid=None, object_type=None, owners=None, parent=None, tags=None, device_mo_id=None, dn=None, rn=None, model=None, revision=None, serial=None, vendor=None, block_size=None, capacity=None, controller=None, drives_enabled=None, health=None, manufacturer_date=None, manufacturer_id=None, oem_id=None, partition_count=None, pd_status=None, physical_drive=None, product_name=None, product_revision=None, read_error_count=None, read_error_threshold=None, registered_device=None, storage_flex_util_controller=None, write_enabled=None, write_error_count=None, write_error_threshold=None):
        """
        StorageFlexUtilPhysicalDrive - a model defined in Swagger
        """

        self._account_moid = None
        self._ancestors = None
        self._create_time = None
        self._mod_time = None
        self._moid = None
        self._object_type = None
        self._owners = None
        self._parent = None
        self._tags = None
        self._device_mo_id = None
        self._dn = None
        self._rn = None
        self._model = None
        self._revision = None
        self._serial = None
        self._vendor = None
        self._block_size = None
        self._capacity = None
        self._controller = None
        self._drives_enabled = None
        self._health = None
        self._manufacturer_date = None
        self._manufacturer_id = None
        self._oem_id = None
        self._partition_count = None
        self._pd_status = None
        self._physical_drive = None
        self._product_name = None
        self._product_revision = None
        self._read_error_count = None
        self._read_error_threshold = None
        self._registered_device = None
        self._storage_flex_util_controller = None
        self._write_enabled = None
        self._write_error_count = None
        self._write_error_threshold = None

        if account_moid is not None:
          self.account_moid = account_moid
        if ancestors is not None:
          self.ancestors = ancestors
        if create_time is not None:
          self.create_time = create_time
        if mod_time is not None:
          self.mod_time = mod_time
        if moid is not None:
          self.moid = moid
        if object_type is not None:
          self.object_type = object_type
        if owners is not None:
          self.owners = owners
        if parent is not None:
          self.parent = parent
        if tags is not None:
          self.tags = tags
        if device_mo_id is not None:
          self.device_mo_id = device_mo_id
        if dn is not None:
          self.dn = dn
        if rn is not None:
          self.rn = rn
        if model is not None:
          self.model = model
        if revision is not None:
          self.revision = revision
        if serial is not None:
          self.serial = serial
        if vendor is not None:
          self.vendor = vendor
        if block_size is not None:
          self.block_size = block_size
        if capacity is not None:
          self.capacity = capacity
        if controller is not None:
          self.controller = controller
        if drives_enabled is not None:
          self.drives_enabled = drives_enabled
        if health is not None:
          self.health = health
        if manufacturer_date is not None:
          self.manufacturer_date = manufacturer_date
        if manufacturer_id is not None:
          self.manufacturer_id = manufacturer_id
        if oem_id is not None:
          self.oem_id = oem_id
        if partition_count is not None:
          self.partition_count = partition_count
        if pd_status is not None:
          self.pd_status = pd_status
        if physical_drive is not None:
          self.physical_drive = physical_drive
        if product_name is not None:
          self.product_name = product_name
        if product_revision is not None:
          self.product_revision = product_revision
        if read_error_count is not None:
          self.read_error_count = read_error_count
        if read_error_threshold is not None:
          self.read_error_threshold = read_error_threshold
        if registered_device is not None:
          self.registered_device = registered_device
        if storage_flex_util_controller is not None:
          self.storage_flex_util_controller = storage_flex_util_controller
        if write_enabled is not None:
          self.write_enabled = write_enabled
        if write_error_count is not None:
          self.write_error_count = write_error_count
        if write_error_threshold is not None:
          self.write_error_threshold = write_error_threshold

    @property
    def account_moid(self):
        """
        Gets the account_moid of this StorageFlexUtilPhysicalDrive.
        The Account ID for this managed object.  

        :return: The account_moid of this StorageFlexUtilPhysicalDrive.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this StorageFlexUtilPhysicalDrive.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this StorageFlexUtilPhysicalDrive.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def ancestors(self):
        """
        Gets the ancestors of this StorageFlexUtilPhysicalDrive.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this StorageFlexUtilPhysicalDrive.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this StorageFlexUtilPhysicalDrive.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this StorageFlexUtilPhysicalDrive.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def create_time(self):
        """
        Gets the create_time of this StorageFlexUtilPhysicalDrive.
        The time when this managed object was created.  

        :return: The create_time of this StorageFlexUtilPhysicalDrive.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this StorageFlexUtilPhysicalDrive.
        The time when this managed object was created.  

        :param create_time: The create_time of this StorageFlexUtilPhysicalDrive.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def mod_time(self):
        """
        Gets the mod_time of this StorageFlexUtilPhysicalDrive.
        The time when this managed object was last modified.  

        :return: The mod_time of this StorageFlexUtilPhysicalDrive.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this StorageFlexUtilPhysicalDrive.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this StorageFlexUtilPhysicalDrive.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this StorageFlexUtilPhysicalDrive.
        A unique identifier of this Managed Object instance.  

        :return: The moid of this StorageFlexUtilPhysicalDrive.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this StorageFlexUtilPhysicalDrive.
        A unique identifier of this Managed Object instance.  

        :param moid: The moid of this StorageFlexUtilPhysicalDrive.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this StorageFlexUtilPhysicalDrive.
        The fully-qualified type of this managed object, e.g. the class name.  

        :return: The object_type of this StorageFlexUtilPhysicalDrive.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this StorageFlexUtilPhysicalDrive.
        The fully-qualified type of this managed object, e.g. the class name.  

        :param object_type: The object_type of this StorageFlexUtilPhysicalDrive.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this StorageFlexUtilPhysicalDrive.
        An array of owners which represent effective ownership of this object.   

        :return: The owners of this StorageFlexUtilPhysicalDrive.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this StorageFlexUtilPhysicalDrive.
        An array of owners which represent effective ownership of this object.   

        :param owners: The owners of this StorageFlexUtilPhysicalDrive.
        :type: list[str]
        """

        self._owners = owners

    @property
    def parent(self):
        """
        Gets the parent of this StorageFlexUtilPhysicalDrive.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this StorageFlexUtilPhysicalDrive.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this StorageFlexUtilPhysicalDrive.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this StorageFlexUtilPhysicalDrive.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def tags(self):
        """
        Gets the tags of this StorageFlexUtilPhysicalDrive.
        An array of tags, which allow to add key, value meta-data to managed objects.   

        :return: The tags of this StorageFlexUtilPhysicalDrive.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this StorageFlexUtilPhysicalDrive.
        An array of tags, which allow to add key, value meta-data to managed objects.   

        :param tags: The tags of this StorageFlexUtilPhysicalDrive.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def device_mo_id(self):
        """
        Gets the device_mo_id of this StorageFlexUtilPhysicalDrive.

        :return: The device_mo_id of this StorageFlexUtilPhysicalDrive.
        :rtype: str
        """
        return self._device_mo_id

    @device_mo_id.setter
    def device_mo_id(self, device_mo_id):
        """
        Sets the device_mo_id of this StorageFlexUtilPhysicalDrive.

        :param device_mo_id: The device_mo_id of this StorageFlexUtilPhysicalDrive.
        :type: str
        """

        self._device_mo_id = device_mo_id

    @property
    def dn(self):
        """
        Gets the dn of this StorageFlexUtilPhysicalDrive.

        :return: The dn of this StorageFlexUtilPhysicalDrive.
        :rtype: str
        """
        return self._dn

    @dn.setter
    def dn(self, dn):
        """
        Sets the dn of this StorageFlexUtilPhysicalDrive.

        :param dn: The dn of this StorageFlexUtilPhysicalDrive.
        :type: str
        """

        self._dn = dn

    @property
    def rn(self):
        """
        Gets the rn of this StorageFlexUtilPhysicalDrive.

        :return: The rn of this StorageFlexUtilPhysicalDrive.
        :rtype: str
        """
        return self._rn

    @rn.setter
    def rn(self, rn):
        """
        Sets the rn of this StorageFlexUtilPhysicalDrive.

        :param rn: The rn of this StorageFlexUtilPhysicalDrive.
        :type: str
        """

        self._rn = rn

    @property
    def model(self):
        """
        Gets the model of this StorageFlexUtilPhysicalDrive.

        :return: The model of this StorageFlexUtilPhysicalDrive.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """
        Sets the model of this StorageFlexUtilPhysicalDrive.

        :param model: The model of this StorageFlexUtilPhysicalDrive.
        :type: str
        """

        self._model = model

    @property
    def revision(self):
        """
        Gets the revision of this StorageFlexUtilPhysicalDrive.

        :return: The revision of this StorageFlexUtilPhysicalDrive.
        :rtype: str
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """
        Sets the revision of this StorageFlexUtilPhysicalDrive.

        :param revision: The revision of this StorageFlexUtilPhysicalDrive.
        :type: str
        """

        self._revision = revision

    @property
    def serial(self):
        """
        Gets the serial of this StorageFlexUtilPhysicalDrive.

        :return: The serial of this StorageFlexUtilPhysicalDrive.
        :rtype: str
        """
        return self._serial

    @serial.setter
    def serial(self, serial):
        """
        Sets the serial of this StorageFlexUtilPhysicalDrive.

        :param serial: The serial of this StorageFlexUtilPhysicalDrive.
        :type: str
        """

        self._serial = serial

    @property
    def vendor(self):
        """
        Gets the vendor of this StorageFlexUtilPhysicalDrive.

        :return: The vendor of this StorageFlexUtilPhysicalDrive.
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        """
        Sets the vendor of this StorageFlexUtilPhysicalDrive.

        :param vendor: The vendor of this StorageFlexUtilPhysicalDrive.
        :type: str
        """

        self._vendor = vendor

    @property
    def block_size(self):
        """
        Gets the block_size of this StorageFlexUtilPhysicalDrive.

        :return: The block_size of this StorageFlexUtilPhysicalDrive.
        :rtype: str
        """
        return self._block_size

    @block_size.setter
    def block_size(self, block_size):
        """
        Sets the block_size of this StorageFlexUtilPhysicalDrive.

        :param block_size: The block_size of this StorageFlexUtilPhysicalDrive.
        :type: str
        """

        self._block_size = block_size

    @property
    def capacity(self):
        """
        Gets the capacity of this StorageFlexUtilPhysicalDrive.

        :return: The capacity of this StorageFlexUtilPhysicalDrive.
        :rtype: str
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """
        Sets the capacity of this StorageFlexUtilPhysicalDrive.

        :param capacity: The capacity of this StorageFlexUtilPhysicalDrive.
        :type: str
        """

        self._capacity = capacity

    @property
    def controller(self):
        """
        Gets the controller of this StorageFlexUtilPhysicalDrive.

        :return: The controller of this StorageFlexUtilPhysicalDrive.
        :rtype: str
        """
        return self._controller

    @controller.setter
    def controller(self, controller):
        """
        Sets the controller of this StorageFlexUtilPhysicalDrive.

        :param controller: The controller of this StorageFlexUtilPhysicalDrive.
        :type: str
        """

        self._controller = controller

    @property
    def drives_enabled(self):
        """
        Gets the drives_enabled of this StorageFlexUtilPhysicalDrive.

        :return: The drives_enabled of this StorageFlexUtilPhysicalDrive.
        :rtype: str
        """
        return self._drives_enabled

    @drives_enabled.setter
    def drives_enabled(self, drives_enabled):
        """
        Sets the drives_enabled of this StorageFlexUtilPhysicalDrive.

        :param drives_enabled: The drives_enabled of this StorageFlexUtilPhysicalDrive.
        :type: str
        """

        self._drives_enabled = drives_enabled

    @property
    def health(self):
        """
        Gets the health of this StorageFlexUtilPhysicalDrive.

        :return: The health of this StorageFlexUtilPhysicalDrive.
        :rtype: str
        """
        return self._health

    @health.setter
    def health(self, health):
        """
        Sets the health of this StorageFlexUtilPhysicalDrive.

        :param health: The health of this StorageFlexUtilPhysicalDrive.
        :type: str
        """

        self._health = health

    @property
    def manufacturer_date(self):
        """
        Gets the manufacturer_date of this StorageFlexUtilPhysicalDrive.

        :return: The manufacturer_date of this StorageFlexUtilPhysicalDrive.
        :rtype: str
        """
        return self._manufacturer_date

    @manufacturer_date.setter
    def manufacturer_date(self, manufacturer_date):
        """
        Sets the manufacturer_date of this StorageFlexUtilPhysicalDrive.

        :param manufacturer_date: The manufacturer_date of this StorageFlexUtilPhysicalDrive.
        :type: str
        """

        self._manufacturer_date = manufacturer_date

    @property
    def manufacturer_id(self):
        """
        Gets the manufacturer_id of this StorageFlexUtilPhysicalDrive.

        :return: The manufacturer_id of this StorageFlexUtilPhysicalDrive.
        :rtype: str
        """
        return self._manufacturer_id

    @manufacturer_id.setter
    def manufacturer_id(self, manufacturer_id):
        """
        Sets the manufacturer_id of this StorageFlexUtilPhysicalDrive.

        :param manufacturer_id: The manufacturer_id of this StorageFlexUtilPhysicalDrive.
        :type: str
        """

        self._manufacturer_id = manufacturer_id

    @property
    def oem_id(self):
        """
        Gets the oem_id of this StorageFlexUtilPhysicalDrive.

        :return: The oem_id of this StorageFlexUtilPhysicalDrive.
        :rtype: str
        """
        return self._oem_id

    @oem_id.setter
    def oem_id(self, oem_id):
        """
        Sets the oem_id of this StorageFlexUtilPhysicalDrive.

        :param oem_id: The oem_id of this StorageFlexUtilPhysicalDrive.
        :type: str
        """

        self._oem_id = oem_id

    @property
    def partition_count(self):
        """
        Gets the partition_count of this StorageFlexUtilPhysicalDrive.

        :return: The partition_count of this StorageFlexUtilPhysicalDrive.
        :rtype: str
        """
        return self._partition_count

    @partition_count.setter
    def partition_count(self, partition_count):
        """
        Sets the partition_count of this StorageFlexUtilPhysicalDrive.

        :param partition_count: The partition_count of this StorageFlexUtilPhysicalDrive.
        :type: str
        """

        self._partition_count = partition_count

    @property
    def pd_status(self):
        """
        Gets the pd_status of this StorageFlexUtilPhysicalDrive.

        :return: The pd_status of this StorageFlexUtilPhysicalDrive.
        :rtype: str
        """
        return self._pd_status

    @pd_status.setter
    def pd_status(self, pd_status):
        """
        Sets the pd_status of this StorageFlexUtilPhysicalDrive.

        :param pd_status: The pd_status of this StorageFlexUtilPhysicalDrive.
        :type: str
        """

        self._pd_status = pd_status

    @property
    def physical_drive(self):
        """
        Gets the physical_drive of this StorageFlexUtilPhysicalDrive.

        :return: The physical_drive of this StorageFlexUtilPhysicalDrive.
        :rtype: str
        """
        return self._physical_drive

    @physical_drive.setter
    def physical_drive(self, physical_drive):
        """
        Sets the physical_drive of this StorageFlexUtilPhysicalDrive.

        :param physical_drive: The physical_drive of this StorageFlexUtilPhysicalDrive.
        :type: str
        """

        self._physical_drive = physical_drive

    @property
    def product_name(self):
        """
        Gets the product_name of this StorageFlexUtilPhysicalDrive.

        :return: The product_name of this StorageFlexUtilPhysicalDrive.
        :rtype: str
        """
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        """
        Sets the product_name of this StorageFlexUtilPhysicalDrive.

        :param product_name: The product_name of this StorageFlexUtilPhysicalDrive.
        :type: str
        """

        self._product_name = product_name

    @property
    def product_revision(self):
        """
        Gets the product_revision of this StorageFlexUtilPhysicalDrive.

        :return: The product_revision of this StorageFlexUtilPhysicalDrive.
        :rtype: str
        """
        return self._product_revision

    @product_revision.setter
    def product_revision(self, product_revision):
        """
        Sets the product_revision of this StorageFlexUtilPhysicalDrive.

        :param product_revision: The product_revision of this StorageFlexUtilPhysicalDrive.
        :type: str
        """

        self._product_revision = product_revision

    @property
    def read_error_count(self):
        """
        Gets the read_error_count of this StorageFlexUtilPhysicalDrive.

        :return: The read_error_count of this StorageFlexUtilPhysicalDrive.
        :rtype: str
        """
        return self._read_error_count

    @read_error_count.setter
    def read_error_count(self, read_error_count):
        """
        Sets the read_error_count of this StorageFlexUtilPhysicalDrive.

        :param read_error_count: The read_error_count of this StorageFlexUtilPhysicalDrive.
        :type: str
        """

        self._read_error_count = read_error_count

    @property
    def read_error_threshold(self):
        """
        Gets the read_error_threshold of this StorageFlexUtilPhysicalDrive.

        :return: The read_error_threshold of this StorageFlexUtilPhysicalDrive.
        :rtype: str
        """
        return self._read_error_threshold

    @read_error_threshold.setter
    def read_error_threshold(self, read_error_threshold):
        """
        Sets the read_error_threshold of this StorageFlexUtilPhysicalDrive.

        :param read_error_threshold: The read_error_threshold of this StorageFlexUtilPhysicalDrive.
        :type: str
        """

        self._read_error_threshold = read_error_threshold

    @property
    def registered_device(self):
        """
        Gets the registered_device of this StorageFlexUtilPhysicalDrive.

        :return: The registered_device of this StorageFlexUtilPhysicalDrive.
        :rtype: AssetDeviceRegistrationRef
        """
        return self._registered_device

    @registered_device.setter
    def registered_device(self, registered_device):
        """
        Sets the registered_device of this StorageFlexUtilPhysicalDrive.

        :param registered_device: The registered_device of this StorageFlexUtilPhysicalDrive.
        :type: AssetDeviceRegistrationRef
        """

        self._registered_device = registered_device

    @property
    def storage_flex_util_controller(self):
        """
        Gets the storage_flex_util_controller of this StorageFlexUtilPhysicalDrive.

        :return: The storage_flex_util_controller of this StorageFlexUtilPhysicalDrive.
        :rtype: StorageFlexUtilControllerRef
        """
        return self._storage_flex_util_controller

    @storage_flex_util_controller.setter
    def storage_flex_util_controller(self, storage_flex_util_controller):
        """
        Sets the storage_flex_util_controller of this StorageFlexUtilPhysicalDrive.

        :param storage_flex_util_controller: The storage_flex_util_controller of this StorageFlexUtilPhysicalDrive.
        :type: StorageFlexUtilControllerRef
        """

        self._storage_flex_util_controller = storage_flex_util_controller

    @property
    def write_enabled(self):
        """
        Gets the write_enabled of this StorageFlexUtilPhysicalDrive.

        :return: The write_enabled of this StorageFlexUtilPhysicalDrive.
        :rtype: str
        """
        return self._write_enabled

    @write_enabled.setter
    def write_enabled(self, write_enabled):
        """
        Sets the write_enabled of this StorageFlexUtilPhysicalDrive.

        :param write_enabled: The write_enabled of this StorageFlexUtilPhysicalDrive.
        :type: str
        """

        self._write_enabled = write_enabled

    @property
    def write_error_count(self):
        """
        Gets the write_error_count of this StorageFlexUtilPhysicalDrive.

        :return: The write_error_count of this StorageFlexUtilPhysicalDrive.
        :rtype: str
        """
        return self._write_error_count

    @write_error_count.setter
    def write_error_count(self, write_error_count):
        """
        Sets the write_error_count of this StorageFlexUtilPhysicalDrive.

        :param write_error_count: The write_error_count of this StorageFlexUtilPhysicalDrive.
        :type: str
        """

        self._write_error_count = write_error_count

    @property
    def write_error_threshold(self):
        """
        Gets the write_error_threshold of this StorageFlexUtilPhysicalDrive.

        :return: The write_error_threshold of this StorageFlexUtilPhysicalDrive.
        :rtype: str
        """
        return self._write_error_threshold

    @write_error_threshold.setter
    def write_error_threshold(self, write_error_threshold):
        """
        Sets the write_error_threshold of this StorageFlexUtilPhysicalDrive.

        :param write_error_threshold: The write_error_threshold of this StorageFlexUtilPhysicalDrive.
        :type: str
        """

        self._write_error_threshold = write_error_threshold

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
        if not isinstance(other, StorageFlexUtilPhysicalDrive):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
