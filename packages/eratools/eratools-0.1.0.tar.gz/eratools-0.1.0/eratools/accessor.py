from typing import List
import numpy as np
import xarray as xr
from scipy.interpolate import interp1d
from .modeldefs import era5levels, eraintlevels
from .geopotential import geopotential2geometric
import logging


@xr.register_dataset_accessor('era')
class ERAML(object):
    def __init__(self, ds: xr.Dataset):
        logging.info(f'Initializing dataset with type ERAML (ERA model level)')

        self._obj: xr.Dataset = ds

        # Drop all the extra NaN's from ground geopotential height (z) and surface pressure (lnsp)
        if 'level' in ds.z.dims:
            self._obj['z'] = ds.z.isel(level=0)
        if 'level' in ds.lnsp.dims:
            self._obj['lnsp'] = ds.lnsp.isel(level=0)

        # Add a 360 longitude entry if the data wraps
        if ds.longitude.min() == 0.0 and 359.0 < ds.longitude.max() < 360.0:
            lon0 = ds.sel(longitude=0.0)
            lon0['longitude'] = 360
            self._obj = xr.concat([ds, lon0], 'longitude')

    def extend(self):
        logging.info(f'Extending ERAML dataset (adding pressure, temperature, heights)')

        era_dict = {60: eraintlevels(), 137: era5levels()}

        level = era_dict[self._obj.sizes['level']]

        pressure = (level.a + level.b * np.exp(self._obj.lnsp)) / 100
        self._obj['pressure'] = pressure

        self._obj['full_pressure'] = pressure.rolling(level=2, min_periods=1).mean()
        self._obj['full_pressure'].loc[dict(level=1)] = 0.5 * pressure.sel(level=1)

        virtual_temperature = self._obj.t * (1.0 + 0.609133 * self._obj.q)

        # I do not calculate the geopotential of the 0th half pressure as the corresponding half pressure is 0.0
        dlogp = np.log(pressure.shift(level=-1) / pressure)
        h = 287.058 * virtual_temperature.shift(level=-1) * dlogp
        self._obj['geopotential_height'] = self._obj.z + h.sortby('level', ascending=False).cumsum(dim='level')

        self._obj['height'] = geopotential2geometric(self._obj.geopotential_height, self._obj.latitude)

    def airdensityonalt(self, latitude: float, longitude: float, time: np.datetime64, altitudes):
        interped = self._obj.interp(latitude=latitude, longitude=longitude, time=time)
        return interp1d(x=interped.height, y=interped.pressure, bounds_error=False)(altitudes)

    def interp2points(self, latitude: List[float], longitude: List[float], time: List[np.datetime64]):
        return self._obj.interp(latitude=latitude, longitude=longitude, time=time)
