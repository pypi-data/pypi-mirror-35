# coding: utf-8

"""
Copyright 2015 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from datetime import datetime
from pprint import pformat
from six import iteritems


class RepositoryCreationResultRest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        RepositoryCreationResultRest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'repository_id': 'int',
            'build_configuration_id': 'int'
        }

        self.attribute_map = {
            'repository_id': 'repositoryId',
            'build_configuration_id': 'buildConfigurationId'
        }

        self._repository_id = None
        self._build_configuration_id = None

    @property
    def repository_id(self):
        """
        Gets the repository_id of this RepositoryCreationResultRest.


        :return: The repository_id of this RepositoryCreationResultRest.
        :rtype: int
        """
        return self._repository_id

    @repository_id.setter
    def repository_id(self, repository_id):
        """
        Sets the repository_id of this RepositoryCreationResultRest.


        :param repository_id: The repository_id of this RepositoryCreationResultRest.
        :type: int
        """
        self._repository_id = repository_id

    @property
    def build_configuration_id(self):
        """
        Gets the build_configuration_id of this RepositoryCreationResultRest.


        :return: The build_configuration_id of this RepositoryCreationResultRest.
        :rtype: int
        """
        return self._build_configuration_id

    @build_configuration_id.setter
    def build_configuration_id(self, build_configuration_id):
        """
        Sets the build_configuration_id of this RepositoryCreationResultRest.


        :param build_configuration_id: The build_configuration_id of this RepositoryCreationResultRest.
        :type: int
        """
        self._build_configuration_id = build_configuration_id

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
	    elif isinstance(value, datetime):
		result[attr] = str(value.date())
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
