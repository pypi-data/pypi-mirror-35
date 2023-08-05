# coding: utf-8

"""
    Flywheel

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.0.0-dev.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


## NOTE: This file is auto generated by the swagger code generator program.
## Do not edit the file manually.

import pprint
import re  # noqa: F401

import six

from flywheel.models.common_classification import CommonClassification  # noqa: F401,E501
from flywheel.models.common_info import CommonInfo  # noqa: F401,E501
from flywheel.models.file_origin import FileOrigin  # noqa: F401,E501

# NOTE: This file is auto generated by the swagger code generator program.
# Do not edit the class manually.

class FileEntry(object):

    swagger_types = {
        'id': 'str',
        'name': 'str',
        'type': 'str',
        'mimetype': 'str',
        'modality': 'str',
        'classification': 'CommonClassification',
        'tags': 'list[str]',
        'info': 'CommonInfo',
        'origin': 'FileOrigin',
        'hash': 'str',
        'created': 'datetime',
        'modified': 'datetime',
        'size': 'int',
        'info_exists': 'bool'
    }

    attribute_map = {
        'id': '_id',
        'name': 'name',
        'type': 'type',
        'mimetype': 'mimetype',
        'modality': 'modality',
        'classification': 'classification',
        'tags': 'tags',
        'info': 'info',
        'origin': 'origin',
        'hash': 'hash',
        'created': 'created',
        'modified': 'modified',
        'size': 'size',
        'info_exists': 'info_exists'
    }

    rattribute_map = {
        '_id': 'id',
        'name': 'name',
        'type': 'type',
        'mimetype': 'mimetype',
        'modality': 'modality',
        'classification': 'classification',
        'tags': 'tags',
        'info': 'info',
        'origin': 'origin',
        'hash': 'hash',
        'created': 'created',
        'modified': 'modified',
        'size': 'size',
        'info_exists': 'info_exists'
    }

    def __init__(self, id=None, name=None, type=None, mimetype=None, modality=None, classification=None, tags=None, info=None, origin=None, hash=None, created=None, modified=None, size=None, info_exists=None):  # noqa: E501
        """FileEntry - a model defined in Swagger"""

        self._id = None
        self._name = None
        self._type = None
        self._mimetype = None
        self._modality = None
        self._classification = None
        self._tags = None
        self._info = None
        self._origin = None
        self._hash = None
        self._created = None
        self._modified = None
        self._size = None
        self._info_exists = None
        self.discriminator = None
        self.alt_discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if mimetype is not None:
            self.mimetype = mimetype
        if modality is not None:
            self.modality = modality
        if classification is not None:
            self.classification = classification
        if tags is not None:
            self.tags = tags
        if info is not None:
            self.info = info
        if origin is not None:
            self.origin = origin
        if hash is not None:
            self.hash = hash
        if created is not None:
            self.created = created
        if modified is not None:
            self.modified = modified
        if size is not None:
            self.size = size
        if info_exists is not None:
            self.info_exists = info_exists

    @property
    def id(self):
        """Gets the id of this FileEntry.


        :return: The id of this FileEntry.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FileEntry.


        :param id: The id of this FileEntry.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this FileEntry.

        The name of the file on disk

        :return: The name of this FileEntry.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FileEntry.

        The name of the file on disk

        :param name: The name of this FileEntry.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this FileEntry.

        A descriptive file type (e.g. dicom, image, document, ...)

        :return: The type of this FileEntry.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this FileEntry.

        A descriptive file type (e.g. dicom, image, document, ...)

        :param type: The type of this FileEntry.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def mimetype(self):
        """Gets the mimetype of this FileEntry.

        A MIME Content-Type of the file

        :return: The mimetype of this FileEntry.
        :rtype: str
        """
        return self._mimetype

    @mimetype.setter
    def mimetype(self, mimetype):
        """Sets the mimetype of this FileEntry.

        A MIME Content-Type of the file

        :param mimetype: The mimetype of this FileEntry.  # noqa: E501
        :type: str
        """

        self._mimetype = mimetype

    @property
    def modality(self):
        """Gets the modality of this FileEntry.

        The type of instrument that originated the file (e.g. MR, CT, ...)

        :return: The modality of this FileEntry.
        :rtype: str
        """
        return self._modality

    @modality.setter
    def modality(self, modality):
        """Sets the modality of this FileEntry.

        The type of instrument that originated the file (e.g. MR, CT, ...)

        :param modality: The modality of this FileEntry.  # noqa: E501
        :type: str
        """

        self._modality = modality

    @property
    def classification(self):
        """Gets the classification of this FileEntry.


        :return: The classification of this FileEntry.
        :rtype: CommonClassification
        """
        return self._classification

    @classification.setter
    def classification(self, classification):
        """Sets the classification of this FileEntry.


        :param classification: The classification of this FileEntry.  # noqa: E501
        :type: CommonClassification
        """

        self._classification = classification

    @property
    def tags(self):
        """Gets the tags of this FileEntry.

        Array of application-specific tags

        :return: The tags of this FileEntry.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this FileEntry.

        Array of application-specific tags

        :param tags: The tags of this FileEntry.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def info(self):
        """Gets the info of this FileEntry.


        :return: The info of this FileEntry.
        :rtype: CommonInfo
        """
        return self._info

    @info.setter
    def info(self, info):
        """Sets the info of this FileEntry.


        :param info: The info of this FileEntry.  # noqa: E501
        :type: CommonInfo
        """

        self._info = info

    @property
    def origin(self):
        """Gets the origin of this FileEntry.


        :return: The origin of this FileEntry.
        :rtype: FileOrigin
        """
        return self._origin

    @origin.setter
    def origin(self, origin):
        """Sets the origin of this FileEntry.


        :param origin: The origin of this FileEntry.  # noqa: E501
        :type: FileOrigin
        """

        self._origin = origin

    @property
    def hash(self):
        """Gets the hash of this FileEntry.

        Cryptographic hash of the file

        :return: The hash of this FileEntry.
        :rtype: str
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        """Sets the hash of this FileEntry.

        Cryptographic hash of the file

        :param hash: The hash of this FileEntry.  # noqa: E501
        :type: str
        """

        self._hash = hash

    @property
    def created(self):
        """Gets the created of this FileEntry.

        Creation time (automatically set)

        :return: The created of this FileEntry.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this FileEntry.

        Creation time (automatically set)

        :param created: The created of this FileEntry.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def modified(self):
        """Gets the modified of this FileEntry.

        Last modification time (automatically updated)

        :return: The modified of this FileEntry.
        :rtype: datetime
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """Sets the modified of this FileEntry.

        Last modification time (automatically updated)

        :param modified: The modified of this FileEntry.  # noqa: E501
        :type: datetime
        """

        self._modified = modified

    @property
    def size(self):
        """Gets the size of this FileEntry.

        Size of the file, in bytes

        :return: The size of this FileEntry.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this FileEntry.

        Size of the file, in bytes

        :param size: The size of this FileEntry.  # noqa: E501
        :type: int
        """

        self._size = size

    @property
    def info_exists(self):
        """Gets the info_exists of this FileEntry.


        :return: The info_exists of this FileEntry.
        :rtype: bool
        """
        return self._info_exists

    @info_exists.setter
    def info_exists(self, info_exists):
        """Sets the info_exists of this FileEntry.


        :param info_exists: The info_exists of this FileEntry.  # noqa: E501
        :type: bool
        """

        self._info_exists = info_exists


    @staticmethod
    def positional_to_model(value):
        """Converts a positional argument to a model value"""
        return value

    def return_value(self):
        """Unwraps return value from model"""
        return self

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, FileEntry):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

    # Container emulation
    def __getitem__(self, key):
        """Returns the value of key"""
        key = self._map_key(key)
        return getattr(self, key)

    def __setitem__(self, key, value):
        """Sets the value of key"""
        key = self._map_key(key)
        setattr(self, key, value)

    def __contains__(self, key):
        """Checks if the given value is a key in this object"""
        key = self._map_key(key, raise_on_error=False)
        return key is not None

    def keys(self):
        """Returns the list of json properties in the object"""
        return self.__class__.rattribute_map.keys()

    def values(self):
        """Returns the list of values in the object"""
        for key in self.__class__.attribute_map.keys():
            yield getattr(self, key)

    def items(self):
        """Returns the list of json property to value mapping"""
        for key, prop in self.__class__.rattribute_map.items():
            yield key, getattr(self, prop)

    def get(self, key, default=None):
        """Get the value of the provided json property, or default"""
        key = self._map_key(key, raise_on_error=False)
        if key:
            return getattr(self, key, default)
        return default

    def _map_key(self, key, raise_on_error=True):
        result = self.__class__.rattribute_map.get(key)
        if result is None:
            if raise_on_error:
                raise AttributeError('Invalid attribute name: {}'.format(key))
            return None
        return '_' + result
