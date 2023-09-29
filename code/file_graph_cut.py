#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 21:33:04 2023

@author: mariachzhen
"""

import xarray as xr
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

file_path = '/Users/mariachzhen/Desktop/SF2023/Data/agg-120m-runoff-ERA5.nc'
file_new = xr.open_dataset(file_path)
file_new = file_new.to_array()
print("file_new converted to array")
file_new = file_new.values
print("file converted to numpy ndarray")

data = file_new[0,0,:,:] * 1000
plotted = np.nanpercentile(data, 95)

masked_data = np.where(data > plotted, np.nan, data)
log_data = np.log(data)

plt.imshow(masked_data, cmap='cool')
plt.colorbar(label='Runoff')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Runoff - Aggregated over 120 months - Top 5% data removed')
plt.show()

plt.imshow(log_data, cmap='cool')
plt.colorbar(label='Runoff')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Runoff - Aggregated over 120 months - Logarithm of the data')
plt.show()

plt.imshow(data, cmap='cool')
plt.colorbar(label='Runoff')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Runoff - Aggregated over 120 months - Original')
plt.show()