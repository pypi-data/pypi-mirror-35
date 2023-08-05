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
from . import SaaSposeResponse

class HyperlinksResponse(SaaSposeResponse):
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
        'hyperlinks': 'Hyperlinks'
    }

    attribute_map = {
        'hyperlinks': 'Hyperlinks'
    }
    
    @staticmethod
    def get_swagger_types():
        return dict(HyperlinksResponse.swagger_types, **SaaSposeResponse.get_swagger_types())
    
    @staticmethod
    def get_attribute_map():
        return dict(HyperlinksResponse.attribute_map, **SaaSposeResponse.get_attribute_map())
    
    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self, hyperlinks=None, **kw):
        super(HyperlinksResponse, self).__init__(**kw)
		    
        """
        HyperlinksResponse - a model defined in Swagger
        """

        self.container['hyperlinks'] = None

        if hyperlinks is not None:
          self.hyperlinks = hyperlinks

    @property
    def hyperlinks(self):
        """
        Gets the hyperlinks of this HyperlinksResponse.

        :return: The hyperlinks of this HyperlinksResponse.
        :rtype: Hyperlinks
        """
        return self.container['hyperlinks']

    @hyperlinks.setter
    def hyperlinks(self, hyperlinks):
        """
        Sets the hyperlinks of this HyperlinksResponse.

        :param hyperlinks: The hyperlinks of this HyperlinksResponse.
        :type: Hyperlinks
        """

        self.container['hyperlinks'] = hyperlinks

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
        if not isinstance(other, HyperlinksResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
