"""tools to analyze interferometric data."""
from matplotlib import colors

from ._phase import OpticalPhase
from ._zernike import defocus
from .io import read_zygo_dat, read_zygo_datx
from .fttools import forward_ft_unit
from .coordinates import cart_to_polar, uniform_cart_to_polar
from .propagation import prop_pupil_plane_to_psf_plane
from .util import share_fig_ax


from prysm import mathops as m


class Interferogram(OpticalPhase):
    """Class containing logic and data for working with interferometric data."""
    def __init__(self, phase, intensity=None, x=None, y=None, scale='px', phase_unit='nm', meta=None):
        if x is None:  # assume x, y given together
            x = m.arange(phase.shape[1])
            y = m.arange(phase.shape[0])
            scale = 'px'
            self.lateral_res = 1

        super().__init__(unit_x=x, unit_y=y, phase=phase,
                         wavelength=meta.get('wavelength'), phase_unit=phase_unit,
                         spatial_unit='m' if scale == 'px' else scale)

        self.xaxis_label = 'X'
        self.yaxis_label = 'Y'
        self.zaxis_label = 'Height'
        self.intensity = intensity
        self.meta = meta

        if scale != 'px':
            self.change_spatial_unit(to=scale, inplace=True)

        self._psd = None
        self._psdargs = {}

    @property
    def dropout_percentage(self):
        """Percentage of pixels in the data that are invalid (NaN)."""
        return m.count_nonzero(~m.isfinite(self.phase)) / self.phase.size * 100

    def fill(self, _with=0):
        """Fill invalid (NaN) values.

        Parameters
        ----------
        _with : `float`, optional
            value to fill with

        Returns
        -------
        `Interferogram`
            self

        """
        nans = ~m.isfinite(self.phase)
        self.phase[nans] = _with
        return self

    def crop(self):
        """Crop data to rectangle bounding non-NaN region."""
        nans = m.isfinite(self.phase)
        nancols = m.any(nans, axis=0)
        nanrows = m.any(nans, axis=1)

        left, right = nanrows.argmax(), nanrows[::-1].argmax()
        top, bottom = nancols.argmax(), nancols[::-1].argmax()
        if left == right == top == bottom == 0:
            return self

        self.phase = self.phase[left:-right, top:-bottom]
        self.unit_y, self.unit_x = self.unit_y[left:-right], self.unit_x[top:-bottom]
        self.unit_x -= self.unit_x[0]
        self.unit_y -= self.unit_y[0]
        return self

    def remove_piston(self):
        """Remove piston from the data by subtracting the mean value."""
        self.phase -= self.phase[m.isfinite(self.phase)].mean()
        return self

    def remove_tiptilt(self):
        """Remove tip/tilt from the data by least squares fitting and subtracting a plane."""
        plane = fit_plane(self.unit_x, self.unit_y, self.phase)
        self.phase -= plane
        return self

    def remove_power(self):
        """Remove power from the data by least squares fitting."""
        sphere = fit_sphere(self.phase)
        self.phase -= sphere
        return self

    def remove_piston_tiptilt(self):
        """Remove piston/tip/tilt from the data, see remove_tiptilt and remove_piston."""
        self.remove_piston()
        self.remove_tiptilt()
        return self

    def remove_piston_tiptilt_power(self):
        """Remove piston/tip/tilt/power from the data."""
        self.remove_piston()
        self.remove_piston_tiptilt()
        self.remove_power()
        return self

    def mask(self, mask):
        """Apply a mask to the data.

        Parameters
        ----------
        mask : `numpy.ndarray`
            masking array; expects an array of zeros (remove) and ones (keep)

        Returns
        -------
        `Interferogram`
            self

        """
        hitpts = mask == 0
        self.phase[hitpts] = m.nan
        self.intensity[hitpts] = m.nan
        return self

    def bandreject(self, wllow, wlhigh):
        """Apply a band-rejection filter to the phase (height) data.

        Parameters
        ----------
        wllow : `float`
            low wavelength (spatial period), units of self.scale
        wlhigh : `float`
            high wavelength (spatial period), units of self.scale

        Returns
        -------
        `Interferogram`
            in-place modified instance of self

        """
        new_phase = bandreject_filter(self.phase, self.sample_spacing, wllow, wlhigh)
        new_phase[~m.isfinite(self.phase)] = m.nan
        self.phase = new_phase
        return self

    def psd(self):
        """Power spectral density of the data., units (self.phase_unit^2)/((cy/self.spatial_unit)^2).

        Returns
        -------
        unit_x : `numpy.ndarray`
            ordinate x frequency axis
        unit_y : `numpy.ndarray`
            ordinate y frequency axis
        psd : `numpy.ndarray`
            power spectral density

        """
        if self._psd is None:
            self._psd = psd(self.phase, self.sample_spacing)

        return self._psd

    def psd_xy_avg(self):
        """Power spectral density of the data., units (self.phase_unit^2)/((cy/self.spatial_unit)^2).

        Returns
        -------
        `dict`
            with keys x, y, avg.  Each containing a tuple of (unit, psd)

        """
        if self._psd is None:
            self._psd = psd(self.phase, self.sample_spacing)

        x, y, _psd = self._psd
        lx, ly = len(x)//2, len(y)//2

        rho, phi, _psdrp = uniform_cart_to_polar(x, y, _psd)

        return {
            'x': (x[lx:], _psd[ly, lx:]),
            'y': (y[ly:], _psd[ly:, lx]),
            'avg': (rho, _psdrp.mean(axis=0)),
        }

    def clear_psd(self):
        """Clear cached PSD data."""
        self._psdargs = {}
        self._psd = None
        return self

    def plot_psd2d(self, axlim=None, interp_method='lanczos', fig=None, ax=None):
        """Plot the two dimensional PSD.

        Parameters
        ----------
        axlim : `float`, optional
            symmetrical axis limit
        power : `float`, optional
            inverse of power to stretch image by
        interp_method : `str`, optional
            method used to interpolate the image, passed directly to matplotlib
            imshow
        fig : `matplotlib.figure.Figure`
            Figure containing the plot
        ax : `matplotlib.axes.Axis`
            Axis containing the plot

        Returns
        -------
        fig : `matplotlib.figure.Figure`
            Figure containing the plot
        ax : `matplotlib.axes.Axis`
            Axis containing the plot

        """
        x, y, psd = self.psd()

        if axlim is None:
            lims = (None, None)
        else:
            lims = (-axlim, axlim)

        fig, ax = share_fig_ax(fig, ax)
        im = ax.imshow(psd,
                       extent=[x[0], x[-1], y[0], y[-1]],
                       origin='lower',
                       cmap='Greys_r',
                       norm=colors.LogNorm(1e-10, 1e5),
                       interpolation=interp_method)

        ax.set(xlim=lims, xlabel=r'$\nu_x$' + f'[cy/{self.spatial_unit}]',
               ylim=lims, ylabel=r'$\nu_y$' + f'[cy/{self.spatial_unit}]')

        cb = fig.colorbar(im, label=r'PSD [nm$^2$' + f'/(cy/{self.spatial_unit})]',
                          ax=ax, fraction=0.046, extend='both')
        cb.outline.set_edgecolor('k')
        cb.outline.set_linewidth(0.5)

        return fig, ax

    def plot_psd_xyavg(self, a=None, b=None, c=None,
                       xlim=None, ylim=None, fig=None, ax=None):
        """Plot the x, y, and average PSD on a linear x axis.

        Parameters
        ----------
        a : `float`, optional
            a coefficient of Lorentzian PSD model plotted alongside data
        b : `float`, optional
            b coefficient of Lorentzian PSD model plotted alongside data
        c : `float`, optional
            c coefficient of Lorentzian PSD model plotted alongside data
        xlim : `tuple`, optional
            len 2 tuple of low, high x axis limits
        ylim : `tuple`, optional
            len 2 tuple of low, high y axis limits
        fig : `matplotlib.figure.Figure`
            Figure containing the plot
        ax : `matplotlib.axes.Axis`
            Axis containing the plot

        Returns
        -------
        fig : `matplotlib.figure.Figure`
            Figure containing the plot
        ax : `matplotlib.axes.Axis`
            Axis containing the plot

        """
        xyavg = self.psd_xy_avg()
        x, px = xyavg['x']
        y, py = xyavg['y']
        r, pr = xyavg['avg']

        fig, ax = share_fig_ax(fig, ax)
        ax.loglog(x, px, lw=3, label='x', alpha=0.4)
        ax.loglog(y, py, lw=3, label='y', alpha=0.4)
        ax.loglog(r, pr, lw=3, label='avg')

        if a is not None:
            requirement = abc_psd(a, b, c, r)
            ax.loglog(r, requirement, c='k', lw=3)

        ax.legend(title='Orientation')
        ax.set(xlim=xlim, xlabel=f'Spatial Frequency [cy/{self.spatial_unit}]',
               ylim=ylim, ylabel=r'PSD [nm$^2$/' + f'(cy/{self.spatial_unit})$^2$]')

        return fig, ax

    @staticmethod
    def from_zygo_dat(path, multi_intensity_action='first', scale='um'):
        """Create a new interferogram from a zygo dat file.

        Parameters
        ----------
        path : path_like
            path to a zygo dat file
        multi_intensity_action : str, optional
            see `io.read_zygo_dat`
        scale : `str`, optional, {'um', 'mm'}
            what xy scale to label the data with, microns or mm

        Returns
        -------
        `Interferogram`
            new Interferogram instance

        """
        if str(path).endswith('datx'):
            # datx file, use datx reader
            zydat = read_zygo_datx(path)
            res = zydat['meta']['Lateral Resolution']
        else:
            # dat file, use dat file reader
            zydat = read_zygo_dat(path, multi_intensity_action=multi_intensity_action)
            res = zydat['meta']['lateral_resolution']  # meters

        phase = zydat['phase']
        if res == 0.0:
            res = 1
            scale = 'px'
        i = Interferogram(phase=phase, intensity=zydat['intensity'],
                          x=m.arange(phase.shape[1]) * res, y=m.arange(phase.shape[0]) * res,
                          scale='m', meta=zydat['meta'])
        return i.change_spatial_unit(to=scale.lower(), inplace=True)


