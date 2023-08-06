# -*- coding: utf-8 -*-
"""
:created on: 25-07-2018

:copyright: 
:author: leo
:contact: 
"""


class StoreException(Exception):
    """Store base exception"""


class NameIsProtected(StoreException):
    """Exception raised when key is tried to be overridden."""


class AliasError(StoreException):
    """Exception raised if alias doesn't exist."""

class TAFileException(Exception):
    """Exception"""
    pass
