# Code

This folder contains scripts and notebooks that support the earthquake and rock type analysis.

- `analysis.py` - reusable workflow for loading spatial data, spatially joining earthquake points to rock type polygons, and summarizing earthquake counts by rock type
- `utils.py` - shared path helpers for locating project folders
- `earthquake_count_by_rocktype.py` - analysis script for the earthquake count by rock type workflow
- `Earthquake_Count_by_RockType_Clean.ipynb` - cleaned notebook version of the rock type count analysis
- `CA_EQ_Shallow_Attribute_Analysis.ipynb` - notebook for exploring CA_EQ_Shallow earthquake attributes
- `CA_EQ_Shallow_Attribute_Analysis_original.ipynb` - original attribute analysis notebook kept for reference
- `temp_notebook.ipynb` - temporary/intermediate notebook retained for project history

Run scripts from the repository root so relative paths such as `data/raw/` work correctly.
