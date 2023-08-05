# coding: utf-8

"""
    Web API Swagger specification

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class AutoFilter(object):
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
        'link': 'Link',
        'range': 'str',
        'filter_columns': 'list[FilterColumn]',
        'sorter': 'DataSorter'
    }

    attribute_map = {
        'link': 'link',
        'range': 'Range',
        'filter_columns': 'FilterColumns',
        'sorter': 'Sorter'
    }
    
    @staticmethod
    def get_swagger_types():
        return AutoFilter.swagger_types
    
    @staticmethod
    def get_attribute_map():
        return AutoFilter.attribute_map
    
    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self, link=None, range=None, filter_columns=None, sorter=None, **kw):
        """
        Associative dict for storing property values
        """
        self.container = {}
		    
        """
        AutoFilter - a model defined in Swagger
        """

        self.container['link'] = None
        self.container['range'] = None
        self.container['filter_columns'] = None
        self.container['sorter'] = None

        if link is not None:
          self.link = link
        if range is not None:
          self.range = range
        if filter_columns is not None:
          self.filter_columns = filter_columns
        if sorter is not None:
          self.sorter = sorter

    @property
    def link(self):
        """
        Gets the link of this AutoFilter.

        :return: The link of this AutoFilter.
        :rtype: Link
        """
        return self.container['link']

    @link.setter
    def link(self, link):
        """
        Sets the link of this AutoFilter.

        :param link: The link of this AutoFilter.
        :type: Link
        """

        self.container['link'] = link

    @property
    def range(self):
        """
        Gets the range of this AutoFilter.

        :return: The range of this AutoFilter.
        :rtype: str
        """
        return self.container['range']

    @range.setter
    def range(self, range):
        """
        Sets the range of this AutoFilter.

        :param range: The range of this AutoFilter.
        :type: str
        """

        self.container['range'] = range

    @property
    def filter_columns(self):
        """
        Gets the filter_columns of this AutoFilter.

        :return: The filter_columns of this AutoFilter.
        :rtype: list[FilterColumn]
        """
        return self.container['filter_columns']

    @filter_columns.setter
    def filter_columns(self, filter_columns):
        """
        Sets the filter_columns of this AutoFilter.

        :param filter_columns: The filter_columns of this AutoFilter.
        :type: list[FilterColumn]
        """

        self.container['filter_columns'] = filter_columns

    @property
    def sorter(self):
        """
        Gets the sorter of this AutoFilter.

        :return: The sorter of this AutoFilter.
        :rtype: DataSorter
        """
        return self.container['sorter']

    @sorter.setter
    def sorter(self, sorter):
        """
        Sets the sorter of this AutoFilter.

        :param sorter: The sorter of this AutoFilter.
        :type: DataSorter
        """

        self.container['sorter'] = sorter

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.get_swagger_types()):
            value = self.get_from_container(attr)
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
        if not isinstance(other, AutoFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