def fit_plane(x, y, z):
    xx, yy = m.meshgrid(x, y)
    pts = m.isfinite(z)
    xx_, yy_ = xx[pts].flatten(), yy[pts].flatten()
    flat = m.ones(xx_.shape)

    coefs = m.lstsq(m.stack([xx_, yy_, flat]).T, z[pts].flatten(), rcond=None)[0]
    plane_fit = coefs[0] * xx + coefs[1] * yy + coefs[2]
    return plane_fit


def fit_sphere(z):
    x, y = m.linspace(-1, 1, z.shape[1]), m.linspace(-1, 1, z.shape[0])
    xx, yy = m.meshgrid(x, y)
    pts = m.isfinite(z)
    xx_, yy_ = xx[pts].flatten(), yy[pts].flatten()
    rho, phi = cart_to_polar(xx_, yy_)
    focus = defocus(rho, phi)

    coefs = m.lstsq(m.stack([focus, m.ones(focus.shape)]).T, z[pts].flatten(), rcond=None)[0]
    rho, phi = cart_to_polar(xx, yy)
    sphere = defocus(rho, phi) * coefs[0]
    return sphere


def bandreject_filter(array, sample_spacing, wllow, wlhigh):
    sy, sx = array.shape

    # compute the bandpass in sample coordinates
    ux, uy = forward_ft_unit(sample_spacing, sx), forward_ft_unit(sample_spacing, sy)
    fhigh, flow = 1/wllow, 1/wlhigh

    # make an ordinate array in frequency space and use it to make a mask
    uxx, uyy = m.meshgrid(ux, uy)
    highpass = ((uxx < -fhigh) | (uxx > fhigh)) | ((uyy < -fhigh) | (uyy > fhigh))
    lowpass = ((uxx > -flow) & (uxx < flow)) & ((uyy > -flow) & (uyy < flow))
    mask = highpass | lowpass

    # adjust NaNs and FFT
    work = array.copy()
    work[~m.isfinite(work)] = 0
    fourier = m.fftshift(m.fft2(m.ifftshift(work)))
    fourier[mask] = 0
    out = m.fftshift(m.ifft2(m.ifftshift(fourier)))
    return out.real


