# python script to test imports 

import xarray as xr 
import numpy as np 
import pandas as pd
import scipy

data_np = np.arange(0,10,1)
da = xr.DataArray(data_np, coords={"x":np.arange(0,10,1)})
print("xr.DataArray: {0}".format(da))