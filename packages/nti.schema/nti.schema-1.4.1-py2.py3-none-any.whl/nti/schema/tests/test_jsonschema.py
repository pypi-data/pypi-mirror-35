#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Tests for jsonschema.py
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# stdlib imports
import unittest

from zope.interface import Interface
from zope.interface import Attribute

from .. import jsonschema
from ..field import DecodingValidTextLine

from hamcrest import assert_that
from hamcrest import has_entry
from hamcrest import is_

__docformat__ = "restructuredtext en"


#disable: accessing protected members, too many methods
#pylint: disable=W0212,R0904,inherit-non-class,no-method-argument

class TestJsonSchemafier(unittest.TestCase):

    def test_excludes(self):

        class IA(Interface):

            def method():
                "A method"

            _thing = Attribute("A private attribute")

            hidden = Attribute("Hidden attribute")
            hidden.setTaggedValue(jsonschema.TAG_HIDDEN_IN_UI, True)

        schema = jsonschema.JsonSchemafier(IA).make_schema()
        assert_that(schema, is_({}))

    def test_readonly_override(self):
        class IA(Interface):

            field = Attribute("A field")

        schema = jsonschema.JsonSchemafier(IA, readonly_override=True).make_schema()
        assert_that(schema, has_entry('field', has_entry('readonly', True)))

    def test_ui_type(self):
        class IA(Interface):

            field = Attribute("A field")
            field.setTaggedValue(jsonschema.TAG_UI_TYPE, 'MyType')

        schema = jsonschema.JsonSchemafier(IA).make_schema()
        assert_that(schema, has_entry('field', has_entry('type', 'MyType')))

    def test_type_from_types(self):

        def _assert_type(t, name='field'):
            schema = jsonschema.JsonSchemafier(IA).make_schema()
            assert_that(schema, has_entry(name, has_entry('type', t)))
            return schema

        class IA(Interface):

            field = Attribute("A field")

            field2 = DecodingValidTextLine()

        IA['field']._type = str
        _assert_type('string')

        IA['field']._type = (str,)
        _assert_type('string')


        IA['field']._type = float
        _assert_type('float')

        IA['field']._type = (float,)
        _assert_type('float')

        IA['field']._type = int
        _assert_type('int')

        IA['field']._type = (int,)
        _assert_type('int')

        IA['field']._type = bool
        _assert_type('bool')

        schema = _assert_type('string', 'field2')
        assert_that(schema, has_entry('field2', has_entry('base_type', 'string')))
