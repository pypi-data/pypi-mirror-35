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

from .base_enum_object import BaseEnumObject

# NOTE: This class is auto generated by the swagger code generator program.
# Do not edit the class manually.
class PluginType(BaseEnumObject):
    """
    Type of this plugin.

    Enumeration values::
        PluginType.STANDARD = "Standard"
        PluginType.IMPERSONATING = "Impersonating"
        PluginType.CUSTOMALGORITHM = "CustomAlgorithm"

    This class doesnt use python standard enumeration since they dont support unknown values. 
    
    This is an object of type BaseEnumObject and provides similar functionality as a String Enumeration.
    
    Get a standard instance of enum: PluginType.FOO or PluginType("FOO")
    Get non standard instance of enum: PluginType("BAR")
    Enum instance to String value: PluginType.FOO.value , PluginType.FOO.name (Gives "FOO")
    Equality: PluginType.FOO == PluginType("FOO") , PluginType.FOO != PluginType.BAR
    Provides str func:  str(PluginType.FOO) == "PluginType.FOO"
    
    Also the class maintains a static dict of values. hence PluginType.FOO and PluginType("FOO") are really backed by same data. 
    """
    
    """
    Inner class that stores the actual value
    """
    class __PluginType(BaseEnumObject):

        def __init__(self, value):
            self.__value = value

        @property
        def value(self):
            return self.__value

        @property
        def name(self):
            return self.__value

        def __str__(self):
            return "PluginType." + self.__value

    """
    allowed enum values
    """
    STANDARD = __PluginType("Standard")
    IMPERSONATING = __PluginType("Impersonating")
    CUSTOMALGORITHM = __PluginType("CustomAlgorithm")

    """
    dictionary that keeps the enum value mapping for static access
    """
    __VALUES = dict()
    __VALUES["Standard"] = STANDARD
    __VALUES["Impersonating"] = IMPERSONATING
    __VALUES["CustomAlgorithm"] = CUSTOMALGORITHM

    def __init__(self, name):
        if name in PluginType.__VALUES:
            self.__instance = PluginType.__VALUES[name]
        else:
            new_value = PluginType.__PluginType(name)
            PluginType.__VALUES[name] = new_value
            self.__instance = new_value

    @property
    def value(self):
        return self.__instance.value

    @property
    def name(self):
        return self.__instance.name

    def __str__(self):
        return "PluginType." + self.__instance.name

    """ 
    This is to ensure equals work for both static defined values and client defined ones.
    """
    def __eq__(self, other):
        if (isinstance(self, PluginType) or isinstance(self, PluginType.__PluginType)) and \
                (isinstance(other, PluginType) or isinstance(other, PluginType.__PluginType)):
                return self.value == other.value

        return False

    def __ne__(self, other):
        if (isinstance(self, PluginType) or isinstance(self, PluginType.__PluginType)) and \
                (isinstance(other, PluginType) or isinstance(other, PluginType.__PluginType)):
                return self.value != other.value

        return True


