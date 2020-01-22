# coding: utf-8

"""
    Intersight REST API

    This is Intersight REST API 

    OpenAPI spec version: 1.0.9-961
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class OsInstall(object):
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
        'domain_group_moid': 'str',
        'mod_time': 'datetime',
        'moid': 'str',
        'object_type': 'str',
        'owners': 'list[str]',
        'parent': 'MoBaseMoRef',
        'shared_scope': 'str',
        'tags': 'list[MoTag]',
        'version_context': 'MoVersionContext',
        'additional_parameters': 'object',
        'answers': 'OsAnswers',
        'description': 'str',
        'install_method': 'str',
        'name': 'str',
        'configuration_file': 'OsConfigurationFileRef',
        'image': 'SoftwarerepositoryOperatingSystemFileRef',
        'organization': 'IamAccountRef',
        'osdu_image': 'FirmwareServerConfigurationUtilityDistributableRef',
        'post_install_scripts': 'list[OsPostInstallScriptRef]',
        'server': 'ComputePhysicalRef',
        'workflow_info': 'WorkflowWorkflowInfoRef'
    }

    attribute_map = {
        'account_moid': 'AccountMoid',
        'ancestors': 'Ancestors',
        'create_time': 'CreateTime',
        'domain_group_moid': 'DomainGroupMoid',
        'mod_time': 'ModTime',
        'moid': 'Moid',
        'object_type': 'ObjectType',
        'owners': 'Owners',
        'parent': 'Parent',
        'shared_scope': 'SharedScope',
        'tags': 'Tags',
        'version_context': 'VersionContext',
        'additional_parameters': 'AdditionalParameters',
        'answers': 'Answers',
        'description': 'Description',
        'install_method': 'InstallMethod',
        'name': 'Name',
        'configuration_file': 'ConfigurationFile',
        'image': 'Image',
        'organization': 'Organization',
        'osdu_image': 'OsduImage',
        'post_install_scripts': 'PostInstallScripts',
        'server': 'Server',
        'workflow_info': 'WorkflowInfo'
    }

    def __init__(self, account_moid=None, ancestors=None, create_time=None, domain_group_moid=None, mod_time=None, moid=None, object_type=None, owners=None, parent=None, shared_scope=None, tags=None, version_context=None, additional_parameters=None, answers=None, description=None, install_method='vMedia', name=None, configuration_file=None, image=None, organization=None, osdu_image=None, post_install_scripts=None, server=None, workflow_info=None):
        """
        OsInstall - a model defined in Swagger
        """

        self._account_moid = None
        self._ancestors = None
        self._create_time = None
        self._domain_group_moid = None
        self._mod_time = None
        self._moid = None
        self._object_type = None
        self._owners = None
        self._parent = None
        self._shared_scope = None
        self._tags = None
        self._version_context = None
        self._additional_parameters = None
        self._answers = None
        self._description = None
        self._install_method = None
        self._name = None
        self._configuration_file = None
        self._image = None
        self._organization = None
        self._osdu_image = None
        self._post_install_scripts = None
        self._server = None
        self._workflow_info = None

        if account_moid is not None:
          self.account_moid = account_moid
        if ancestors is not None:
          self.ancestors = ancestors
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
        if parent is not None:
          self.parent = parent
        if shared_scope is not None:
          self.shared_scope = shared_scope
        if tags is not None:
          self.tags = tags
        if version_context is not None:
          self.version_context = version_context
        if additional_parameters is not None:
          self.additional_parameters = additional_parameters
        if answers is not None:
          self.answers = answers
        if description is not None:
          self.description = description
        if install_method is not None:
          self.install_method = install_method
        if name is not None:
          self.name = name
        if configuration_file is not None:
          self.configuration_file = configuration_file
        if image is not None:
          self.image = image
        if organization is not None:
          self.organization = organization
        if osdu_image is not None:
          self.osdu_image = osdu_image
        if post_install_scripts is not None:
          self.post_install_scripts = post_install_scripts
        if server is not None:
          self.server = server
        if workflow_info is not None:
          self.workflow_info = workflow_info

    @property
    def account_moid(self):
        """
        Gets the account_moid of this OsInstall.
        The Account ID for this managed object.  

        :return: The account_moid of this OsInstall.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this OsInstall.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this OsInstall.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def ancestors(self):
        """
        Gets the ancestors of this OsInstall.
        The array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this OsInstall.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this OsInstall.
        The array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this OsInstall.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def create_time(self):
        """
        Gets the create_time of this OsInstall.
        The time when this managed object was created.  

        :return: The create_time of this OsInstall.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this OsInstall.
        The time when this managed object was created.  

        :param create_time: The create_time of this OsInstall.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def domain_group_moid(self):
        """
        Gets the domain_group_moid of this OsInstall.
        The DomainGroup ID for this managed object.  

        :return: The domain_group_moid of this OsInstall.
        :rtype: str
        """
        return self._domain_group_moid

    @domain_group_moid.setter
    def domain_group_moid(self, domain_group_moid):
        """
        Sets the domain_group_moid of this OsInstall.
        The DomainGroup ID for this managed object.  

        :param domain_group_moid: The domain_group_moid of this OsInstall.
        :type: str
        """

        self._domain_group_moid = domain_group_moid

    @property
    def mod_time(self):
        """
        Gets the mod_time of this OsInstall.
        The time when this managed object was last modified.  

        :return: The mod_time of this OsInstall.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this OsInstall.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this OsInstall.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this OsInstall.
        The unique identifier of this Managed Object instance.  

        :return: The moid of this OsInstall.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this OsInstall.
        The unique identifier of this Managed Object instance.  

        :param moid: The moid of this OsInstall.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this OsInstall.
        The fully-qualified type of this managed object, e.g. the class name.  

        :return: The object_type of this OsInstall.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this OsInstall.
        The fully-qualified type of this managed object, e.g. the class name.  

        :param object_type: The object_type of this OsInstall.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this OsInstall.
        The array of owners which represent effective ownership of this object.   

        :return: The owners of this OsInstall.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this OsInstall.
        The array of owners which represent effective ownership of this object.   

        :param owners: The owners of this OsInstall.
        :type: list[str]
        """

        self._owners = owners

    @property
    def parent(self):
        """
        Gets the parent of this OsInstall.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this OsInstall.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this OsInstall.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this OsInstall.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def shared_scope(self):
        """
        Gets the shared_scope of this OsInstall.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.  

        :return: The shared_scope of this OsInstall.
        :rtype: str
        """
        return self._shared_scope

    @shared_scope.setter
    def shared_scope(self, shared_scope):
        """
        Sets the shared_scope of this OsInstall.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.  

        :param shared_scope: The shared_scope of this OsInstall.
        :type: str
        """

        self._shared_scope = shared_scope

    @property
    def tags(self):
        """
        Gets the tags of this OsInstall.
        The array of tags, which allow to add key, value meta-data to managed objects.  

        :return: The tags of this OsInstall.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this OsInstall.
        The array of tags, which allow to add key, value meta-data to managed objects.  

        :param tags: The tags of this OsInstall.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this OsInstall.
        The versioning info for this managed object.   

        :return: The version_context of this OsInstall.
        :rtype: MoVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this OsInstall.
        The versioning info for this managed object.   

        :param version_context: The version_context of this OsInstall.
        :type: MoVersionContext
        """

        self._version_context = version_context

    @property
    def additional_parameters(self):
        """
        Gets the additional_parameters of this OsInstall.
        If the os.ConfigurationFile MO selected is a template that uses additional placeholders other than the ones provided in standard os.Answers MO, the values for those additional placeholders are provided here.   

        :return: The additional_parameters of this OsInstall.
        :rtype: object
        """
        return self._additional_parameters

    @additional_parameters.setter
    def additional_parameters(self, additional_parameters):
        """
        Sets the additional_parameters of this OsInstall.
        If the os.ConfigurationFile MO selected is a template that uses additional placeholders other than the ones provided in standard os.Answers MO, the values for those additional placeholders are provided here.   

        :param additional_parameters: The additional_parameters of this OsInstall.
        :type: object
        """

        self._additional_parameters = additional_parameters

    @property
    def answers(self):
        """
        Gets the answers of this OsInstall.
        Answers provided by user for the unattended OS installation.   

        :return: The answers of this OsInstall.
        :rtype: OsAnswers
        """
        return self._answers

    @answers.setter
    def answers(self, answers):
        """
        Sets the answers of this OsInstall.
        Answers provided by user for the unattended OS installation.   

        :param answers: The answers of this OsInstall.
        :type: OsAnswers
        """

        self._answers = answers

    @property
    def description(self):
        """
        Gets the description of this OsInstall.
        User provided description about the OS install configuration.   

        :return: The description of this OsInstall.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this OsInstall.
        User provided description about the OS install configuration.   

        :param description: The description of this OsInstall.
        :type: str
        """

        self._description = description

    @property
    def install_method(self):
        """
        Gets the install_method of this OsInstall.
        The install method to be used for OS installation - vMedia, iPXE.  Only vMedia is supported as of now.   

        :return: The install_method of this OsInstall.
        :rtype: str
        """
        return self._install_method

    @install_method.setter
    def install_method(self, install_method):
        """
        Sets the install_method of this OsInstall.
        The install method to be used for OS installation - vMedia, iPXE.  Only vMedia is supported as of now.   

        :param install_method: The install_method of this OsInstall.
        :type: str
        """
        allowed_values = ["vMedia"]
        if install_method not in allowed_values:
            raise ValueError(
                "Invalid value for `install_method` ({0}), must be one of {1}"
                .format(install_method, allowed_values)
            )

        self._install_method = install_method

    @property
    def name(self):
        """
        Gets the name of this OsInstall.
        The name of the OS install configuration.     

        :return: The name of this OsInstall.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this OsInstall.
        The name of the OS install configuration.     

        :param name: The name of this OsInstall.
        :type: str
        """

        self._name = name

    @property
    def configuration_file(self):
        """
        Gets the configuration_file of this OsInstall.
        If the answers source is selected as 'Template' in 'Answers' property, this relation provides the os.ConfigurationFile instance to be used for this OS install. 

        :return: The configuration_file of this OsInstall.
        :rtype: OsConfigurationFileRef
        """
        return self._configuration_file

    @configuration_file.setter
    def configuration_file(self, configuration_file):
        """
        Sets the configuration_file of this OsInstall.
        If the answers source is selected as 'Template' in 'Answers' property, this relation provides the os.ConfigurationFile instance to be used for this OS install. 

        :param configuration_file: The configuration_file of this OsInstall.
        :type: OsConfigurationFileRef
        """

        self._configuration_file = configuration_file

    @property
    def image(self):
        """
        Gets the image of this OsInstall.
        OS Image to be installed as part of this OS installation. 

        :return: The image of this OsInstall.
        :rtype: SoftwarerepositoryOperatingSystemFileRef
        """
        return self._image

    @image.setter
    def image(self, image):
        """
        Sets the image of this OsInstall.
        OS Image to be installed as part of this OS installation. 

        :param image: The image of this OsInstall.
        :type: SoftwarerepositoryOperatingSystemFileRef
        """

        self._image = image

    @property
    def organization(self):
        """
        Gets the organization of this OsInstall.
        Relationship to the Organization that owns the Managed Object. 

        :return: The organization of this OsInstall.
        :rtype: IamAccountRef
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """
        Sets the organization of this OsInstall.
        Relationship to the Organization that owns the Managed Object. 

        :param organization: The organization of this OsInstall.
        :type: IamAccountRef
        """

        self._organization = organization

    @property
    def osdu_image(self):
        """
        Gets the osdu_image of this OsInstall.
        Location of the Intersight OS Deployment Utilityimage, if the user has downloaded and available locally, to be used for this OS install configuration. This image is applicable for vMedia install method. Cisco publishes a OS Deployment Utility image that bootstraps and installs the user provided operating system images along with answers for unattended instllation. If this property is empty for vMedia install type, the image hosted in Intersight image repository will be used. Note that in this case, the image will be downloaded from Intersight in every target server every time. 

        :return: The osdu_image of this OsInstall.
        :rtype: FirmwareServerConfigurationUtilityDistributableRef
        """
        return self._osdu_image

    @osdu_image.setter
    def osdu_image(self, osdu_image):
        """
        Sets the osdu_image of this OsInstall.
        Location of the Intersight OS Deployment Utilityimage, if the user has downloaded and available locally, to be used for this OS install configuration. This image is applicable for vMedia install method. Cisco publishes a OS Deployment Utility image that bootstraps and installs the user provided operating system images along with answers for unattended instllation. If this property is empty for vMedia install type, the image hosted in Intersight image repository will be used. Note that in this case, the image will be downloaded from Intersight in every target server every time. 

        :param osdu_image: The osdu_image of this OsInstall.
        :type: FirmwareServerConfigurationUtilityDistributableRef
        """

        self._osdu_image = osdu_image

    @property
    def post_install_scripts(self):
        """
        Gets the post_install_scripts of this OsInstall.
        Post Install Scripts to be executed specified in order. 

        :return: The post_install_scripts of this OsInstall.
        :rtype: list[OsPostInstallScriptRef]
        """
        return self._post_install_scripts

    @post_install_scripts.setter
    def post_install_scripts(self, post_install_scripts):
        """
        Sets the post_install_scripts of this OsInstall.
        Post Install Scripts to be executed specified in order. 

        :param post_install_scripts: The post_install_scripts of this OsInstall.
        :type: list[OsPostInstallScriptRef]
        """

        self._post_install_scripts = post_install_scripts

    @property
    def server(self):
        """
        Gets the server of this OsInstall.
        This relation provides the target server in which the OS is to be installed. 

        :return: The server of this OsInstall.
        :rtype: ComputePhysicalRef
        """
        return self._server

    @server.setter
    def server(self, server):
        """
        Sets the server of this OsInstall.
        This relation provides the target server in which the OS is to be installed. 

        :param server: The server of this OsInstall.
        :type: ComputePhysicalRef
        """

        self._server = server

    @property
    def workflow_info(self):
        """
        Gets the workflow_info of this OsInstall.
        This relation is populated with the reference of OS install workflow started for this request. This workflow info MO shall be used for tracking further status and completion. 

        :return: The workflow_info of this OsInstall.
        :rtype: WorkflowWorkflowInfoRef
        """
        return self._workflow_info

    @workflow_info.setter
    def workflow_info(self, workflow_info):
        """
        Sets the workflow_info of this OsInstall.
        This relation is populated with the reference of OS install workflow started for this request. This workflow info MO shall be used for tracking further status and completion. 

        :param workflow_info: The workflow_info of this OsInstall.
        :type: WorkflowWorkflowInfoRef
        """

        self._workflow_info = workflow_info

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
        if not isinstance(other, OsInstall):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other