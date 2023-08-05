# coding: utf-8

"""
    Fortanix SDKMS REST API

    This is a set of REST APIs for accessing the Fortanix Self-Defending Key Management System. This includes APIs for managing accounts, and for performing cryptographic and key management operations. 

    OpenAPI spec version: 1.0.0-20171218
    Contact: support@fortanix.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at
    
        http://www.apache.org/licenses/LICENSE-2.0
    
    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""


from pprint import pformat
from six import iteritems
import re




# NOTE: This class is auto generated by the swagger code generator program.
# Do not edit the class manually.
class GoogleServiceAccountKey(object):
    """
    @undocumented: swagger_types
    @undocumented: attribute_map
    @undocumented: to_dict
    @undocumented: to_str
    @undocumented: __repr__
    @undocumented: __eq__
    @undocumented: __ne__
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'type': 'str',
        'project_id': 'str',
        'private_key_id': 'str',
        'private_key': 'str',
        'client_email': 'str'
    }

    attribute_map = {
        'type': 'type',
        'project_id': 'project_id',
        'private_key_id': 'private_key_id',
        'private_key': 'private_key',
        'client_email': 'client_email'
    }

    def __init__(self, type=None, project_id=None, private_key_id=None, private_key=None, client_email=None):
        """
        GoogleServiceAccountKey - a model defined in Swagger
        """

        self._type = None
        self._project_id = None
        self._private_key_id = None
        self._private_key = None
        self._client_email = None

        self.type = type
        self.project_id = project_id
        self.private_key_id = private_key_id
        if private_key is not None:
          self.private_key = private_key
        self.client_email = client_email

    @property
    def type(self):
        """
        Gets the type of this GoogleServiceAccountKey.
        Must be \"service_account\"

        Type: L{str}
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this GoogleServiceAccountKey.
        Must be \"service_account\"
        """

        self._type = type

    @property
    def project_id(self):
        """
        Gets the project_id of this GoogleServiceAccountKey.

        Type: L{str}
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """
        Sets the project_id of this GoogleServiceAccountKey.
        """

        self._project_id = project_id

    @property
    def private_key_id(self):
        """
        Gets the private_key_id of this GoogleServiceAccountKey.

        Type: L{str}
        """
        return self._private_key_id

    @private_key_id.setter
    def private_key_id(self, private_key_id):
        """
        Sets the private_key_id of this GoogleServiceAccountKey.
        """

        self._private_key_id = private_key_id

    @property
    def private_key(self):
        """
        Gets the private_key of this GoogleServiceAccountKey.

        Type: L{str}
        """
        return self._private_key

    @private_key.setter
    def private_key(self, private_key):
        """
        Sets the private_key of this GoogleServiceAccountKey.
        """

        self._private_key = private_key

    @property
    def client_email(self):
        """
        Gets the client_email of this GoogleServiceAccountKey.

        Type: L{str}
        """
        return self._client_email

    @client_email.setter
    def client_email(self, client_email):
        """
        Sets the client_email of this GoogleServiceAccountKey.
        """

        self._client_email = client_email

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
        if not isinstance(other, GoogleServiceAccountKey):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

