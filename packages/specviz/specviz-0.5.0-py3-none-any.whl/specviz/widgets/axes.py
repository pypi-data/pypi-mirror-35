import pyqtgraph as pg
import numpy as np
import astropy.constants as const
import astropy.units as u


class DynamicAxisItem(pg.AxisItem):
    """
    Axis that understand spectral modes

    Attributes
    ----------
    mode: int
        Display mode. Can be one of:
            0: velocity
            1: redshift
            2: pixel (default)

    redshift: float
        Reference redshift.

    ref_wave: float
        Reference wavelength for velocity determination.
    """
    def __init__(self, *args, **kwargs):
        super(DynamicAxisItem, self).__init__(*args, **kwargs)
        self.mode = 2
        self.supported_modes = ['velocity', 'redshift', 'pixel']
        self._layer = None
        self.redshift = 0.0
        self.ref_wave = 0.0

    def update_axis(self, layer, mode, redshift, ref_wave):
        """
        Update axis display

        Parameters
        ----------
        layer: Spectrum1DRefLayer
            The layer to update

        mode: int
            The display mode to use.

        redshift: float
            If `mode` == `, redshift, this
            specifies the redshift.

        ref_wave: float
            if `mode` == 0, velocity, this specfies
            the reference wavelength.
        """
        self.mode = mode

        if self.mode == 0:
            self.ref_wave = ref_wave
        elif self.mode == 1:
            self.redshift = redshift
        elif self.mode == 2:
            pass

        self._layer = layer or self._layer
        self.update()
        self.hide()
        self.show()

    def tickStrings(self, values, scale, spacing):
        """
        Defines the tick marking format based on display mode

        See `~pygtgraph.AxisItem` for parameter definitions.
        """
        if self._layer is None:
            return super(DynamicAxisItem, self).tickStrings(values, scale,
                                                            spacing)

        spatial_unit = self._layer.masked_dispersion.data.unit
        dispersion = self._layer.masked_dispersion
        inds = np.arange(dispersion.size, dtype=int)

        if self.mode == 0:
            c = const.c.to('{}/s'.format(spatial_unit))

            waves = u.Quantity(np.array(values), spatial_unit)

            ref_wave = u.Quantity(self.ref_wave, spatial_unit)

            v_quant = ((waves - ref_wave) / waves * c).to('km/s')
            v = v_quant.value
            v[np.isnan(v)] = 0.0

            self.setLabel("Velocity [{}]".format(v_quant.unit), None, None)

            return ["{:.4E}".format(x) for x in v]
        elif self.mode == 1:
            self.setLabel('Redshifted Wavelength [{}]'.format(spatial_unit))

            return ["{:0.2f}".format(v / (1 + self.redshift) * scale)
                    for v in values]
        elif self.mode == 2:
            self.enableAutoSIPrefix(False)
            self.setLabel("Pixel", units=None)

            inds = np.searchsorted(dispersion, values)
            values = list(inds)

            return values

        return super(DynamicAxisItem, self).tickStrings(values, scale, spacing)
