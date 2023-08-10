import xarray as xr
from netCDF4 import Dataset as nc
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

file = xr.open_dataset("/Users/mariachzhen/Downloads/surface-runoff.nc")

latitude_values = list(file.latitude)
longitude_values = list(file.longitude)

latitude_values = list(np.array(latitude_values, dtype=np.float32))
longitude_values = list(np.array(longitude_values, dtype=np.float32))

data = file['sro']

aggs = [3, 6, 12, 36, 60, 120]
for agg in aggs:
    print(agg)
    list_agg = []
    time = 0
    for i in range(0, 420-agg):
        sum_over_window = np.nansum(data[i:i+agg, 0, :, :], axis=0)
        sum_over_window = np.where(sum_over_window == 0, np.nan, sum_over_window)
        list_agg.append(sum_over_window)
        time+=1
        
    time_values = list(range(0, time))
    
    print(np.shape(list_agg), len(latitude_values), len(longitude_values))
    
    
    data_array = xr.DataArray(list_agg, coords=[time_values, latitude_values, longitude_values], dims=['time', 'latitude', 'longitude'])
    dataset = xr.Dataset({'data_variable': data_array})
    file_path = '/Users/mariachzhen/Desktop/SF2023/Data/agg-'+str(agg)+'m-surface-runoff-ERA5.nc'
    dataset.to_netcdf(file_path)
