# Data

This folder stores the spatial datasets used for the SES 230 Group Mercury analysis.

## Folder Layout

- `raw/` - original source data files used by the notebooks and scripts
- `processed/` - cleaned or generated outputs, if produced during analysis

## Expected Raw Data

The analysis uses California earthquake point data and California geologic map or rock type polygon data. Shapefiles require multiple companion files to work correctly, so keep each `.shp` file with its matching `.dbf`, `.shx`, `.prj`, `.cpg`, and other related files.

Key expected files include:

- `CA_EQ_Shallow.shp` and companion files
- `California_Rock_Types.shp` and companion files
- California geologic map source files, if using the full geologic map workflow

## Data Access Notes

Primary data sources include the USGS earthquake catalog and California Geological Survey geologic map data. If a dataset is too large to store directly in GitHub, place the data in the instructor-provided Dropbox folder and add the access link and download instructions here before final submission.

## Reproducibility Notes

Run the notebooks or `python code/analysis.py` from the repository root so relative paths resolve correctly.
