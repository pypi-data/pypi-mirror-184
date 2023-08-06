# SPDX-License-Identifier: MIT
"""Module to allow for backwards compatibility for existing code and extensions."""

from versacord import *

__title__ = "versacord framework"
__author__ = "versacord Developers"
__license__ = "MIT"
__copyright__ = "Copyright 022-present versacord Developers"
__version__ = "1.0.0"

__path__ = __import__("pkgutil").extend_path(__path__, __name__)
