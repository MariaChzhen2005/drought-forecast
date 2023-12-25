#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 09:38:34 2023

@author: mariachzhen
"""

import xarray as xr
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from mpl_toolkits.axes_grid1 import make_axes_locatable

plt.rc('font', size=8)


file_path = '/Users/mariachzhen/Desktop/SF2023/Data/agg-120m-surface-runoff-ERA5.nc'
file_new = xr.open_dataset(file_path)
file_new = file_new.to_array()
print("file_new converted to array")
file_new = file_new.values
print("file converted to numpy ndarray")

data = file_new[0,0,:,:]
plotted = np.nanpercentile(data, 95)

masked_data = np.where(data > plotted, np.nan, data)
log_data = np.log(data)
processed_data = np.exp(np.where(log_data == -np.inf, np.nan, log_data))

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)

plt.title("Surface runoff - 120 month aggregate")

ax1.imshow(masked_data, cmap='cool')
ax1.set_title('Top 5% data removed')
ax1.set_ylabel('Latitude')

ax2.imshow(log_data, cmap='cool')
ax2.set_title('Logarithm of the data')
ax2.set_ylabel('Latitude')

ax4.imshow(processed_data, cmap='cool')
ax4.set_title('Processed')
ax4.set_xlabel('Longitude')
ax4.set_ylabel('Latitude')

ax3.imshow(data, cmap='cool')
ax3.set_title('Original')
ax3.set_xlabel('Longitude')
ax3.set_ylabel('Latitude')



# divider = make_axes_locatable(fig)
# cax = divider.append_axes("right", size="5%", pad=0.05)
# plt.colorbar(fig, cax=cax, label="Temperature")

plt.show()