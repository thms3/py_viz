#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Project:        Python vizualisation plot
Description:    Scatter plot example with zoom plot in addition
                associated with barplot
Author:         Thomas Neff
Date:           2024-10-17 17:04:50
"""

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib import cm

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

# Create a figure with two subplots
fig, (ax_main, ax_zoomed) = plt.subplots(1, 2, figsize=(14, 6))

# ---- Main Scatterplot ----
scatter = ax_main.scatter(cloud_df['x'], cloud_df['y'], c=colors, s=10, alpha=0.8)

# Add title and labels
ax_main.set_title("Main Scatterplot with Viridis Color Temperature Scale")
ax_main.set_xlabel("X Axis")
ax_main.set_ylabel("Y Axis")

# Add a color bar to the main plot
cbar = plt.colorbar(cm.ScalarMappable(norm=norm, cmap='viridis'), ax=ax_main)
cbar.set_label('Normalized Distance', rotation=270, labelpad=15)  # Label for color bar
cbar.ax.invert_yaxis()  # Invert the color bar to match the color scheme

# Set axis limits for the main plot (optional)
#ax_main.set_xlim(0, 10)
#ax_main.set_ylim(0, 10)
ax_main.grid(True)  # Optional: Add grid

# ---- Zoomed Scatterplot ----
# Define the zoomed-in area limits
x1, x2, y1, y2 = 4, 6, 5, 7  # Set the region to zoom into

# Create a second scatter plot for the zoomed-in region
ax_zoomed.scatter(cloud_df['x'], cloud_df['y'], c=colors, s=10, alpha=0.8)
ax_zoomed.set_xlim(x1, x2)
ax_zoomed.set_ylim(y1, y2)

# Add a title to the zoomed-in plot
ax_zoomed.set_title("Zoomed-In Scatterplot")
ax_zoomed.set_xlabel("X Axis (Zoomed)")
ax_zoomed.set_ylabel("Y Axis (Zoomed)")

# Optional: Highlight the zoomed area on the main plot
rect = plt.Rectangle((x1, y1), x2 - x1, y2 - y1, linewidth=1, edgecolor='red', facecolor='none')
ax_main.add_patch(rect)

# Show the plots
plt.tight_layout()  # Adjust layout to prevent overlapping elements
plt.show()
