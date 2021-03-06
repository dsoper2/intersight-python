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


class TamSecurityAdvisoryAllOf(object):
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
        'actions': 'list[TamAction]',
        'advisory_id': 'str',
        'api_data_sources': 'list[TamApiDataSource]',
        'base_score': 'float',
        'cve_ids': 'list[str]',
        'date_published': 'datetime',
        'date_updated': 'datetime',
        'environmental_score': 'float',
        'external_url': 'str',
        'recommendation': 'str',
        'status': 'str',
        'temporal_score': 'float',
        'version': 'str',
        'organization': 'OrganizationOrganization'
    }

    attribute_map = {
        'actions': 'Actions',
        'advisory_id': 'AdvisoryId',
        'api_data_sources': 'ApiDataSources',
        'base_score': 'BaseScore',
        'cve_ids': 'CveIds',
        'date_published': 'DatePublished',
        'date_updated': 'DateUpdated',
        'environmental_score': 'EnvironmentalScore',
        'external_url': 'ExternalUrl',
        'recommendation': 'Recommendation',
        'status': 'Status',
        'temporal_score': 'TemporalScore',
        'version': 'Version',
        'organization': 'Organization'
    }

    def __init__(self,
                 actions=None,
                 advisory_id=None,
                 api_data_sources=None,
                 base_score=None,
                 cve_ids=None,
                 date_published=None,
                 date_updated=None,
                 environmental_score=None,
                 external_url=None,
                 recommendation=None,
                 status='interim',
                 temporal_score=None,
                 version=None,
                 organization=None,
                 local_vars_configuration=None):  # noqa: E501
        """TamSecurityAdvisoryAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._actions = None
        self._advisory_id = None
        self._api_data_sources = None
        self._base_score = None
        self._cve_ids = None
        self._date_published = None
        self._date_updated = None
        self._environmental_score = None
        self._external_url = None
        self._recommendation = None
        self._status = None
        self._temporal_score = None
        self._version = None
        self._organization = None
        self.discriminator = None

        if actions is not None:
            self.actions = actions
        if advisory_id is not None:
            self.advisory_id = advisory_id
        if api_data_sources is not None:
            self.api_data_sources = api_data_sources
        if base_score is not None:
            self.base_score = base_score
        if cve_ids is not None:
            self.cve_ids = cve_ids
        if date_published is not None:
            self.date_published = date_published
        if date_updated is not None:
            self.date_updated = date_updated
        if environmental_score is not None:
            self.environmental_score = environmental_score
        if external_url is not None:
            self.external_url = external_url
        if recommendation is not None:
            self.recommendation = recommendation
        if status is not None:
            self.status = status
        if temporal_score is not None:
            self.temporal_score = temporal_score
        if version is not None:
            self.version = version
        if organization is not None:
            self.organization = organization

    @property
    def actions(self):
        """Gets the actions of this TamSecurityAdvisoryAllOf.  # noqa: E501


        :return: The actions of this TamSecurityAdvisoryAllOf.  # noqa: E501
        :rtype: list[TamAction]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """Sets the actions of this TamSecurityAdvisoryAllOf.


        :param actions: The actions of this TamSecurityAdvisoryAllOf.  # noqa: E501
        :type: list[TamAction]
        """

        self._actions = actions

    @property
    def advisory_id(self):
        """Gets the advisory_id of this TamSecurityAdvisoryAllOf.  # noqa: E501

        Cisco generated identifier for the published security advisory.     # noqa: E501

        :return: The advisory_id of this TamSecurityAdvisoryAllOf.  # noqa: E501
        :rtype: str
        """
        return self._advisory_id

    @advisory_id.setter
    def advisory_id(self, advisory_id):
        """Sets the advisory_id of this TamSecurityAdvisoryAllOf.

        Cisco generated identifier for the published security advisory.     # noqa: E501

        :param advisory_id: The advisory_id of this TamSecurityAdvisoryAllOf.  # noqa: E501
        :type: str
        """

        self._advisory_id = advisory_id

    @property
    def api_data_sources(self):
        """Gets the api_data_sources of this TamSecurityAdvisoryAllOf.  # noqa: E501


        :return: The api_data_sources of this TamSecurityAdvisoryAllOf.  # noqa: E501
        :rtype: list[TamApiDataSource]
        """
        return self._api_data_sources

    @api_data_sources.setter
    def api_data_sources(self, api_data_sources):
        """Sets the api_data_sources of this TamSecurityAdvisoryAllOf.


        :param api_data_sources: The api_data_sources of this TamSecurityAdvisoryAllOf.  # noqa: E501
        :type: list[TamApiDataSource]
        """

        self._api_data_sources = api_data_sources

    @property
    def base_score(self):
        """Gets the base_score of this TamSecurityAdvisoryAllOf.  # noqa: E501

        CVSS version 3 base score for the security Advisory.     # noqa: E501

        :return: The base_score of this TamSecurityAdvisoryAllOf.  # noqa: E501
        :rtype: float
        """
        return self._base_score

    @base_score.setter
    def base_score(self, base_score):
        """Sets the base_score of this TamSecurityAdvisoryAllOf.

        CVSS version 3 base score for the security Advisory.     # noqa: E501

        :param base_score: The base_score of this TamSecurityAdvisoryAllOf.  # noqa: E501
        :type: float
        """

        self._base_score = base_score

    @property
    def cve_ids(self):
        """Gets the cve_ids of this TamSecurityAdvisoryAllOf.  # noqa: E501


        :return: The cve_ids of this TamSecurityAdvisoryAllOf.  # noqa: E501
        :rtype: list[str]
        """
        return self._cve_ids

    @cve_ids.setter
    def cve_ids(self, cve_ids):
        """Sets the cve_ids of this TamSecurityAdvisoryAllOf.


        :param cve_ids: The cve_ids of this TamSecurityAdvisoryAllOf.  # noqa: E501
        :type: list[str]
        """

        self._cve_ids = cve_ids

    @property
    def date_published(self):
        """Gets the date_published of this TamSecurityAdvisoryAllOf.  # noqa: E501

        Date when the security advisory was first published by Cisco.     # noqa: E501

        :return: The date_published of this TamSecurityAdvisoryAllOf.  # noqa: E501
        :rtype: datetime
        """
        return self._date_published

    @date_published.setter
    def date_published(self, date_published):
        """Sets the date_published of this TamSecurityAdvisoryAllOf.

        Date when the security advisory was first published by Cisco.     # noqa: E501

        :param date_published: The date_published of this TamSecurityAdvisoryAllOf.  # noqa: E501
        :type: datetime
        """

        self._date_published = date_published

    @property
    def date_updated(self):
        """Gets the date_updated of this TamSecurityAdvisoryAllOf.  # noqa: E501

        Date when the security advisory was last updated by Cisco.     # noqa: E501

        :return: The date_updated of this TamSecurityAdvisoryAllOf.  # noqa: E501
        :rtype: datetime
        """
        return self._date_updated

    @date_updated.setter
    def date_updated(self, date_updated):
        """Sets the date_updated of this TamSecurityAdvisoryAllOf.

        Date when the security advisory was last updated by Cisco.     # noqa: E501

        :param date_updated: The date_updated of this TamSecurityAdvisoryAllOf.  # noqa: E501
        :type: datetime
        """

        self._date_updated = date_updated

    @property
    def environmental_score(self):
        """Gets the environmental_score of this TamSecurityAdvisoryAllOf.  # noqa: E501

        CVSS version 3 environmental score for the security Advisory.     # noqa: E501

        :return: The environmental_score of this TamSecurityAdvisoryAllOf.  # noqa: E501
        :rtype: float
        """
        return self._environmental_score

    @environmental_score.setter
    def environmental_score(self, environmental_score):
        """Sets the environmental_score of this TamSecurityAdvisoryAllOf.

        CVSS version 3 environmental score for the security Advisory.     # noqa: E501

        :param environmental_score: The environmental_score of this TamSecurityAdvisoryAllOf.  # noqa: E501
        :type: float
        """

        self._environmental_score = environmental_score

    @property
    def external_url(self):
        """Gets the external_url of this TamSecurityAdvisoryAllOf.  # noqa: E501

        A link to an external URL describing security Advisory in more details.     # noqa: E501

        :return: The external_url of this TamSecurityAdvisoryAllOf.  # noqa: E501
        :rtype: str
        """
        return self._external_url

    @external_url.setter
    def external_url(self, external_url):
        """Sets the external_url of this TamSecurityAdvisoryAllOf.

        A link to an external URL describing security Advisory in more details.     # noqa: E501

        :param external_url: The external_url of this TamSecurityAdvisoryAllOf.  # noqa: E501
        :type: str
        """

        self._external_url = external_url

    @property
    def recommendation(self):
        """Gets the recommendation of this TamSecurityAdvisoryAllOf.  # noqa: E501

        Recommended action to resolve the security advisory.     # noqa: E501

        :return: The recommendation of this TamSecurityAdvisoryAllOf.  # noqa: E501
        :rtype: str
        """
        return self._recommendation

    @recommendation.setter
    def recommendation(self, recommendation):
        """Sets the recommendation of this TamSecurityAdvisoryAllOf.

        Recommended action to resolve the security advisory.     # noqa: E501

        :param recommendation: The recommendation of this TamSecurityAdvisoryAllOf.  # noqa: E501
        :type: str
        """

        self._recommendation = recommendation

    @property
    def status(self):
        """Gets the status of this TamSecurityAdvisoryAllOf.  # noqa: E501

        Cisco assigned status of the published advisory based on whether the investigation is complete or on-going.     # noqa: E501

        :return: The status of this TamSecurityAdvisoryAllOf.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TamSecurityAdvisoryAllOf.

        Cisco assigned status of the published advisory based on whether the investigation is complete or on-going.     # noqa: E501

        :param status: The status of this TamSecurityAdvisoryAllOf.  # noqa: E501
        :type: str
        """
        allowed_values = ["interim", "final"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values))

        self._status = status

    @property
    def temporal_score(self):
        """Gets the temporal_score of this TamSecurityAdvisoryAllOf.  # noqa: E501

        CVSS version 3 temporal score for the security Advisory.     # noqa: E501

        :return: The temporal_score of this TamSecurityAdvisoryAllOf.  # noqa: E501
        :rtype: float
        """
        return self._temporal_score

    @temporal_score.setter
    def temporal_score(self, temporal_score):
        """Sets the temporal_score of this TamSecurityAdvisoryAllOf.

        CVSS version 3 temporal score for the security Advisory.     # noqa: E501

        :param temporal_score: The temporal_score of this TamSecurityAdvisoryAllOf.  # noqa: E501
        :type: float
        """

        self._temporal_score = temporal_score

    @property
    def version(self):
        """Gets the version of this TamSecurityAdvisoryAllOf.  # noqa: E501

        Cisco assigned advisory version after latest revision.      # noqa: E501

        :return: The version of this TamSecurityAdvisoryAllOf.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this TamSecurityAdvisoryAllOf.

        Cisco assigned advisory version after latest revision.      # noqa: E501

        :param version: The version of this TamSecurityAdvisoryAllOf.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def organization(self):
        """Gets the organization of this TamSecurityAdvisoryAllOf.  # noqa: E501


        :return: The organization of this TamSecurityAdvisoryAllOf.  # noqa: E501
        :rtype: OrganizationOrganization
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this TamSecurityAdvisoryAllOf.


        :param organization: The organization of this TamSecurityAdvisoryAllOf.  # noqa: E501
        :type: OrganizationOrganization
        """

        self._organization = organization

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
        if not isinstance(other, TamSecurityAdvisoryAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TamSecurityAdvisoryAllOf):
            return True

        return self.to_dict() != other.to_dict()