def psd(height, sample_spacing):
    """Compute the power spectral density of a signal.

    Parameters
    ----------
    height : `numpy.ndarray`
        height or phase data
    sample_spacing : `float`
        spacing of samples in the input data

    Returns
    -------
    unit_x : `numpy.ndarray`
        ordinate x frequency axis
    unit_y : `numpy.ndarray`
        ordinate y frequency axis
    psd : `numpy.ndarray`
        power spectral density

    """
    s = height.shape

    window = window_2d_welch(m.arange(s[1])*sample_spacing, m.arange(s[0])*sample_spacing)
    window = m.ones(height.shape)
    psd = prop_pupil_plane_to_psf_plane(height * window, norm='ortho')
    ux = forward_ft_unit(sample_spacing, int(round(height.shape[1], 0)))
    uy = forward_ft_unit(sample_spacing, int(round(height.shape[0], 0)))

    psd /= height.size

    # adjustment for 2D welch window bias, there is room for improvement to this
    # approximate value from:
    # Power Spectral Density Specification and Analysis of Large Optical Surfaces
    # E. Sidick, JPL
    psd /= 0.925
    return ux, uy, psd


def window_2d_welch(x, y, alpha=8):
    xx, yy = m.meshgrid(x, y)
    r, _ = cart_to_polar(xx, yy)
    rmax = m.sqrt(x.max()**2 + y.max()**2)
    window = 1 - abs(r/rmax)**alpha
    return window


def abc_psd(a, b, c, nu):
    return a / (1 + (nu/b)**2)**(c/2)
