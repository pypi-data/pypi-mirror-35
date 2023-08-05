import inspect
import sys
import warnings

import gc
from inspect import getfile

import zope.proxy

class LazyVariable(object):

    def __init__(self, specifier):
        self.specifier = specifier

    def get(self):
        return self.specifier()

class DeferredAndDeprecated(LazyVariable):

    def __init__(self, specifier, message):
        super(DeferredAndDeprecated, self).__init__(specifier)
        self.message = message

    def get(self):
        warnings.warn(
            self.__name__ + " is deprecated. " + self.message,
            DeprecationWarning, stacklevel=3)

        return super(DeferredAndDeprecated, self).get()

class ModuleProxy(zope.proxy.ProxyBase):
    __slots__ = ('__deferred_definitions__', '__doc__')

    def __init__(self, module):
        super(ModuleProxy, self).__init__(module)
        self.__deferred_definitions__ = {}
        self.__doc__ = module.__doc__

    def __getattr__(self, name):
        try:
            get = self.__deferred_definitions__.pop(name)
        except KeyError:
            raise AttributeError(name)
        v = get.get()
        setattr(self, name, v)
        return v

def initialize(level=1):
    """Prepare a module to support deferred imports.

    Modules do not need to call this directly, because the
    `define*` and `deprecated*` functions call it.

    This is intended to be called from the module to be prepared.
    The implementation wraps a proxy around the module and replaces
    the entry in sys.modules with the proxy.  It does no harm to
    call this function more than once for a given module, because
    this function does not re-wrap a proxied module.

    The level parameter specifies a relative stack depth.
    When this function is called directly by the module, level should be 1.
    When this function is called by a helper function, level should
    increase with the depth of the stack.

    Returns nothing when level is 1; otherwise returns the proxied module.
    """
    __name__ = sys._getframe(level).f_globals['__name__']
    module = sys.modules[__name__]
    if type(module) is not ModuleProxy:
        module = ModuleProxy(module)
        sys.modules[__name__] = module

    if level == 1:
        return
    return module

def get_variable_name():
    f = inspect.currentframe().f_back.f_back
    filename = getfile(f)
    code_line = open(filename).readlines()[f.f_lineno - 1]
    assigned_variable = code_line.split("=")[0].strip()
    return assigned_variable

def find_names(self):
    frame = inspect.currentframe()
    for frame in iter(lambda: frame.f_back, None):
        frame.f_locals
    obj_names = []
    for referrer in gc.get_referrers(self):
        if isinstance(referrer, dict):
            for k, v in referrer.items():
                if v is self:
                    obj_names.append(k)
    print(obj_names)

def define(name, func):
    module = initialize(2)
    # name = get_variable_name()
    __deferred_definitions__ = module.__deferred_definitions__
    __deferred_definitions__[name] = LazyVariable(func)

def defineFrom(from_name, *names):
    """Define deferred imports from a particular module.

    The from_name specifies which module to import.
    The rest of the parameters specify names to import from that module.
    """
    module = initialize(2)
    __deferred_definitions__ = module.__deferred_definitions__
    for name in names:
        specifier = from_name + ':' + name
        __deferred_definitions__[name] = LazyVariable(specifier)

def deprecated(message, **names):
    """Define deferred and deprecated imports using keyword parameters.

    The first use of each name will generate a deprecation warning with
    the given message.

    Each parameter specifies the importable name and how to import it.
    Use `module:name` syntax to import a name from a module, or `module`
    (no colon) to import a module.
    """
    module = initialize(2)
    __deferred_definitions__ = module.__deferred_definitions__
    for name, specifier in names.items():
        __deferred_definitions__[name] = DeferredAndDeprecated(specifier, message)

def deprecatedFrom(message, from_name, *names):
    """Define deferred and deprecated imports from a particular module.

    The first use of each name will generate a deprecation warning with
    the given message.

    The from_name specifies which module to import.
    The rest of the parameters specify names to import from that module.
    """
    module = initialize(2)
    __deferred_definitions__ = module.__deferred_definitions__
    for name in names:
        specifier = from_name + ':' + name
        __deferred_definitions__[name] = DeferredAndDeprecated(specifier, message)
