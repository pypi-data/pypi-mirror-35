# coding: utf-8

"""
    Web API Swagger specification

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class CellsPropertiesApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def cells_properties_delete_document_properties(self, name, **kwargs):
        """
        Delete all custom document properties and clean built-in ones.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.cells_properties_delete_document_properties(name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str name: The document name. (required)
        :param str folder: The document folder.
        :return: CellsDocumentPropertiesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.cells_properties_delete_document_properties_with_http_info(name, **kwargs)
        else:
            (data) = self.cells_properties_delete_document_properties_with_http_info(name, **kwargs)
            return data

    def cells_properties_delete_document_properties_with_http_info(self, name, **kwargs):
        """
        Delete all custom document properties and clean built-in ones.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.cells_properties_delete_document_properties_with_http_info(name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str name: The document name. (required)
        :param str folder: The document folder.
        :return: CellsDocumentPropertiesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name', 'folder']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method cells_properties_delete_document_properties" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params) or (params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `cells_properties_delete_document_properties`")


        collection_formats = {}

        path_params = {}
        if 'name' in params:
            path_params['name'] = params['name']

        query_params = []
        if 'folder' in params:
            query_params.append(('folder', params['folder']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/cells/{name}/documentproperties', 'DELETE',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='CellsDocumentPropertiesResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def cells_properties_delete_document_property(self, name, property_name, **kwargs):
        """
        Delete document property.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.cells_properties_delete_document_property(name, property_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str name: The document name. (required)
        :param str property_name: The property name. (required)
        :param str folder: The document folder.
        :return: CellsDocumentPropertiesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.cells_properties_delete_document_property_with_http_info(name, property_name, **kwargs)
        else:
            (data) = self.cells_properties_delete_document_property_with_http_info(name, property_name, **kwargs)
            return data

    def cells_properties_delete_document_property_with_http_info(self, name, property_name, **kwargs):
        """
        Delete document property.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.cells_properties_delete_document_property_with_http_info(name, property_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str name: The document name. (required)
        :param str property_name: The property name. (required)
        :param str folder: The document folder.
        :return: CellsDocumentPropertiesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name', 'property_name', 'folder']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method cells_properties_delete_document_property" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params) or (params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `cells_properties_delete_document_property`")
        # verify the required parameter 'property_name' is set
        if ('property_name' not in params) or (params['property_name'] is None):
            raise ValueError("Missing the required parameter `property_name` when calling `cells_properties_delete_document_property`")


        collection_formats = {}

        path_params = {}
        if 'name' in params:
            path_params['name'] = params['name']
        if 'property_name' in params:
            path_params['propertyName'] = params['property_name']

        query_params = []
        if 'folder' in params:
            query_params.append(('folder', params['folder']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/cells/{name}/documentproperties/{propertyName}', 'DELETE',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='CellsDocumentPropertiesResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def cells_properties_get_document_properties(self, name, **kwargs):
        """
        Read document properties.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.cells_properties_get_document_properties(name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str name: The document name. (required)
        :param str folder: The document folder.
        :return: CellsDocumentPropertiesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.cells_properties_get_document_properties_with_http_info(name, **kwargs)
        else:
            (data) = self.cells_properties_get_document_properties_with_http_info(name, **kwargs)
            return data

    def cells_properties_get_document_properties_with_http_info(self, name, **kwargs):
        """
        Read document properties.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.cells_properties_get_document_properties_with_http_info(name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str name: The document name. (required)
        :param str folder: The document folder.
        :return: CellsDocumentPropertiesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name', 'folder']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method cells_properties_get_document_properties" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params) or (params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `cells_properties_get_document_properties`")


        collection_formats = {}

        path_params = {}
        if 'name' in params:
            path_params['name'] = params['name']

        query_params = []
        if 'folder' in params:
            query_params.append(('folder', params['folder']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/cells/{name}/documentproperties', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='CellsDocumentPropertiesResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def cells_properties_get_document_property(self, name, property_name, **kwargs):
        """
        Read document property by name.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.cells_properties_get_document_property(name, property_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str name: The document name. (required)
        :param str property_name: The property name. (required)
        :param str folder: The document folder.
        :return: CellsDocumentPropertyResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.cells_properties_get_document_property_with_http_info(name, property_name, **kwargs)
        else:
            (data) = self.cells_properties_get_document_property_with_http_info(name, property_name, **kwargs)
            return data

    def cells_properties_get_document_property_with_http_info(self, name, property_name, **kwargs):
        """
        Read document property by name.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.cells_properties_get_document_property_with_http_info(name, property_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str name: The document name. (required)
        :param str property_name: The property name. (required)
        :param str folder: The document folder.
        :return: CellsDocumentPropertyResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name', 'property_name', 'folder']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method cells_properties_get_document_property" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params) or (params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `cells_properties_get_document_property`")
        # verify the required parameter 'property_name' is set
        if ('property_name' not in params) or (params['property_name'] is None):
            raise ValueError("Missing the required parameter `property_name` when calling `cells_properties_get_document_property`")


        collection_formats = {}

        path_params = {}
        if 'name' in params:
            path_params['name'] = params['name']
        if 'property_name' in params:
            path_params['propertyName'] = params['property_name']

        query_params = []
        if 'folder' in params:
            query_params.append(('folder', params['folder']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/cells/{name}/documentproperties/{propertyName}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='CellsDocumentPropertyResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def cells_properties_put_document_property(self, name, property_name, **kwargs):
        """
        Set/create document property.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.cells_properties_put_document_property(name, property_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str name: The document name. (required)
        :param str property_name: The property name. (required)
        :param CellsDocumentProperty _property: with new property value.
        :param str folder: The document folder.
        :return: CellsDocumentPropertyResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.cells_properties_put_document_property_with_http_info(name, property_name, **kwargs)
        else:
            (data) = self.cells_properties_put_document_property_with_http_info(name, property_name, **kwargs)
            return data

    def cells_properties_put_document_property_with_http_info(self, name, property_name, **kwargs):
        """
        Set/create document property.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.cells_properties_put_document_property_with_http_info(name, property_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str name: The document name. (required)
        :param str property_name: The property name. (required)
        :param CellsDocumentProperty _property: with new property value.
        :param str folder: The document folder.
        :return: CellsDocumentPropertyResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name', 'property_name', '_property', 'folder']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method cells_properties_put_document_property" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params) or (params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `cells_properties_put_document_property`")
        # verify the required parameter 'property_name' is set
        if ('property_name' not in params) or (params['property_name'] is None):
            raise ValueError("Missing the required parameter `property_name` when calling `cells_properties_put_document_property`")


        collection_formats = {}

        path_params = {}
        if 'name' in params:
            path_params['name'] = params['name']
        if 'property_name' in params:
            path_params['propertyName'] = params['property_name']

        query_params = []
        if 'folder' in params:
            query_params.append(('folder', params['folder']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if '_property' in params:
            body_params = params['_property']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/cells/{name}/documentproperties/{propertyName}', 'PUT',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='CellsDocumentPropertyResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
