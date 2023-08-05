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


class PivotFilter(object):
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
        'evaluation_order': 'int',
        'name': 'str',
        'filter_type': 'str',
        'auto_filter': 'AutoFilter',
        'field_index': 'int',
        'measure_fld_index': 'int',
        'value1': 'str',
        'member_property_field_index': 'int',
        'value2': 'str'
    }

    attribute_map = {
        'evaluation_order': 'EvaluationOrder',
        'name': 'Name',
        'filter_type': 'FilterType',
        'auto_filter': 'AutoFilter',
        'field_index': 'FieldIndex',
        'measure_fld_index': 'MeasureFldIndex',
        'value1': 'Value1',
        'member_property_field_index': 'MemberPropertyFieldIndex',
        'value2': 'Value2'
    }
    
    @staticmethod
    def get_swagger_types():
        return PivotFilter.swagger_types
    
    @staticmethod
    def get_attribute_map():
        return PivotFilter.attribute_map
    
    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self, evaluation_order=None, name=None, filter_type=None, auto_filter=None, field_index=None, measure_fld_index=None, value1=None, member_property_field_index=None, value2=None, **kw):
        """
        Associative dict for storing property values
        """
        self.container = {}
		    
        """
        PivotFilter - a model defined in Swagger
        """

        self.container['evaluation_order'] = None
        self.container['name'] = None
        self.container['filter_type'] = None
        self.container['auto_filter'] = None
        self.container['field_index'] = None
        self.container['measure_fld_index'] = None
        self.container['value1'] = None
        self.container['member_property_field_index'] = None
        self.container['value2'] = None

        if evaluation_order is not None:
          self.evaluation_order = evaluation_order
        if name is not None:
          self.name = name
        if filter_type is not None:
          self.filter_type = filter_type
        if auto_filter is not None:
          self.auto_filter = auto_filter
        if field_index is not None:
          self.field_index = field_index
        if measure_fld_index is not None:
          self.measure_fld_index = measure_fld_index
        if value1 is not None:
          self.value1 = value1
        if member_property_field_index is not None:
          self.member_property_field_index = member_property_field_index
        if value2 is not None:
          self.value2 = value2

    @property
    def evaluation_order(self):
        """
        Gets the evaluation_order of this PivotFilter.
        Gets the Evaluation Order of the pivot filter.

        :return: The evaluation_order of this PivotFilter.
        :rtype: int
        """
        return self.container['evaluation_order']

    @evaluation_order.setter
    def evaluation_order(self, evaluation_order):
        """
        Sets the evaluation_order of this PivotFilter.
        Gets the Evaluation Order of the pivot filter.

        :param evaluation_order: The evaluation_order of this PivotFilter.
        :type: int
        """

        self.container['evaluation_order'] = evaluation_order

    @property
    def name(self):
        """
        Gets the name of this PivotFilter.
        Gets the name of the pivot filter.

        :return: The name of this PivotFilter.
        :rtype: str
        """
        return self.container['name']

    @name.setter
    def name(self, name):
        """
        Sets the name of this PivotFilter.
        Gets the name of the pivot filter.

        :param name: The name of this PivotFilter.
        :type: str
        """

        self.container['name'] = name

    @property
    def filter_type(self):
        """
        Gets the filter_type of this PivotFilter.
        Gets the autofilter type of the pivot filter.

        :return: The filter_type of this PivotFilter.
        :rtype: str
        """
        return self.container['filter_type']

    @filter_type.setter
    def filter_type(self, filter_type):
        """
        Sets the filter_type of this PivotFilter.
        Gets the autofilter type of the pivot filter.

        :param filter_type: The filter_type of this PivotFilter.
        :type: str
        """

        self.container['filter_type'] = filter_type

    @property
    def auto_filter(self):
        """
        Gets the auto_filter of this PivotFilter.
        Gets the autofilter of the pivot filter.

        :return: The auto_filter of this PivotFilter.
        :rtype: AutoFilter
        """
        return self.container['auto_filter']

    @auto_filter.setter
    def auto_filter(self, auto_filter):
        """
        Sets the auto_filter of this PivotFilter.
        Gets the autofilter of the pivot filter.

        :param auto_filter: The auto_filter of this PivotFilter.
        :type: AutoFilter
        """

        self.container['auto_filter'] = auto_filter

    @property
    def field_index(self):
        """
        Gets the field_index of this PivotFilter.
        Gets the field index of the pivot filter.

        :return: The field_index of this PivotFilter.
        :rtype: int
        """
        return self.container['field_index']

    @field_index.setter
    def field_index(self, field_index):
        """
        Sets the field_index of this PivotFilter.
        Gets the field index of the pivot filter.

        :param field_index: The field_index of this PivotFilter.
        :type: int
        """

        self.container['field_index'] = field_index

    @property
    def measure_fld_index(self):
        """
        Gets the measure_fld_index of this PivotFilter.
        Gets the measure field index of the pivot filter.             

        :return: The measure_fld_index of this PivotFilter.
        :rtype: int
        """
        return self.container['measure_fld_index']

    @measure_fld_index.setter
    def measure_fld_index(self, measure_fld_index):
        """
        Sets the measure_fld_index of this PivotFilter.
        Gets the measure field index of the pivot filter.             

        :param measure_fld_index: The measure_fld_index of this PivotFilter.
        :type: int
        """

        self.container['measure_fld_index'] = measure_fld_index

    @property
    def value1(self):
        """
        Gets the value1 of this PivotFilter.
        Gets the string value1 of the label pivot filter.             

        :return: The value1 of this PivotFilter.
        :rtype: str
        """
        return self.container['value1']

    @value1.setter
    def value1(self, value1):
        """
        Sets the value1 of this PivotFilter.
        Gets the string value1 of the label pivot filter.             

        :param value1: The value1 of this PivotFilter.
        :type: str
        """

        self.container['value1'] = value1

    @property
    def member_property_field_index(self):
        """
        Gets the member_property_field_index of this PivotFilter.
        Gets the member property field index of the pivot filter.             

        :return: The member_property_field_index of this PivotFilter.
        :rtype: int
        """
        return self.container['member_property_field_index']

    @member_property_field_index.setter
    def member_property_field_index(self, member_property_field_index):
        """
        Sets the member_property_field_index of this PivotFilter.
        Gets the member property field index of the pivot filter.             

        :param member_property_field_index: The member_property_field_index of this PivotFilter.
        :type: int
        """

        self.container['member_property_field_index'] = member_property_field_index

    @property
    def value2(self):
        """
        Gets the value2 of this PivotFilter.
        Gets the string value2 of the label pivot filter.             

        :return: The value2 of this PivotFilter.
        :rtype: str
        """
        return self.container['value2']

    @value2.setter
    def value2(self, value2):
        """
        Sets the value2 of this PivotFilter.
        Gets the string value2 of the label pivot filter.             

        :param value2: The value2 of this PivotFilter.
        :type: str
        """

        self.container['value2'] = value2

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
        if not isinstance(other, PivotFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
