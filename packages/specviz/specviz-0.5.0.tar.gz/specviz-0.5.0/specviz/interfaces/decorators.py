from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import logging
from functools import wraps

import astropy.io.registry as io_registry

from ..core.data import Spectrum1DRef

__all__ = ['data_loader']

def data_loader(label, identifier, priority=-1, extensions=None, writer=None,
                **kwargs):
    """
    A decorator that registers a function and identifies with an Astropy io
    registry object.

    Priority will be assigned as an attribute to the wrapped function for use
    in the auto loader.  Loaders with high numerical value will be tried first,
    followed by low numerical value in order.

    Parameters
    ----------
    label : str
        user-fiendly name for the data loader
    identifier : function
        function used to determine if the loader should be used on the Input
    priority : int
        absolute priority to determine which loader to attempt first
    """
    if extensions is None:
        extensions = ["*"]
    else:
        extensions = ["*.{}".format(ext) if not ext.startswith("*.") else ext
                      for ext in extensions]

        if "*.fits" in extensions:
            extensions += ["*fits.gz"]

    def decorator(func):
        """
        Parameters
        ----------
        func : function
            Function added to the registry in order to read data files.
        """

        logging.info("Added {} to loader registry.".format(label))

        func.loader_wrapper = True
        func.priority = priority

        format = label + " ({})".format(" ".join(extensions))

        if format in io_registry.get_formats()['Format']:
            return

        io_registry.register_reader(format, Spectrum1DRef, func)

        if writer is not None:
            io_registry.register_writer(format, Spectrum1DRef, writer)

        io_registry.register_identifier(format, Spectrum1DRef,
                                        identifier)

        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper

    return decorator


def data_writer(spectrum, label, **kwargs):
    def decorator(func):
        logging.info("Added {} to writer registry.".format(label))

        func.loader_wrapper = True

        loaders = io_registry.get_formats(Spectrum1DRef)['Format'].data
        format = [x for x in loaders if label in x]

        format = label if len(format) == 0 else format[0]

        io_registry.register_writer(format, Spectrum1DRef, func)

        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper

    return decorator
