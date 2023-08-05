# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 16:44:06 2023

@author: samuel
"""
from basics import *
from models import *
from collect import *
from visuals import *
from analyses import *
import importlib as _importlib

submodules = [
        'basics',
        'models',
        'collect',
        'visuals',
        'analyses',
    ]

__all__ = submodules

def __dir__():
        return __all__

def __getattr__(name):
    if name in submodules:
        return _importlib.import_module(f'tsma.{name}')
    else:
        try:
            return globals()[name]
        except KeyError:
            raise AttributeError(
                f"Module 'tsma' has no attribute '{name}'"
            )
