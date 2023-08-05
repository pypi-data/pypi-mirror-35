# -*- coding: utf-8 -*-
#
# Copyright (c) 2018~2999 - Cologler <skyoflw@gmail.com>
# ----------
# a global ioc
# ----------

from .ioc import ServiceProvider
from .utils import auto_inject

ioc = ServiceProvider()

def ioc_singleton(cls: type):
    ioc.register_singleton(cls.__name__, auto_inject(cls))
    return cls

def ioc_scoped(cls: type):
    ioc.register_scoped(cls.__name__, auto_inject(cls))
    return cls

def ioc_transient(cls: type):
    ioc.register_transient(cls.__name__, auto_inject(cls))
    return cls
