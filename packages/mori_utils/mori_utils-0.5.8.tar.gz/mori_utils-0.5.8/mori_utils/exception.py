#!/usr/bin/env python
"""
@author: Mori
@contact: moridisa@moridisa.com
@file: exception
@time: 2018/8/29 10:42 AM
@desc: Code By Mori
"""

__all__ = ['AttributeNotFound', 'ConfigNoFound']


class AttributeNotFound(KeyError):
    """
    attribute not found
    """
    pass


class ConfigNoFound(KeyError):
    """
    config name not found
    """
    pass
