# -*- coding: utf-8 -*-
#
# Copyright (c) 2018~2999 - Cologler <skyoflw@gmail.com>
# ----------
# a global ioc
# ----------

from .ioc import ServiceProvider
from .utils import auto_inject, dispose_at_exit

ioc = ServiceProvider()
dispose_at_exit(ioc)

def ioc_singleton(cls: type):
    ioc.register_singleton(cls.__name__, auto_inject(cls))
    return cls

def ioc_scoped(cls: type):
    ioc.register_scoped(cls.__name__, auto_inject(cls))
    return cls

def ioc_transient(cls: type):
    ioc.register_transient(cls.__name__, auto_inject(cls))
    return cls

def ioc_bind(new_key):
    '''
    bind with new key.
    '''
    def binding(cls):
        name = cls.__name__
        ioc.register_transient(new_key, lambda x: x[name])
        return cls
    return binding
