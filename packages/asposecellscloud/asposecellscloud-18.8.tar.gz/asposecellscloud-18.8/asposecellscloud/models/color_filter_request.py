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


class ColorFilterRequest(object):
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
        'pattern': 'str',
        'foreground_color': 'CellsColor',
        'background_color': 'CellsColor'
    }

    attribute_map = {
        'pattern': 'Pattern',
        'foreground_color': 'ForegroundColor',
        'background_color': 'BackgroundColor'
    }
    
    @staticmethod
    def get_swagger_types():
        return ColorFilterRequest.swagger_types
    
    @staticmethod
    def get_attribute_map():
        return ColorFilterRequest.attribute_map
    
    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self, pattern=None, foreground_color=None, background_color=None, **kw):
        """
        Associative dict for storing property values
        """
        self.container = {}
		    
        """
        ColorFilterRequest - a model defined in Swagger
        """

        self.container['pattern'] = None
        self.container['foreground_color'] = None
        self.container['background_color'] = None

        if pattern is not None:
          self.pattern = pattern
        if foreground_color is not None:
          self.foreground_color = foreground_color
        if background_color is not None:
          self.background_color = background_color

    @property
    def pattern(self):
        """
        Gets the pattern of this ColorFilterRequest.

        :return: The pattern of this ColorFilterRequest.
        :rtype: str
        """
        return self.container['pattern']

    @pattern.setter
    def pattern(self, pattern):
        """
        Sets the pattern of this ColorFilterRequest.

        :param pattern: The pattern of this ColorFilterRequest.
        :type: str
        """

        self.container['pattern'] = pattern

    @property
    def foreground_color(self):
        """
        Gets the foreground_color of this ColorFilterRequest.

        :return: The foreground_color of this ColorFilterRequest.
        :rtype: CellsColor
        """
        return self.container['foreground_color']

    @foreground_color.setter
    def foreground_color(self, foreground_color):
        """
        Sets the foreground_color of this ColorFilterRequest.

        :param foreground_color: The foreground_color of this ColorFilterRequest.
        :type: CellsColor
        """

        self.container['foreground_color'] = foreground_color

    @property
    def background_color(self):
        """
        Gets the background_color of this ColorFilterRequest.

        :return: The background_color of this ColorFilterRequest.
        :rtype: CellsColor
        """
        return self.container['background_color']

    @background_color.setter
    def background_color(self, background_color):
        """
        Sets the background_color of this ColorFilterRequest.

        :param background_color: The background_color of this ColorFilterRequest.
        :type: CellsColor
        """

        self.container['background_color'] = background_color

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
        if not isinstance(other, ColorFilterRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
