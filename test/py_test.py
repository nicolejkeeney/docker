# python script to test image

# A few libraries in the environment file 
import xarray as xr 
import numpy as np 
import pandas as pd
import scipy
import matplotlib.pyplot as plt
import hvplot.pandas
import hvplot.xarray

# Make a dummy xr.DataArray object 
data_np = np.arange(0,10,1)
da = xr.DataArray(data_np, coords={"x":np.arange(0,10,1)})
print("xr.DataArray: {0}".format(da))