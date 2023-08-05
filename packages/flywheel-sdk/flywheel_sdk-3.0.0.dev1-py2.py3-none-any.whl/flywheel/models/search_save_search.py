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

from flywheel.models.permission import Permission  # noqa: F401,E501
from flywheel.models.search_query import SearchQuery  # noqa: F401,E501

# NOTE: This file is auto generated by the swagger code generator program.
# Do not edit the class manually.

class SearchSaveSearch(object):

    swagger_types = {
        'label': 'str',
        'search': 'SearchQuery',
        'id': 'str',
        'uid': 'str',
        'created': 'datetime',
        'modified': 'datetime',
        'permissions': 'list[Permission]'
    }

    attribute_map = {
        'label': 'label',
        'search': 'search',
        'id': '_id',
        'uid': 'uid',
        'created': 'created',
        'modified': 'modified',
        'permissions': 'permissions'
    }

    rattribute_map = {
        'label': 'label',
        'search': 'search',
        '_id': 'id',
        'uid': 'uid',
        'created': 'created',
        'modified': 'modified',
        'permissions': 'permissions'
    }

    def __init__(self, label=None, search=None, id=None, uid=None, created=None, modified=None, permissions=None):  # noqa: E501
        """SearchSaveSearch - a model defined in Swagger"""

        self._label = None
        self._search = None
        self._id = None
        self._uid = None
        self._created = None
        self._modified = None
        self._permissions = None
        self.discriminator = None
        self.alt_discriminator = None

        if label is not None:
            self.label = label
        if search is not None:
            self.search = search
        if id is not None:
            self.id = id
        if uid is not None:
            self.uid = uid
        if created is not None:
            self.created = created
        if modified is not None:
            self.modified = modified
        if permissions is not None:
            self.permissions = permissions

    @property
    def label(self):
        """Gets the label of this SearchSaveSearch.

        Application-specific label

        :return: The label of this SearchSaveSearch.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this SearchSaveSearch.

        Application-specific label

        :param label: The label of this SearchSaveSearch.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def search(self):
        """Gets the search of this SearchSaveSearch.


        :return: The search of this SearchSaveSearch.
        :rtype: SearchQuery
        """
        return self._search

    @search.setter
    def search(self, search):
        """Sets the search of this SearchSaveSearch.


        :param search: The search of this SearchSaveSearch.  # noqa: E501
        :type: SearchQuery
        """

        self._search = search

    @property
    def id(self):
        """Gets the id of this SearchSaveSearch.

        Unique database ID

        :return: The id of this SearchSaveSearch.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SearchSaveSearch.

        Unique database ID

        :param id: The id of this SearchSaveSearch.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def uid(self):
        """Gets the uid of this SearchSaveSearch.

        A user database ID

        :return: The uid of this SearchSaveSearch.
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this SearchSaveSearch.

        A user database ID

        :param uid: The uid of this SearchSaveSearch.  # noqa: E501
        :type: str
        """

        self._uid = uid

    @property
    def created(self):
        """Gets the created of this SearchSaveSearch.

        Creation time (automatically set)

        :return: The created of this SearchSaveSearch.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this SearchSaveSearch.

        Creation time (automatically set)

        :param created: The created of this SearchSaveSearch.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def modified(self):
        """Gets the modified of this SearchSaveSearch.

        Last modification time (automatically updated)

        :return: The modified of this SearchSaveSearch.
        :rtype: datetime
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """Sets the modified of this SearchSaveSearch.

        Last modification time (automatically updated)

        :param modified: The modified of this SearchSaveSearch.  # noqa: E501
        :type: datetime
        """

        self._modified = modified

    @property
    def permissions(self):
        """Gets the permissions of this SearchSaveSearch.


        :return: The permissions of this SearchSaveSearch.
        :rtype: list[Permission]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this SearchSaveSearch.


        :param permissions: The permissions of this SearchSaveSearch.  # noqa: E501
        :type: list[Permission]
        """

        self._permissions = permissions


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
        if not isinstance(other, SearchSaveSearch):
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
