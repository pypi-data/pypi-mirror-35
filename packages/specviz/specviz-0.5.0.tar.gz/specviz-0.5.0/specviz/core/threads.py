"""
Thread Helpers
"""
from qtpy.QtCore import QThread, Signal
import os
import logging

from ..core.data import Spectrum1DRef, Spectrum1DRefModelLayer
from ..interfaces.factories import FitterFactory
from ..core.linelist import LineList

import astropy.io.registry as io_registry

__all__ = [
    'FileLoadThread',
    'LineListLoadThread',
    'FitModelThread',
]

class FileLoadThread(QThread):
    """
    Asynchronously read in a file

    Parameters
    ----------
    parent: QtWidget
        The parent widget or None

    Call
    ----
    file_name: str
        Name of the file to read.

    file_filter: str
        Type of file to read.

    Attributes
    ----------
    file_name: str
        Name of the file to read.

    file_filter: str
        Type of file to read. If `Auto`, try all known formats.

    Signals
    -------
    status(message, timeout)
        State of the thread
            message: The status message
            timeout: Time (msec) to display message

    result(Spectrum1DRef)
        The file's data
    """
    status = Signal(str, int)
    result = Signal(Spectrum1DRef)

    def __init__(self, parent=None):
        super(FileLoadThread, self).__init__(parent)
        self.file_name = ""
        self.file_filter = ""

    def __call__(self, file_name, file_filter):
        """
        Initialize the thread
        """
        self.file_name = file_name
        self.file_filter = file_filter

    def run(self):
        """
        Start thread to read the file.
        """
        self.status.emit("Loading file...", 0)
        data = self.read_file(self.file_name, self.file_filter)

        if data is not None:
            self.status.emit("File loaded successfully!", 5000)
        else:
            self.status.emit("An error occurred while loading file.", 5000)

        if data is not None:
            self.result.emit(data)
        else:
            logging.error("Could not open file.")

    def read_file(self, file_name, file_filter):
        """
        Convenience method that directly reads a spectrum from a file.

        Parameters
        ----------
        file_name: str
            Name of the file to read.

        file_filter: str
            Type of file to read. If `Auto`, try all known formats.

        Returns
        -------
        data: Spectrum1DRef
            The file's data or None if no known formats are found.

        Notes
        -----
        This exists mostly to facilitate development workflow. In time it
        could be augmented to support fancier features such as wildcards,
        file lists, mixed file types, and the like.
        Note that the filter string is hard coded here; its details might
        depend on the intrincacies of the registries, loaders, and data
        classes. In other words, this is brittle code.
        """
        file_filter = 'Auto (*)' if file_filter is None else file_filter

        logging.info("Attempting to read file {} with {}.".format(file_name, file_filter))

        if not (file_name and file_filter):
            return

        file_name = str(file_name)
        file_ext = os.path.splitext(file_name)[-1]
        all_formats = io_registry.get_formats(Spectrum1DRef)['Format']

        if file_filter == 'Auto (*)':
            #-- sort loaders by priorty given in the definition
            all_priority = [getattr(io_registry.get_reader(fmt, Spectrum1DRef), 'priority', 0) for fmt in all_formats]
            all_registry = sorted(zip(all_formats, all_priority), key=lambda item: item[1], reverse=True)
            all_formats = [item[0] for item in all_registry]
        else:
            all_formats = [x for x in all_formats if file_filter in x]

        for format in all_formats:
            logging.info("Trying to load with {}".format(format))
            try:
                data = Spectrum1DRef.read(file_name, format=format)
                return data
            except Exception as e:
                logging.error("Incompatible loader for selected data: {"
                              "} because {}".format(file_filter, e))


class LineListLoadThread(FileLoadThread):
    """
    Asynchronously read in a line list.

    Extends functionality in the main file load thread
    to handle the specifics of a line list.

    Parameters
    ----------
    parent: QtWidget
        The parent widget or None

    Call
    ----
    file_name: str
        Name of the file to read.

    file_filter: str
        Type of file to read.

    Attributes
    ----------
    file_name: str
        Name of the file to read.

    file_filter: str
        Type of file to read. If `Auto`, try all known formats.

    Signals
    -------
    status(message, timeout)
        State of the thread
            message: The status message
            timeout: Time (msec) to display message

    result(LineList)
        The line list's data
    """
    status = Signal(str, int)
    result = Signal(LineList)

    def __init__(self, linelist, metadata, parent=None):
        super(LineListLoadThread, self).__init__(parent)
        self.file_name = linelist
        self.metadata = metadata

    def read_file(self, file_name, file_filter):
        """
        Directly reads a line list from a file.

        Parameters
        ----------
        file_name: str
            Name of the file to read.

        file_filter: str
            Type of file to read. If `Auto`, try all known formats.

        Returns
        -------
        data: LineList
            The file's data or None if no known formats are found.

        Notes
        -----
        """
        file_filter = 'Auto (*)' if file_filter is None else file_filter

        # logging.info("Attempting to read file {} with {}.".format(file_name, file_filter))
        #
        # if not (file_name and file_filter):
        #     return
        #
        # file_name = str(file_name)
        # file_ext = os.path.splitext(file_name)[-1]
        # all_formats = io_registry.get_formats(Spectrum1DRef)['Format']
        #
        # if file_filter == 'Auto (*)':
        #     #-- sort loaders by priorty given in the definition
        #     all_priority = [getattr(io_registry.get_reader(fmt, Spectrum1DRef), 'priority', 0) for fmt in all_formats]
        #     all_registry = sorted(zip(all_formats, all_priority), key=lambda item: item[1], reverse=True)
        #     all_formats = [item[0] for item in all_registry]
        # else:
        #     all_formats = [x for x in all_formats if file_filter in x]
        #
        # for format in all_formats:
        #     logging.info("Trying to load with {}".format(format))
        #     try:
        #         data = Spectrum1DRef.read(file_name, format=format)
        #         return data
        #     except Exception as e:
        #         logging.error("Incompatible loader for selected data: {"
        #                       "} because {}".format(file_filter, e))


