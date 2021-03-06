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


class StoragePureProtectionGroup(object):
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
        'create_time': 'datetime',
        'domain_group_moid': 'str',
        'mod_time': 'datetime',
        'moid': 'str',
        'object_type': 'str',
        'owners': 'list[str]',
        'shared_scope': 'str',
        'tags': 'list[MoTag]',
        'version_context': 'MoVersionContext',
        'ancestors': 'list[MoBaseMoRef]',
        'parent': 'MoBaseMoRef',
        'permission_resources': 'list[MoBaseMoRef]',
        'name': 'str',
        'prefix': 'str',
        'replication_enabled': 'bool',
        'snapshot_enabled': 'bool',
        'storage_array': 'StorageGenericArrayRef',
        'size': 'int',
        'source': 'str',
        'targets': 'list[str]',
        'host_groups': 'list[StoragePureHostRef]',
        'hosts': 'list[StoragePureHostRef]',
        'registered_device': 'AssetDeviceRegistrationRef',
        'volumes': 'list[StoragePureVolumeRef]'
    }

    attribute_map = {
        'account_moid': 'AccountMoid',
        'create_time': 'CreateTime',
        'domain_group_moid': 'DomainGroupMoid',
        'mod_time': 'ModTime',
        'moid': 'Moid',
        'object_type': 'ObjectType',
        'owners': 'Owners',
        'shared_scope': 'SharedScope',
        'tags': 'Tags',
        'version_context': 'VersionContext',
        'ancestors': 'Ancestors',
        'parent': 'Parent',
        'permission_resources': 'PermissionResources',
        'name': 'Name',
        'prefix': 'Prefix',
        'replication_enabled': 'ReplicationEnabled',
        'snapshot_enabled': 'SnapshotEnabled',
        'storage_array': 'StorageArray',
        'size': 'Size',
        'source': 'Source',
        'targets': 'Targets',
        'host_groups': 'HostGroups',
        'hosts': 'Hosts',
        'registered_device': 'RegisteredDevice',
        'volumes': 'Volumes'
    }

    def __init__(self, account_moid=None, create_time=None, domain_group_moid=None, mod_time=None, moid=None, object_type=None, owners=None, shared_scope=None, tags=None, version_context=None, ancestors=None, parent=None, permission_resources=None, name=None, prefix=None, replication_enabled=None, snapshot_enabled=None, storage_array=None, size=None, source=None, targets=None, host_groups=None, hosts=None, registered_device=None, volumes=None):
        """
        StoragePureProtectionGroup - a model defined in Swagger
        """

        self._account_moid = None
        self._create_time = None
        self._domain_group_moid = None
        self._mod_time = None
        self._moid = None
        self._object_type = None
        self._owners = None
        self._shared_scope = None
        self._tags = None
        self._version_context = None
        self._ancestors = None
        self._parent = None
        self._permission_resources = None
        self._name = None
        self._prefix = None
        self._replication_enabled = None
        self._snapshot_enabled = None
        self._storage_array = None
        self._size = None
        self._source = None
        self._targets = None
        self._host_groups = None
        self._hosts = None
        self._registered_device = None
        self._volumes = None

        if account_moid is not None:
          self.account_moid = account_moid
        if create_time is not None:
          self.create_time = create_time
        if domain_group_moid is not None:
          self.domain_group_moid = domain_group_moid
        if mod_time is not None:
          self.mod_time = mod_time
        if moid is not None:
          self.moid = moid
        if object_type is not None:
          self.object_type = object_type
        if owners is not None:
          self.owners = owners
        if shared_scope is not None:
          self.shared_scope = shared_scope
        if tags is not None:
          self.tags = tags
        if version_context is not None:
          self.version_context = version_context
        if ancestors is not None:
          self.ancestors = ancestors
        if parent is not None:
          self.parent = parent
        if permission_resources is not None:
          self.permission_resources = permission_resources
        if name is not None:
          self.name = name
        if prefix is not None:
          self.prefix = prefix
        if replication_enabled is not None:
          self.replication_enabled = replication_enabled
        if snapshot_enabled is not None:
          self.snapshot_enabled = snapshot_enabled
        if storage_array is not None:
          self.storage_array = storage_array
        if size is not None:
          self.size = size
        if source is not None:
          self.source = source
        if targets is not None:
          self.targets = targets
        if host_groups is not None:
          self.host_groups = host_groups
        if hosts is not None:
          self.hosts = hosts
        if registered_device is not None:
          self.registered_device = registered_device
        if volumes is not None:
          self.volumes = volumes

    @property
    def account_moid(self):
        """
        Gets the account_moid of this StoragePureProtectionGroup.
        The Account ID for this managed object.

        :return: The account_moid of this StoragePureProtectionGroup.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this StoragePureProtectionGroup.
        The Account ID for this managed object.

        :param account_moid: The account_moid of this StoragePureProtectionGroup.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def create_time(self):
        """
        Gets the create_time of this StoragePureProtectionGroup.
        The time when this managed object was created.

        :return: The create_time of this StoragePureProtectionGroup.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this StoragePureProtectionGroup.
        The time when this managed object was created.

        :param create_time: The create_time of this StoragePureProtectionGroup.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def domain_group_moid(self):
        """
        Gets the domain_group_moid of this StoragePureProtectionGroup.
        The DomainGroup ID for this managed object.

        :return: The domain_group_moid of this StoragePureProtectionGroup.
        :rtype: str
        """
        return self._domain_group_moid

    @domain_group_moid.setter
    def domain_group_moid(self, domain_group_moid):
        """
        Sets the domain_group_moid of this StoragePureProtectionGroup.
        The DomainGroup ID for this managed object.

        :param domain_group_moid: The domain_group_moid of this StoragePureProtectionGroup.
        :type: str
        """

        self._domain_group_moid = domain_group_moid

    @property
    def mod_time(self):
        """
        Gets the mod_time of this StoragePureProtectionGroup.
        The time when this managed object was last modified.

        :return: The mod_time of this StoragePureProtectionGroup.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this StoragePureProtectionGroup.
        The time when this managed object was last modified.

        :param mod_time: The mod_time of this StoragePureProtectionGroup.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this StoragePureProtectionGroup.
        The unique identifier of this Managed Object instance.

        :return: The moid of this StoragePureProtectionGroup.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this StoragePureProtectionGroup.
        The unique identifier of this Managed Object instance.

        :param moid: The moid of this StoragePureProtectionGroup.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this StoragePureProtectionGroup.
        The fully-qualified type of this managed object, i.e. the class name. This property is optional. The ObjectType is implied from the URL path. If specified, the value of objectType must match the class name specified in the URL path.

        :return: The object_type of this StoragePureProtectionGroup.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this StoragePureProtectionGroup.
        The fully-qualified type of this managed object, i.e. the class name. This property is optional. The ObjectType is implied from the URL path. If specified, the value of objectType must match the class name specified in the URL path.

        :param object_type: The object_type of this StoragePureProtectionGroup.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this StoragePureProtectionGroup.
        The array of owners which represent effective ownership of this object.

        :return: The owners of this StoragePureProtectionGroup.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this StoragePureProtectionGroup.
        The array of owners which represent effective ownership of this object.

        :param owners: The owners of this StoragePureProtectionGroup.
        :type: list[str]
        """

        self._owners = owners

    @property
    def shared_scope(self):
        """
        Gets the shared_scope of this StoragePureProtectionGroup.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.

        :return: The shared_scope of this StoragePureProtectionGroup.
        :rtype: str
        """
        return self._shared_scope

    @shared_scope.setter
    def shared_scope(self, shared_scope):
        """
        Sets the shared_scope of this StoragePureProtectionGroup.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.

        :param shared_scope: The shared_scope of this StoragePureProtectionGroup.
        :type: str
        """

        self._shared_scope = shared_scope

    @property
    def tags(self):
        """
        Gets the tags of this StoragePureProtectionGroup.
        The array of tags, which allow to add key, value meta-data to managed objects.

        :return: The tags of this StoragePureProtectionGroup.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this StoragePureProtectionGroup.
        The array of tags, which allow to add key, value meta-data to managed objects.

        :param tags: The tags of this StoragePureProtectionGroup.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this StoragePureProtectionGroup.
        The versioning info for this managed object.

        :return: The version_context of this StoragePureProtectionGroup.
        :rtype: MoVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this StoragePureProtectionGroup.
        The versioning info for this managed object.

        :param version_context: The version_context of this StoragePureProtectionGroup.
        :type: MoVersionContext
        """

        self._version_context = version_context

    @property
    def ancestors(self):
        """
        Gets the ancestors of this StoragePureProtectionGroup.
        The array containing the MO references of the ancestors in the object containment hierarchy.

        :return: The ancestors of this StoragePureProtectionGroup.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this StoragePureProtectionGroup.
        The array containing the MO references of the ancestors in the object containment hierarchy.

        :param ancestors: The ancestors of this StoragePureProtectionGroup.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def parent(self):
        """
        Gets the parent of this StoragePureProtectionGroup.
        The direct ancestor of this managed object in the containment hierarchy.

        :return: The parent of this StoragePureProtectionGroup.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this StoragePureProtectionGroup.
        The direct ancestor of this managed object in the containment hierarchy.

        :param parent: The parent of this StoragePureProtectionGroup.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def permission_resources(self):
        """
        Gets the permission_resources of this StoragePureProtectionGroup.
        A slice of all permission resources (organizations) associated with this object. Permission ties resources and its associated roles/privileges. These resources which can be specified in a permission is PermissionResource. Currently only organizations can be specified in permission. All logical and physical resources part of an organization will have organization in PermissionResources field. If DeviceRegistration contains another DeviceRegistration and if parent is in org1 and child is part of org2, then child objects will have PermissionResources as org1 and org2. Parent Objects will have PermissionResources as org1. All profiles/policies created with in an organization will have the organization as PermissionResources.

        :return: The permission_resources of this StoragePureProtectionGroup.
        :rtype: list[MoBaseMoRef]
        """
        return self._permission_resources

    @permission_resources.setter
    def permission_resources(self, permission_resources):
        """
        Sets the permission_resources of this StoragePureProtectionGroup.
        A slice of all permission resources (organizations) associated with this object. Permission ties resources and its associated roles/privileges. These resources which can be specified in a permission is PermissionResource. Currently only organizations can be specified in permission. All logical and physical resources part of an organization will have organization in PermissionResources field. If DeviceRegistration contains another DeviceRegistration and if parent is in org1 and child is part of org2, then child objects will have PermissionResources as org1 and org2. Parent Objects will have PermissionResources as org1. All profiles/policies created with in an organization will have the organization as PermissionResources.

        :param permission_resources: The permission_resources of this StoragePureProtectionGroup.
        :type: list[MoBaseMoRef]
        """

        self._permission_resources = permission_resources

    @property
    def name(self):
        """
        Gets the name of this StoragePureProtectionGroup.
        Name of the protection Group.

        :return: The name of this StoragePureProtectionGroup.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this StoragePureProtectionGroup.
        Name of the protection Group.

        :param name: The name of this StoragePureProtectionGroup.
        :type: str
        """

        self._name = name

    @property
    def prefix(self):
        """
        Gets the prefix of this StoragePureProtectionGroup.
        Prefix used for all generated snapshots from the protection group.

        :return: The prefix of this StoragePureProtectionGroup.
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        """
        Sets the prefix of this StoragePureProtectionGroup.
        Prefix used for all generated snapshots from the protection group.

        :param prefix: The prefix of this StoragePureProtectionGroup.
        :type: str
        """

        self._prefix = prefix

    @property
    def replication_enabled(self):
        """
        Gets the replication_enabled of this StoragePureProtectionGroup.
        Flag to determine if the replication is enabled. Snapshots are created on target array if the flag is set.

        :return: The replication_enabled of this StoragePureProtectionGroup.
        :rtype: bool
        """
        return self._replication_enabled

    @replication_enabled.setter
    def replication_enabled(self, replication_enabled):
        """
        Sets the replication_enabled of this StoragePureProtectionGroup.
        Flag to determine if the replication is enabled. Snapshots are created on target array if the flag is set.

        :param replication_enabled: The replication_enabled of this StoragePureProtectionGroup.
        :type: bool
        """

        self._replication_enabled = replication_enabled

    @property
    def snapshot_enabled(self):
        """
        Gets the snapshot_enabled of this StoragePureProtectionGroup.
        Flag to determine if the snapshot is enabled. Snapshots are created on local array if the flag is set.

        :return: The snapshot_enabled of this StoragePureProtectionGroup.
        :rtype: bool
        """
        return self._snapshot_enabled

    @snapshot_enabled.setter
    def snapshot_enabled(self, snapshot_enabled):
        """
        Sets the snapshot_enabled of this StoragePureProtectionGroup.
        Flag to determine if the snapshot is enabled. Snapshots are created on local array if the flag is set.

        :param snapshot_enabled: The snapshot_enabled of this StoragePureProtectionGroup.
        :type: bool
        """

        self._snapshot_enabled = snapshot_enabled

    @property
    def storage_array(self):
        """
        Gets the storage_array of this StoragePureProtectionGroup.
        Storage array managed object.

        :return: The storage_array of this StoragePureProtectionGroup.
        :rtype: StorageGenericArrayRef
        """
        return self._storage_array

    @storage_array.setter
    def storage_array(self, storage_array):
        """
        Sets the storage_array of this StoragePureProtectionGroup.
        Storage array managed object.

        :param storage_array: The storage_array of this StoragePureProtectionGroup.
        :type: StorageGenericArrayRef
        """

        self._storage_array = storage_array

    @property
    def size(self):
        """
        Gets the size of this StoragePureProtectionGroup.
        Overall size of all snapshots in the protection group, represented in bytes.

        :return: The size of this StoragePureProtectionGroup.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """
        Sets the size of this StoragePureProtectionGroup.
        Overall size of all snapshots in the protection group, represented in bytes.

        :param size: The size of this StoragePureProtectionGroup.
        :type: int
        """

        self._size = size

    @property
    def source(self):
        """
        Gets the source of this StoragePureProtectionGroup.
        Name of PureStorage array name on which the protection group is created.

        :return: The source of this StoragePureProtectionGroup.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """
        Sets the source of this StoragePureProtectionGroup.
        Name of PureStorage array name on which the protection group is created.

        :param source: The source of this StoragePureProtectionGroup.
        :type: str
        """

        self._source = source

    @property
    def targets(self):
        """
        Gets the targets of this StoragePureProtectionGroup.
        Target PureStorage array names where the replication snapshots are created.

        :return: The targets of this StoragePureProtectionGroup.
        :rtype: list[str]
        """
        return self._targets

    @targets.setter
    def targets(self, targets):
        """
        Sets the targets of this StoragePureProtectionGroup.
        Target PureStorage array names where the replication snapshots are created.

        :param targets: The targets of this StoragePureProtectionGroup.
        :type: list[str]
        """

        self._targets = targets

    @property
    def host_groups(self):
        """
        Gets the host_groups of this StoragePureProtectionGroup.
        List of host group object associated to the protection group.

        :return: The host_groups of this StoragePureProtectionGroup.
        :rtype: list[StoragePureHostRef]
        """
        return self._host_groups

    @host_groups.setter
    def host_groups(self, host_groups):
        """
        Sets the host_groups of this StoragePureProtectionGroup.
        List of host group object associated to the protection group.

        :param host_groups: The host_groups of this StoragePureProtectionGroup.
        :type: list[StoragePureHostRef]
        """

        self._host_groups = host_groups

    @property
    def hosts(self):
        """
        Gets the hosts of this StoragePureProtectionGroup.
        List of host object associated to the protection group.

        :return: The hosts of this StoragePureProtectionGroup.
        :rtype: list[StoragePureHostRef]
        """
        return self._hosts

    @hosts.setter
    def hosts(self, hosts):
        """
        Sets the hosts of this StoragePureProtectionGroup.
        List of host object associated to the protection group.

        :param hosts: The hosts of this StoragePureProtectionGroup.
        :type: list[StoragePureHostRef]
        """

        self._hosts = hosts

    @property
    def registered_device(self):
        """
        Gets the registered_device of this StoragePureProtectionGroup.
        Device registration managed object that represents this storage array connection to Intersight.

        :return: The registered_device of this StoragePureProtectionGroup.
        :rtype: AssetDeviceRegistrationRef
        """
        return self._registered_device

    @registered_device.setter
    def registered_device(self, registered_device):
        """
        Sets the registered_device of this StoragePureProtectionGroup.
        Device registration managed object that represents this storage array connection to Intersight.

        :param registered_device: The registered_device of this StoragePureProtectionGroup.
        :type: AssetDeviceRegistrationRef
        """

        self._registered_device = registered_device

    @property
    def volumes(self):
        """
        Gets the volumes of this StoragePureProtectionGroup.
        List of volume object associated to the protection group.

        :return: The volumes of this StoragePureProtectionGroup.
        :rtype: list[StoragePureVolumeRef]
        """
        return self._volumes

    @volumes.setter
    def volumes(self, volumes):
        """
        Sets the volumes of this StoragePureProtectionGroup.
        List of volume object associated to the protection group.

        :param volumes: The volumes of this StoragePureProtectionGroup.
        :type: list[StoragePureVolumeRef]
        """

        self._volumes = volumes

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
        if not isinstance(other, StoragePureProtectionGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
