#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ruamel.yaml.scalarstring import DoubleQuotedScalarString, SingleQuotedScalarString
from public import public


@public
def single(value):
    return SingleQuotedScalarString(value)


@public
def double(value):
    return DoubleQuotedScalarString(value)
