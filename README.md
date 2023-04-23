# qdmap


[![image](https://img.shields.io/pypi/v/qdmap.svg)](https://pypi.python.org/pypi/qdmap)
[![image](https://github.com/josh-spatial/qdmap/workflows/build/badge.svg)](https://github.com/josh-spatial/qdmap/actions?query=workflow%3Abuild)

**A python package for explosives safety quantity-distance spatial analysis.**

-   Free software: MIT license
-   Documentation: https://josh-spatial.github.io/qdmap


## Features

- **IN-PROGRESS** Create a basic quantity-distance calculator
    - **DONE** Finish adding all AASTP-1 Blast Distance equations to qdcalc.py
    - **TODO** Finish adding all Debris and Fragment, Progressive, and Thermal Distance equations to qdcalc.py
- **IN-PROGRESS** Write spatial analysis (GeoPandas)

- TODO Create QGIS Plugin
    - TODO Determine database type to use as a basis (PostGIS, GeoPackage, shapefiles?)
        - Currently I'm using GeoPackage files.
    - TODO Create UI for plugin

## Credits

This package was created with [Cookiecutter](https://github.com/cookiecutter/cookiecutter) and the [giswqs/pypackage](https://github.com/giswqs/pypackage) project template.
