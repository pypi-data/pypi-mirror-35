# -*- coding: utf-8 -*-

"""Main module."""

import random, string

# STANDARD IMPORTS
def unique_id():
    return ''.join(random.choice(string.ascii_lowercase) for i in range(25))
