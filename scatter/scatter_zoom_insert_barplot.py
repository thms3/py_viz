#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Project:        Python vizualisation plot
Description:    Scatter plot example with zoom insertion associated with barplot
Author:         Thomas Neff
Date:           2024-10-17 17:02:40
"""

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib import cm
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

# Generate random data for the cloud of points
np.random.seed(0)  # For reproducibility
x_cloud = np.random.rand(100) * 10  # 100 random x-coordinates
y_cloud = np.random.rand(100) * 10  # 100 random y-coordinates

# Create a DataFrame for the cloud of points
cloud_df = pd.DataFrame({'x': x_cloud, 'y': y_cloud})

# Define a center point to calculate distance for color mapping
center_point = {'x': 5, 'y': 7}

# Calculate the distance from the center point for each point in the cloud
cloud_df['distance'] = np.sqrt((cloud_df['x'] - center_point['x']) ** 2 +
                                (cloud_df['y'] - center_point['y']) ** 2)

# Normalize the distance for color mapping
cloud_df['norm_distance'] = (cloud_df['distance'] - cloud_df['distance'].min()) / (cloud_df['distance'].max() - cloud_df['distance'].min())

# Create a color map based on normalized distance using Viridis
norm = plt.Normalize(cloud_df['norm_distance'].min(), cloud_df['norm_distance'].max())
colors = cm.viridis(norm(cloud_df['norm_distance']))

# Create a main scatterplot with a fixed size and color map
fig, ax = plt.subplots(figsize=(10, 8))
scatter = ax.scatter(cloud_df['x'], cloud_df['y'], c=colors, s=10, alpha=0.8)

# Add title and labels
ax.set_title("Scatterplot with Viridis Color Temperature Scale")
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")

# Add a color bar
cbar = plt.colorbar(cm.ScalarMappable(norm=norm, cmap='viridis'), ax=ax)
cbar.set_label('Normalized Distance', rotation=270, labelpad=15)  # Label for color bar
cbar.ax.invert_yaxis()  # Invert the color bar to match the color scheme

# Set the axis limits
#ax.set_xlim(0, 10)  # Set x-axis limit
#ax.set_ylim(0, 10)  # Set y-axis limit
ax.grid(True)       # Optional: Add grid for better visibility

# Create an inset for zooming in
# Define the limits for the inset (zoomed area)
x1, x2, y1, y2 = 4, 6, 5, 7  # Set the region to zoom into

# Create inset axes
ax_inset = inset_axes(ax, width="30%", height="30%", loc='upper right')  # Adjust width and height as needed
ax_inset.scatter(cloud_df['x'], cloud_df['y'], c=colors, s=10, alpha=0.8)
ax_inset.set_xlim(x1, x2)
ax_inset.set_ylim(y1, y2)

# Optional: Add a rectangle to indicate the zoomed area in the main plot
rect = plt.Rectangle((x1, y1), x2-x1, y2-y1, linewidth=1, edgecolor='red', facecolor='none')
ax.add_patch(rect)

# Show the plot
plt.show()
