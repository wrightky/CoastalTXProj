#!/usr/bin/env python
"""

"""
import numpy as np
import xarray as xr
import matplotlib

class CoaTX_Projection():
    """
    Class for transforming longitude/latitude coordinates into along-coast pseudo-coordinates
    """
    def __init__(self):
        """
        Read grid information and build the geotransform interpolation functions
        """
        ds = xr.open_dataset(r'transform_grid.nc')
        self.lat = ds['lat'].to_numpy()
        self.lon = ds['lon'].to_numpy()
        self.h = ds['h'].to_numpy()
        self.s = ds['s'].to_numpy()
        self.mesh = ds['mesh'].to_numpy()
        
        self.triang = matplotlib.tri.Triangulation(
            self.lon.ravel(), self.lat.ravel(), self.mesh
        )
        
        self.interp_h = matplotlib.tri.LinearTriInterpolator(self.triang, self.h.ravel())
        self.interp_s = matplotlib.tri.LinearTriInterpolator(self.triang, self.s.ravel())
    
    def __call__(self, coordinates):
        """
        Method for translating degree coordinates into the linear coast projection.
        Note that coordinates expected in [x,y] order, i.e. [longitude, latitude]
        
        **Inputs**
            coordinates (list or array) : Degree coordinates to be transformed, with
                longitude in the first column of the array and latitude in the second.
        **Outputs**
            Array of transformed coordinates, with the first column being 'distance along
                coast' and the second column being 'distance inland'.
        """
        coordinates = np.array(coordinates)
        try:
            s_values = self.interp_s(coordinates[:,0], coordinates[:,1]).filled(np.nan)
            h_values = self.interp_h(coordinates[:,0], coordinates[:,1]).filled(np.nan)
        except IndexError:
            s_values = self.interp_s(coordinates[0], coordinates[1]).filled(np.nan)
            h_values = self.interp_h(coordinates[0], coordinates[1]).filled(np.nan)
        sh = np.vstack((s_values, h_values)).T
        return sh