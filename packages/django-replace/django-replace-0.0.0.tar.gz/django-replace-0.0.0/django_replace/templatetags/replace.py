#!/usr/bin/env python
import re
from django import template

register = template.Library()

# {{ value|replace:",old,new" }}


@register.filter
def replace(string, argument):  # multiple arguments not suported
    ignore, search, replace = argument.split(argument[0])
    return re.sub(search, replace, string)
