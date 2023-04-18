# # Geoprocessing with GeoPanda vice PyQGIS
#
# 1. Import the raw potential explosion site (PES) layer data.
# 2. Read the PES data into a GeoDataframe.
# 3. Calculate the QDs and add them as new columns in the GeoDataframe.
# 4. Create buffer geometry columns for each QD based on the respective calculated QD.
# 5. Create new GeoDataframes for each QD buffer with the geometry of the respective QD buffer.
# 6. Export the GeoDataframes to layers within a single output Geopackage file.
# 7. Import the Geopackage output file into QGIS.

# geopandas setup for google colab
# try:
#     import geopandas
# except ModuleNotFoundError:
#     if 'google.colab' in str(get_ipython()):
#         !apt install libspatialindex-dev -qq
#         !pip install fiona shapely pyproj rtree --quiet
#         !pip install geopandas --quiet
#     else:
#         print('geopandas not found, please install via conda in your environment')

import os
import pandas as pd
import geopandas as gpd
import numpy as np
import matplotlib.pyplot as plt
import sys
# import QD calc (make sure qdcalc in in your path)
sys.path.append("/Users/josh/github/qdmap/qdmap/")
# Import the file with all of the QD functions already defined.
import qdcalc as qd


data_folder = 'data'
output_folder = 'output'

if not os.path.exists(data_folder):
    os.mkdir(data_folder)
if not os.path.exists(output_folder):
    os.mkdir(output_folder)

# TODO automate the export of a selected layer to a .gpkg file called 'pes_initial_data'
input_file = 'pes_initial_data.gpkg'
input_path = os.path.join(data_folder, input_file)
pes_gdf = gpd.read_file(input_path)

# Visualize the layer

fig, ax = plt.subplots(1, 1)
fig.set_size_inches(15,7)
pes_gdf.plot(ax=ax, color='red', alpha=0.5)

minx, miny, maxx, maxy = pes_gdf.total_bounds
ax.set_xlim(minx, maxx)
ax.set_ylim(miny, maxy)

legend_elements = [
    plt.plot([],[], color='red', alpha=0.5, label='Potential Explosion Sites', ls='')[0]]
ax.legend()
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
plt.show()

# Check the CRS of the GDF. (Make sure we are in a projected CRS so that we can perform the buffer operation, otherwise we need to reproject into one first.)
pes_gdf.crs

# Geodataframe analysis
# Apply the BD1 QD function to the net explosive quantity (NEQ) of HD 1.1 field/column.
pes_gdf['hd_1_1_bd_1'] = pes_gdf.neq_1_1.apply(qd.bd1)
# Round the column down to 2 decimal places.
pes_gdf = pes_gdf.round({'hd_1_1_bd_1': 2})

# Add the other functions.
pes_gdf['hd_1_1_bd_2'] = pes_gdf.neq_1_1.apply(qd.bd2)
pes_gdf['hd_1_1_bd_3'] = pes_gdf.neq_1_1.apply(qd.bd3)

pes_gdf = pes_gdf.round({'hd_1_1_bd_2': 2, 'hd_1_1_bd_3': 2})
pes_gdf.head()

# Automate this by looping through a list of functions.

# functions = [qd.bd1(), qd.bd2(), qd.bd3()]

# for function in functions:
#     pes_gdf["hd_1_1" + str(function)] = pes_gdf.neq_1_1.apply(function)

# create buffer geometry GeoSeries based on newly computed QDs
qd_functions = {
    'hd_1_1_bd_1': pes_gdf.hd_1_1_bd_1,
    'hd_1_1_bd_2': pes_gdf.hd_1_1_bd_2,
    'hd_1_1_bd_3': pes_gdf.hd_1_1_bd_3}

# Add the GeoSeries to the geodataframe with a loop
for qd_type, distance in qd_functions.items():
    buffer_name = qd_type + '_buff_geom'
    pes_gdf[buffer_name] = pes_gdf.buffer(
        distance,
        resolution=40,
        cap_style=1,
        join_style=1,
        mitre_limit=2)

qd_functions.keys()


# %%
# pes_gdf.head()

# %%
ax = pes_gdf["geometry"].plot()
pes_gdf["hd_1_1_bd_1_buff_geom"].plot(ax=ax, color="red", alpha=0.5)
pes_gdf["hd_1_1_bd_2_buff_geom"].plot(ax=ax, color="purple", alpha=0.5)


# %%
output_file = 'processed_data.gpkg'
output_path = os.path.join(output_folder, output_file)


# Example code from https://gis.stackexchange.com/questions/375577/how-do-i-write-out-a-mixed-geometry-geodataframe-to-a-geopackage
# *** How to export a GDF with multiple geometries to separate layers in the same geopackage file.

# for geomtype in pes_gdf.geom_type.unique():
#    pes_gdf[pes_gdf.geom_type == geomtype].to_file(output_path, driver="GPKG", layer=geomtype)

pes_gdf.geometry

qd_functions.keys()

# Make a list of the new buffered geometries
qd_function_key_list = list(qd_functions.keys())
string_suffix = '_buff_geom'
buffer_geometries = [x + string_suffix for x in qd_function_key_list]

# Create a dictionary so I can grab both values for exporting
qd_buffer_dict = dict(zip(buffer_geometries, qd_function_key_list))
# print(qd_buffer_dict)

# %%
# I need more than just the geometry.
# To select multiple columns, use a list of column names within the selection brackets [].

for buffer_geometry in buffer_geometries:
   pes_gdf[buffer_geometry].to_file(output_path, driver="GPKG", layer=buffer_geometry)

# %%



