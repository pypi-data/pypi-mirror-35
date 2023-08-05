#!/usr/bin/python
# -*- coding: utf-8 -*-
from functools import wraps

import jsonpickle
import os
import re

from urlparse import urlsplit, SplitResult


def validate_vlan_number(number):
    try:
        if int(number) > 4000 or int(number) < 1:
            return False
    except ValueError:
        return False
    return True


def validate_vlan_range(vlan_range):
    result = None
    for vlan in vlan_range.split(','):
        if '-' in vlan:
            for vlan_range_border in vlan.split('-'):
                result = validate_vlan_number(vlan_range_border)
        else:
            result = validate_vlan_number(vlan)
        if not result:
            return False
    return True


def serialize_to_json(result, unpicklable=False):
    """Serializes output as JSON and writes it to console output wrapped with special prefix and suffix

    :param result: Result to return
    :param unpicklable: If True adds JSON can be deserialized as real object.
                        When False will be deserialized as dictionary
    """

    json = jsonpickle.encode(result, unpicklable=unpicklable)
    result_for_output = str(json)
    return result_for_output


class UrlParser(object):
    SCHEME = 'scheme'
    NETLOC = 'netloc'
    PATH = 'path'
    FILENAME = 'filename'
    QUERY = 'query'
    FRAGMENT = 'fragment'
    USERNAME = 'username'
    PASSWORD = 'password'
    HOSTNAME = 'hostname'
    PORT = 'port'

    @staticmethod
    def parse_url(url):
        parsed = urlsplit(url)
        result = {}
        for attr in dir(UrlParser):
            if attr.isupper() and not attr.startswith('_'):
                attr_value = getattr(UrlParser, attr)
                if hasattr(parsed, attr_value):
                    value = getattr(parsed, attr_value)
                    if attr_value == UrlParser.PATH:
                        path, filename = os.path.split(value)
                        result[UrlParser.PATH] = path
                        result[UrlParser.FILENAME] = filename
                    else:
                        result[attr_value] = value
        return result

    @staticmethod
    def build_url(url):
        url_result = {UrlParser.QUERY: '', UrlParser.FRAGMENT: ''}
        if not url or UrlParser.SCHEME not in url or not url[UrlParser.SCHEME]:
            raise Exception('UrlParser:build_url', 'Url dictionary is empty or missing key values')

        url_result[UrlParser.SCHEME] = url[UrlParser.SCHEME]

        if UrlParser.NETLOC in url and url[UrlParser.NETLOC]:
            if UrlParser.USERNAME in url \
                    and url[UrlParser.USERNAME] \
                    and url[UrlParser.USERNAME] in url[UrlParser.NETLOC]:
                url_result[UrlParser.NETLOC] = url[UrlParser.NETLOC]
        if UrlParser.NETLOC not in url_result:
            url_result[UrlParser.NETLOC] = url[UrlParser.HOSTNAME]
            if UrlParser.PORT in url and url[UrlParser.PORT]:
                url_result[UrlParser.NETLOC] += ':{}'.format(url[UrlParser.PORT])
            if UrlParser.USERNAME in url and url[UrlParser.USERNAME]:
                credentials = '{}@'.format(url[UrlParser.USERNAME])
                if UrlParser.PASSWORD in url and url[UrlParser.PASSWORD]:
                    credentials = '{}:{}@'.format(url[UrlParser.USERNAME], url[UrlParser.PASSWORD])
                url_result[UrlParser.NETLOC] = credentials + url_result[UrlParser.NETLOC]

        url_result[UrlParser.PATH] = url[UrlParser.FILENAME]
        if UrlParser.PATH in url and url[UrlParser.PATH]:
            url_result[UrlParser.PATH] = url[UrlParser.PATH] + '/' + url_result[UrlParser.PATH]
            url_result[UrlParser.PATH] = re.sub('//+', '/', url_result[UrlParser.PATH])

        if UrlParser.QUERY in url and url[UrlParser.QUERY]:
            url_result[UrlParser.QUERY] = url[UrlParser.QUERY]

        result = SplitResult(**url_result)
        return result.geturl()


def command_logging(func):
    @wraps(func)
    def wrapped(self, *args, **kwargs):
        func_name = func.__name__

        self._logger.info('Start command "{}"'.format(func_name))
        finishing_msg = 'Command "{}" finished {}'
        try:
            result = func(self, *args, **kwargs)
        except Exception:
            self._logger.info(finishing_msg.format(func_name, 'unsuccessfully'))
            raise
        else:
            self._logger.info(finishing_msg.format(func_name, 'successfully'))

        return result
    return wrapped
