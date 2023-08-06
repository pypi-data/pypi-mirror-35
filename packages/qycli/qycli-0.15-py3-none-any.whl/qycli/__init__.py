# coding: utf-8 2018/9/4 14:45
import os
from collections import namedtuple

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

ArgumentInfo = namedtuple(
    'ArgumentInfo',
    [
        "shot_name",
        "full_name",
        "dest",
        "action",
        "type",
        "default",
        "help",
    ]
)
