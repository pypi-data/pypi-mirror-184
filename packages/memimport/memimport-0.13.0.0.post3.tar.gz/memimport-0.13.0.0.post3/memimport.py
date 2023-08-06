r'''memimport - an import function which can import extension modules
from memory without write them to the file system.

The _memimporter module is part of the py2exe package.

Overview
========

It uses the _memimporter extension which uses code from Joachim
Bauch's MemoryModule library. This library emulates the win32 api
function LoadLibrary.

memimport provides a loader MemExtensionFileLoader for basic usage.
Users should write a custom loader for specific requirement,
just likes zipextimporter does.

Sample usage
============

>>> from memimport import memimport
>>> data = some_gen(*any_args)  # read from Disk or Web
>>> mem_mod = memimport(data=get_data, fullname='mem_mod')
>>> print(mem_mod)
<module 'mem_mod' from '<unknown>'>
>>> mem_mod.__file__
'<unknown>'
>>> mem_mod.__loader__
<memimport.MemExtensionFileLoader object at 0x0000000001132E90>
>>> # Reloading will not works:
>>> import importlib
>>> importlib.reload(mem_mod)
'Some error message'
>>>

'''

import os
import sys
from importlib.machinery import ExtensionFileLoader, ModuleSpec

# _memimporter is a module built into the py2exe runstubs,
# or a standalone module of memimport.
from _memimporter import import_module, get_verbose_flag


__version__ = '0.13.0.0.post3'

__all__ = [
    'memimport_from_data', 'memimport_from_loader', 'memimport_from_spec',
    'memimport', 'get_verbose_flag', 'set_verbose'
]


class MemExtensionFileLoader(ExtensionFileLoader):

    def create_module(self, spec):
        pass

    def exec_module(self, module):
        pass

    def load_module(self, fullname):
        pass


def memimport_from_data(fullname, data, is_package=None):
    return memimport(data=data, fullname=fullname, is_package=is_package)

def memimport_from_loader(fullname, loader, data=None, is_package=None):
    return memimport(data=data, loader=loader, fullname=fullname, is_package=is_package)

def memimport_from_spec(spec, data=None, is_package=None):
    return memimport(data=data, spec=spec, is_package=is_package)


def memimport(data=None, spec=None,
              fullname=None, loader=None, origin=None, is_package=None):
    if spec:
        if not fullname:
            fullname = spec.name
        if is_package and spec.submodule_search_locations is None:
            spec.submodule_search_locations = []
    elif fullname:
        if not origin:
            try:
                origin = loader.get_filename(fullname)
            except (NameError, AttributeError):
                if data is None:
                    raise ValueError(
                        f'loader {loader} has no `get_filename` attribute, '
                        'so argument "data" or "origin" MUST be provided.'
                        )
                origin = '<unknown>'
        origin = origin.replace('/', '\\')
        if loader is None:
            if data is None:
                if not os.path.isfile(origin):
                    raise ValueError('argument "loader" MUST be provided, or '
                                     'argument "origin" MUST be a locale file.')
                loader = ExtensionFileLoader(fullname, origin)
            else:
                loader = MemExtensionFileLoader(fullname, origin)
        if is_package is None:
            is_package = loader.is_package(fullname)
        spec = ModuleSpec(fullname, loader, origin=origin, is_package=is_package)
    else:
        raise ValueError('argument "spec" or "fullname" MUST be provided.')

    loader = spec.loader
    origin = spec.origin
    sub_search = spec.submodule_search_locations
    spec._set_fileattr = origin != '<unknown>'  # has_location, use for reload
    if sub_search is not None and not sub_search:
        sub_search.append(origin.rpartition('\\')[0])

    MEMIMPORTPATH = 'MEMIMPORT|' + fullname
    initname = 'PyInit_' + fullname.rpartition('.')[2]

    def get_data(path):
        if path != MEMIMPORTPATH:
            return loader.get_data(path)
        if callable(data):
            return data()
        if data:
            return data
        return loader.get_data(origin)

    mod = import_module(fullname, MEMIMPORTPATH, initname, get_data, spec)
    # init attributes
    mod.__spec__ = spec
    mod.__file__ = origin
    mod.__loader__ = loader
    mod.__package__ = spec.parent
    if sub_search is not None:
        mod.__path__ = sub_search
    if verbose > 1:
        print(f'memimport {fullname} # loaded from {origin}',
              file=sys.stderr)
    return mod


verbose = get_verbose_flag()

def set_verbose(i):
    '''Set verbose, the argument as same as built-in function int's.'''
    global verbose
    verbose = int(i)
