#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Date Format: YYYY-MM-DD
#
# This file is part of RTFDE, a RTF De-Encapsulator.
# Copyright © 2020 seamus tuohy, <code@seamustuohy.com>
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the included LICENSE file for details.

"""
RTFDE: A python3 library for extracting HTML content from RTF encapsulated HTML.

https://github.com/seamustuohy/RTF_De-Encapsulator
"""

__author__ = 'seamus tuohy'
__date__ = '2020-12-05'
__version__ = '0.1.0'

import logging
from logging import NullHandler

logging.getLogger(__name__).addHandler(NullHandler())
logging.getLogger(__name__ + ".tree_logger").addHandler(NullHandler())



from RTFDE.deencapsulate import DeEncapsulator
