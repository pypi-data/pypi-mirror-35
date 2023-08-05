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
class DeriveKeyRequestEx(object):
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
        'key': 'SobjectDescriptor',
        'name': 'str',
        'group_id': 'str',
        'key_size': 'int',
        'key_type': 'ObjectType',
        'mechanism': 'DeriveKeyMechanism',
        'enabled': 'bool',
        'description': 'str',
        'key_ops': 'list[KeyOperations]',
        'custom_metadata': 'dict(str, str)',
        'transient': 'bool'
    }

    attribute_map = {
        'key': 'key',
        'name': 'name',
        'group_id': 'group_id',
        'key_size': 'key_size',
        'key_type': 'key_type',
        'mechanism': 'mechanism',
        'enabled': 'enabled',
        'description': 'description',
        'key_ops': 'key_ops',
        'custom_metadata': 'custom_metadata',
        'transient': 'transient'
    }

    def __init__(self, key=None, name=None, group_id=None, key_size=None, key_type=None, mechanism=None, enabled=None, description=None, key_ops=None, custom_metadata=None, transient=None):
        """
        DeriveKeyRequestEx - a model defined in Swagger
        """

        self._key = None
        self._name = None
        self._group_id = None
        self._key_size = None
        self._key_type = None
        self._mechanism = None
        self._enabled = None
        self._description = None
        self._key_ops = None
        self._custom_metadata = None
        self._transient = None

        self.key = key
        self.name = name
        if group_id is not None:
          self.group_id = group_id
        self.key_size = key_size
        self.key_type = key_type
        self.mechanism = mechanism
        if enabled is not None:
          self.enabled = enabled
        if description is not None:
          self.description = description
        if key_ops is not None:
          self.key_ops = key_ops
        if custom_metadata is not None:
          self.custom_metadata = custom_metadata
        if transient is not None:
          self.transient = transient

    @property
    def key(self):
        """
        Gets the key of this DeriveKeyRequestEx.

        Type: L{SobjectDescriptor}
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this DeriveKeyRequestEx.
        """

        self._key = key

    @property
    def name(self):
        """
        Gets the name of this DeriveKeyRequestEx.
        Name of the derived key. Key names must be unique within an account.

        Type: L{str}
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this DeriveKeyRequestEx.
        Name of the derived key. Key names must be unique within an account.
        """

        self._name = name

    @property
    def group_id(self):
        """
        Gets the group_id of this DeriveKeyRequestEx.
        Group ID (not name) of the security group that this security object should belong to. The user or application creating this security object must be a member of this group. If no group is specified, the default group for the user or application will be used. 

        Type: L{str}
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """
        Sets the group_id of this DeriveKeyRequestEx.
        Group ID (not name) of the security group that this security object should belong to. The user or application creating this security object must be a member of this group. If no group is specified, the default group for the user or application will be used. 
        """

        self._group_id = group_id

    @property
    def key_size(self):
        """
        Gets the key_size of this DeriveKeyRequestEx.
        Key size of the derived key in bits (not bytes).

        Type: L{int}
        """
        return self._key_size

    @key_size.setter
    def key_size(self, key_size):
        """
        Sets the key_size of this DeriveKeyRequestEx.
        Key size of the derived key in bits (not bytes).
        """

        self._key_size = key_size

    @property
    def key_type(self):
        """
        Gets the key_type of this DeriveKeyRequestEx.

        Type: L{ObjectType}
        """
        return self._key_type

    @key_type.setter
    def key_type(self, key_type):
        """
        Sets the key_type of this DeriveKeyRequestEx.
        """

        self._key_type = key_type

    @property
    def mechanism(self):
        """
        Gets the mechanism of this DeriveKeyRequestEx.

        Type: L{DeriveKeyMechanism}
        """
        return self._mechanism

    @mechanism.setter
    def mechanism(self, mechanism):
        """
        Sets the mechanism of this DeriveKeyRequestEx.
        """

        self._mechanism = mechanism

    @property
    def enabled(self):
        """
        Gets the enabled of this DeriveKeyRequestEx.
        Whether the derived key should have cryptographic operations enabled.

        Type: L{bool}
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this DeriveKeyRequestEx.
        Whether the derived key should have cryptographic operations enabled.
        """

        self._enabled = enabled

    @property
    def description(self):
        """
        Gets the description of this DeriveKeyRequestEx.
        Description for the new key.

        Type: L{str}
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this DeriveKeyRequestEx.
        Description for the new key.
        """

        self._description = description

    @property
    def key_ops(self):
        """
        Gets the key_ops of this DeriveKeyRequestEx.
        Optional array of key operations to be enabled for this security object. If this property is not provided, the SDKMS server will provide a default set of key operations. Note that if you provide an empty array, all key operations will be disabled. 

        Type: list[L{KeyOperations}]
        """
        return self._key_ops

    @key_ops.setter
    def key_ops(self, key_ops):
        """
        Sets the key_ops of this DeriveKeyRequestEx.
        Optional array of key operations to be enabled for this security object. If this property is not provided, the SDKMS server will provide a default set of key operations. Note that if you provide an empty array, all key operations will be disabled. 
        """

        self._key_ops = key_ops

    @property
    def custom_metadata(self):
        """
        Gets the custom_metadata of this DeriveKeyRequestEx.
        User-defined metadata for this key. Stored as key-value pairs.

        Type: map[L{str}]
        """
        return self._custom_metadata

    @custom_metadata.setter
    def custom_metadata(self, custom_metadata):
        """
        Sets the custom_metadata of this DeriveKeyRequestEx.
        User-defined metadata for this key. Stored as key-value pairs.
        """

        self._custom_metadata = custom_metadata

    @property
    def transient(self):
        """
        Gets the transient of this DeriveKeyRequestEx.
        If this is true, SDKMS will derive a transient key.

        Type: L{bool}
        """
        return self._transient

    @transient.setter
    def transient(self, transient):
        """
        Sets the transient of this DeriveKeyRequestEx.
        If this is true, SDKMS will derive a transient key.
        """

        self._transient = transient

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
        if not isinstance(other, DeriveKeyRequestEx):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

