# coding: utf-8

"""
    Devdraft Payment & Business Management API

     A comprehensive payment processing and business management API that enables seamless integration of cryptocurrency and traditional payment methods.       # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from devdraft_ai_sdk.api_client import ApiClient


class WebhooksApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def webhook_controller_create(self, body, **kwargs):  # noqa: E501
        """Create a new webhook  # noqa: E501

        Creates a new webhook endpoint for receiving event notifications. Requires webhook:create scope.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.webhook_controller_create(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateWebhookDto body: Webhook configuration details (required)
        :return: WebhookResponseDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.webhook_controller_create_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.webhook_controller_create_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def webhook_controller_create_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create a new webhook  # noqa: E501

        Creates a new webhook endpoint for receiving event notifications. Requires webhook:create scope.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.webhook_controller_create_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateWebhookDto body: Webhook configuration details (required)
        :return: WebhookResponseDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method webhook_controller_create" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `webhook_controller_create`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-client-key', 'x-client-secret']  # noqa: E501

        return self.api_client.call_api(
            '/api/v0/webhooks', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WebhookResponseDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def webhook_controller_find_all(self, **kwargs):  # noqa: E501
        """Get all webhooks  # noqa: E501

        Retrieves a list of all webhooks for your application. Requires webhook:read scope.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.webhook_controller_find_all(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float skip: Number of records to skip (default: 0)
        :param float take: Number of records to return (default: 10)
        :return: list[WebhookResponseDto]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.webhook_controller_find_all_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.webhook_controller_find_all_with_http_info(**kwargs)  # noqa: E501
            return data

    def webhook_controller_find_all_with_http_info(self, **kwargs):  # noqa: E501
        """Get all webhooks  # noqa: E501

        Retrieves a list of all webhooks for your application. Requires webhook:read scope.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.webhook_controller_find_all_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float skip: Number of records to skip (default: 0)
        :param float take: Number of records to return (default: 10)
        :return: list[WebhookResponseDto]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['skip', 'take']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method webhook_controller_find_all" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
        if 'take' in params:
            query_params.append(('take', params['take']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-client-key', 'x-client-secret']  # noqa: E501

        return self.api_client.call_api(
            '/api/v0/webhooks', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[WebhookResponseDto]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def webhook_controller_find_one(self, id, **kwargs):  # noqa: E501
        """Get a webhook by id  # noqa: E501

        Retrieves details for a specific webhook. Requires webhook:read scope.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.webhook_controller_find_one(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Webhook ID (required)
        :return: WebhookResponseDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.webhook_controller_find_one_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.webhook_controller_find_one_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def webhook_controller_find_one_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get a webhook by id  # noqa: E501

        Retrieves details for a specific webhook. Requires webhook:read scope.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.webhook_controller_find_one_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Webhook ID (required)
        :return: WebhookResponseDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method webhook_controller_find_one" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `webhook_controller_find_one`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-client-key', 'x-client-secret']  # noqa: E501

        return self.api_client.call_api(
            '/api/v0/webhooks/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WebhookResponseDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def webhook_controller_remove(self, id, **kwargs):  # noqa: E501
        """Delete a webhook  # noqa: E501

        Deletes a webhook configuration. Requires webhook:delete scope.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.webhook_controller_remove(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Webhook ID (required)
        :return: WebhookResponseDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.webhook_controller_remove_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.webhook_controller_remove_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def webhook_controller_remove_with_http_info(self, id, **kwargs):  # noqa: E501
        """Delete a webhook  # noqa: E501

        Deletes a webhook configuration. Requires webhook:delete scope.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.webhook_controller_remove_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Webhook ID (required)
        :return: WebhookResponseDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method webhook_controller_remove" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `webhook_controller_remove`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-client-key', 'x-client-secret']  # noqa: E501

        return self.api_client.call_api(
            '/api/v0/webhooks/{id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WebhookResponseDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def webhook_controller_update(self, body, id, **kwargs):  # noqa: E501
        """Update a webhook  # noqa: E501

        Updates an existing webhook configuration. Requires webhook:update scope.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.webhook_controller_update(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UpdateWebhookDto body: Webhook update details (required)
        :param str id: Webhook ID (required)
        :return: WebhookResponseDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.webhook_controller_update_with_http_info(body, id, **kwargs)  # noqa: E501
        else:
            (data) = self.webhook_controller_update_with_http_info(body, id, **kwargs)  # noqa: E501
            return data

    def webhook_controller_update_with_http_info(self, body, id, **kwargs):  # noqa: E501
        """Update a webhook  # noqa: E501

        Updates an existing webhook configuration. Requires webhook:update scope.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.webhook_controller_update_with_http_info(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UpdateWebhookDto body: Webhook update details (required)
        :param str id: Webhook ID (required)
        :return: WebhookResponseDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method webhook_controller_update" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `webhook_controller_update`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `webhook_controller_update`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-client-key', 'x-client-secret']  # noqa: E501

        return self.api_client.call_api(
            '/api/v0/webhooks/{id}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WebhookResponseDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
