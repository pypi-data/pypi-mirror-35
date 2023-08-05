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
from . import OperateParameter

class ChartOperateParameter(OperateParameter):
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
        'string': 'str',
        'area': 'str',
        'category_data': 'str',
        'upper_left_row': 'int',
        'lower_right_column': 'int',
        'lower_right_row': 'int',
        'is_auto_get_serial_name': 'bool',
        'chart_type': 'str',
        'is_vertical': 'bool'
    }

    attribute_map = {
        'string': 'string',
        'area': 'Area',
        'category_data': 'CategoryData',
        'upper_left_row': 'UpperLeftRow',
        'lower_right_column': 'LowerRightColumn',
        'lower_right_row': 'LowerRightRow',
        'is_auto_get_serial_name': 'IsAutoGetSerialName',
        'chart_type': 'ChartType',
        'is_vertical': 'IsVertical'
    }
    
    @staticmethod
    def get_swagger_types():
        return dict(ChartOperateParameter.swagger_types, **OperateParameter.get_swagger_types())
    
    @staticmethod
    def get_attribute_map():
        return dict(ChartOperateParameter.attribute_map, **OperateParameter.get_attribute_map())
    
    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self, string=None, area=None, category_data=None, upper_left_row=None, lower_right_column=None, lower_right_row=None, is_auto_get_serial_name=None, chart_type=None, is_vertical=None, **kw):
        super(ChartOperateParameter, self).__init__(**kw)
		    
        """
        ChartOperateParameter - a model defined in Swagger
        """

        self.container['string'] = None
        self.container['area'] = None
        self.container['category_data'] = None
        self.container['upper_left_row'] = None
        self.container['lower_right_column'] = None
        self.container['lower_right_row'] = None
        self.container['is_auto_get_serial_name'] = None
        self.container['chart_type'] = None
        self.container['is_vertical'] = None

        if string is not None:
          self.string = string
        if area is not None:
          self.area = area
        if category_data is not None:
          self.category_data = category_data
        if upper_left_row is not None:
          self.upper_left_row = upper_left_row
        if lower_right_column is not None:
          self.lower_right_column = lower_right_column
        if lower_right_row is not None:
          self.lower_right_row = lower_right_row
        if is_auto_get_serial_name is not None:
          self.is_auto_get_serial_name = is_auto_get_serial_name
        if chart_type is not None:
          self.chart_type = chart_type
        if is_vertical is not None:
          self.is_vertical = is_vertical

    @property
    def string(self):
        """
        Gets the string of this ChartOperateParameter.

        :return: The string of this ChartOperateParameter.
        :rtype: str
        """
        return self.container['string']

    @string.setter
    def string(self, string):
        """
        Sets the string of this ChartOperateParameter.

        :param string: The string of this ChartOperateParameter.
        :type: str
        """

        self.container['string'] = string

    @property
    def area(self):
        """
        Gets the area of this ChartOperateParameter.

        :return: The area of this ChartOperateParameter.
        :rtype: str
        """
        return self.container['area']

    @area.setter
    def area(self, area):
        """
        Sets the area of this ChartOperateParameter.

        :param area: The area of this ChartOperateParameter.
        :type: str
        """

        self.container['area'] = area

    @property
    def category_data(self):
        """
        Gets the category_data of this ChartOperateParameter.

        :return: The category_data of this ChartOperateParameter.
        :rtype: str
        """
        return self.container['category_data']

    @category_data.setter
    def category_data(self, category_data):
        """
        Sets the category_data of this ChartOperateParameter.

        :param category_data: The category_data of this ChartOperateParameter.
        :type: str
        """

        self.container['category_data'] = category_data

    @property
    def upper_left_row(self):
        """
        Gets the upper_left_row of this ChartOperateParameter.

        :return: The upper_left_row of this ChartOperateParameter.
        :rtype: int
        """
        return self.container['upper_left_row']

    @upper_left_row.setter
    def upper_left_row(self, upper_left_row):
        """
        Sets the upper_left_row of this ChartOperateParameter.

        :param upper_left_row: The upper_left_row of this ChartOperateParameter.
        :type: int
        """

        self.container['upper_left_row'] = upper_left_row

    @property
    def lower_right_column(self):
        """
        Gets the lower_right_column of this ChartOperateParameter.

        :return: The lower_right_column of this ChartOperateParameter.
        :rtype: int
        """
        return self.container['lower_right_column']

    @lower_right_column.setter
    def lower_right_column(self, lower_right_column):
        """
        Sets the lower_right_column of this ChartOperateParameter.

        :param lower_right_column: The lower_right_column of this ChartOperateParameter.
        :type: int
        """

        self.container['lower_right_column'] = lower_right_column

    @property
    def lower_right_row(self):
        """
        Gets the lower_right_row of this ChartOperateParameter.

        :return: The lower_right_row of this ChartOperateParameter.
        :rtype: int
        """
        return self.container['lower_right_row']

    @lower_right_row.setter
    def lower_right_row(self, lower_right_row):
        """
        Sets the lower_right_row of this ChartOperateParameter.

        :param lower_right_row: The lower_right_row of this ChartOperateParameter.
        :type: int
        """

        self.container['lower_right_row'] = lower_right_row

    @property
    def is_auto_get_serial_name(self):
        """
        Gets the is_auto_get_serial_name of this ChartOperateParameter.

        :return: The is_auto_get_serial_name of this ChartOperateParameter.
        :rtype: bool
        """
        return self.container['is_auto_get_serial_name']

    @is_auto_get_serial_name.setter
    def is_auto_get_serial_name(self, is_auto_get_serial_name):
        """
        Sets the is_auto_get_serial_name of this ChartOperateParameter.

        :param is_auto_get_serial_name: The is_auto_get_serial_name of this ChartOperateParameter.
        :type: bool
        """

        self.container['is_auto_get_serial_name'] = is_auto_get_serial_name

    @property
    def chart_type(self):
        """
        Gets the chart_type of this ChartOperateParameter.

        :return: The chart_type of this ChartOperateParameter.
        :rtype: str
        """
        return self.container['chart_type']

    @chart_type.setter
    def chart_type(self, chart_type):
        """
        Sets the chart_type of this ChartOperateParameter.

        :param chart_type: The chart_type of this ChartOperateParameter.
        :type: str
        """

        self.container['chart_type'] = chart_type

    @property
    def is_vertical(self):
        """
        Gets the is_vertical of this ChartOperateParameter.

        :return: The is_vertical of this ChartOperateParameter.
        :rtype: bool
        """
        return self.container['is_vertical']

    @is_vertical.setter
    def is_vertical(self, is_vertical):
        """
        Sets the is_vertical of this ChartOperateParameter.

        :param is_vertical: The is_vertical of this ChartOperateParameter.
        :type: bool
        """

        self.container['is_vertical'] = is_vertical

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
        if not isinstance(other, ChartOperateParameter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