class FitModelThread(QThread):
    """
    Asynchronously fit a model to a layer

    Parameters
    ----------
    parent: QtWidget
        The parent widget or None

    Call
    ----
    model_layer: Spectrum1DRefLayer
        The layer to fit to.

    fitter_name: An `~astropy.modeling` fitter
        The fitter to use

    mask: numpy.ndarray
        The mask to apply

    Attributes
    ----------
    model_layer: Spectrum1DRefLayer
        The layer to fit to.

    fitter_name: An `~astropy.modeling` fitter
        The fitter to use

    mask: numpy.ndarray
        The mask to apply

    Signals
    -------
    status(message, timeout)
        State of the thread
            message: The status message
            timeout: Time (msec) to display message

    result(Spectrum1DRefModelLayer)
        The fit
    """
    status = Signal(str, int)
    result = Signal(Spectrum1DRefModelLayer)

    def __init__(self, parent=None):
        super(FitModelThread, self).__init__(parent)
        self.model_layer = None
        self.fitter_name = ""

    def __call__(self, model_layer, fitter_name, mask=None, kwargs=None):
        self.model_layer = model_layer
        self.fitter_name = fitter_name
        self.mask = mask
        self.kwargs = kwargs or {}

    def run(self):
        """
        Start thread to fit the model
        """
        self.status.emit("Fitting model...", 0)
        model_layer, message = self.fit_model(self.model_layer,
                                              self.fitter_name,
                                              self.mask,
                                              self.kwargs)

        if not message:
            self.status.emit("Fit completed successfully!", 5000)
        else:
            self.status.emit("Fit completed, but with warnings.", 5000)

        self.result.emit(model_layer)

    def fit_model(self, model_layer, fitter_name, mask=None, kwargs=None):
        """
        Fit the model

        Parameters
        ----------
        model_layer: Spectrum1DRefLayer
            The layer to fit to.

        fitter_name: An `~astropy.modeling` fitter
            The fitter to use

        mask: numpy.ndarray
            The mask to apply

        Returns
        -------
        (model_layer, fitter_message): Spectrum1DRefLayer, str
            The model_layer.model is updated with the fit paramters.
            The message is from the fitter itself.
        """
        if not hasattr(model_layer, 'model'):
            logging.warning("This layer has no model to fit.")
            return

        # When fitting, the selected layer is a ModelLayer, thus
        # the data to be fitted resides in the parent
        parent_layer = model_layer._parent

        if parent_layer is None:
            return

        flux = parent_layer.masked_data
        dispersion = parent_layer.masked_dispersion
        model = model_layer.model

        # The fitting should only consider the masked regions
        flux = flux[mask].compressed().value
        dispersion = dispersion[mask].compressed().value

        # Get compressed versions of the data arrays
        # flux = flux.compressed().value
        # dispersion = dispersion.compressed().value

        # If the number of parameters is greater than the number of data
        # points, bail
        if len(model.parameters) > flux.size:
            logging.warning("Unable to perform fit; number of parameters is "
                            "greater than the number of data points.")
            return

        # Perform fitting of model
        if fitter_name:
            fitter = FitterFactory.all_fitters[fitter_name]()
        else:
            fitter = FitterFactory.default_fitter()

        # Ensure that the fitter contains the keys in kwargs
        kwargs = {k: v for k, v in kwargs.items() if hasattr(fitter, k)}

        fitted_model = fitter(model, dispersion, flux, **(kwargs or {}))

        if 'message' in fitter.fit_info:
            # The fitter 'message' should probably be logged at INFO level.
            # Problem is, info messages do not display in the error console,
            # and we, ideally, want the user to see the message immediately
            # after the fit is executed.
            logging.warning(fitter.fit_info['message'])

        # Update original model with new values from fitted model
        if hasattr(fitted_model, '_submodels'):
            for i in range(len(fitted_model._submodels)):
                for pname in model._submodels[i].param_names:
                    value = getattr(fitted_model, "{}_{}".format(pname, i))
                    setattr(model._submodels[i], pname, value.value)
                    setattr(model[i], pname, value.value)
        else:
            for pname in model.param_names:
                value = getattr(fitted_model, "{}".format(pname))
                setattr(model, pname, value.value)
        # model_layer.model = fitted_model

        # update GUI with fit results

        return model_layer, fitter.fit_info.get('message', "")
