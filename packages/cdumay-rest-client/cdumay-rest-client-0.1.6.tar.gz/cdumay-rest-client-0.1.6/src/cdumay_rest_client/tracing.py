#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. codeauthor:: Cédric Dumay <cedric.dumay@gmail.com>


"""
import opentracing
from cdumay_opentracing import OpenTracingDriver


class RestDriver(OpenTracingDriver):
    FORMAT = opentracing.Format.HTTP_HEADERS

    @classmethod
    def extract(cls, data):
        """ Extract span context from a `carrier` object

        :param Any data: the `carrier` object.
        :return: a SpanContext instance extracted from `carrier` or None if no
            such span context could be found.
        """
        return opentracing.tracer.extract(cls.FORMAT, data.headers)

    @classmethod
    def tags(cls, data):
        """ Extract tags from `carrier` object.

        :param Any data: the `carrier` object.
        :return: Tags to add on span
        :rtype: dict
        """
        return dict()
