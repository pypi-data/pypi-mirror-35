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


class DataBarBorder(object):
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
        'color': 'Color',
        'type': 'str'
    }

    attribute_map = {
        'color': 'Color',
        'type': 'Type'
    }
    
    @staticmethod
    def get_swagger_types():
        return DataBarBorder.swagger_types
    
    @staticmethod
    def get_attribute_map():
        return DataBarBorder.attribute_map
    
    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self, color=None, type=None, **kw):
        """
        Associative dict for storing property values
        """
        self.container = {}
		    
        """
        DataBarBorder - a model defined in Swagger
        """

        self.container['color'] = None
        self.container['type'] = None

        if color is not None:
          self.color = color
        if type is not None:
          self.type = type

    @property
    def color(self):
        """
        Gets the color of this DataBarBorder.
        Gets or sets the border's color of data bars specified by a conditional formatting rule.

        :return: The color of this DataBarBorder.
        :rtype: Color
        """
        return self.container['color']

    @color.setter
    def color(self, color):
        """
        Sets the color of this DataBarBorder.
        Gets or sets the border's color of data bars specified by a conditional formatting rule.

        :param color: The color of this DataBarBorder.
        :type: Color
        """

        self.container['color'] = color

    @property
    def type(self):
        """
        Gets the type of this DataBarBorder.
        Gets or sets the border's type of data bars specified by a conditional formatting rule.

        :return: The type of this DataBarBorder.
        :rtype: str
        """
        return self.container['type']

    @type.setter
    def type(self, type):
        """
        Sets the type of this DataBarBorder.
        Gets or sets the border's type of data bars specified by a conditional formatting rule.

        :param type: The type of this DataBarBorder.
        :type: str
        """

        self.container['type'] = type

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
        if not isinstance(other, DataBarBorder):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
