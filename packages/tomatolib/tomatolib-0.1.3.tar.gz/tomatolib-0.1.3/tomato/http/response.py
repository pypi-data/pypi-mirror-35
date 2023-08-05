#!/usr/bin/python3
# -*- coding:utf-8 -*-

"""
    @file:      response.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    @auther:    Tangmi(tangmi360@gmail.com)
    @date:      June 21, 2018
    @desc:      Response class
"""


class Response(object):

    def __init__(self):
        self._meta = {}
        self._resp = None
        self._data = None

    def __getattr__(self, attr):
        if self._resp:
            return getattr(self._resp, attr)
        else:
            object.__getattribute__(self, attr)

    @property
    def resp(self):
        return self._resp

    @resp.setter
    def resp(self, resp):
        self._resp = resp

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data

    @property
    def meta(self):
        return self._meta

    @meta.setter
    def meta(self, meta):
        if isinstance(meta, dict):
            self._meta = meta
