#!/bin/env python
# -*- coding: utf-8 -*-

from django import template

register = template.Library()

@register.simple_tag
def query_transform(request, **kwargs):
    updated = request.GET.copy()

    for key, value in kwargs.iteritems():
        updated[key] = value

    return updated.urlencode()
