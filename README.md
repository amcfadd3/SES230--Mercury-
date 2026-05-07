# Earthquake Location Rock Type Correlation

SES 230 Group Mercury final project repository.

Group identifier: Mercury

## Group Members and Roles

- Mackenzie Chadbourne - Coder
- Charles Lewson - Coder
- Ali McFadden - Principal Investigator
- Karlyn Porras - Literature Reviewer
- Nina Balan - Data Manager

## Research Question and Hypothesis

Research question: What rock type are shallow earthquakes most likely to occur in?

Final hypothesis: Earthquakes shallower than 100 m are more likely to occur in primarily metamorphic rock compared to regions with primarily igneous or sedimentary rock.

## Project Summary

This project investigates the relationship between shallow California earthquakes and surface rock type. The workflow uses earthquake point data and California geologic map data, performs a spatial join with GeoPandas, and counts how many earthquake epicenters fall within each mapped rock type. The final results showed that sedimentary and metasedimentary units hosted the largest share of the shallow earthquakes in the dataset, while metamorphic rock hosted the fewest, so the final hypothesis was not supported.

## Repository Structure

- `README.md` - project overview and reproduction instructions
- `LICENSE` - open-source license
- `requirements.txt` - Python dependencies
- `SES230_GroupMercury_FinalReport.ipynb` - single final report notebook containing the report text, figures, and reproducible code
- `code/` - analysis scripts and supporting notebooks
- `data/raw/` - raw spatial datasets used in the analysis
- `data/processed/` - processed outputs, if generated
- `figures/` - maps, charts, screenshots, and report figures
- `docs/` - additional notes, AI use log, reproducibility checklist, and contribution statement
- `zotero/` - exported Zotero library files

## Installing Dependencies

Install the Python packages with:

```bash
pip install -r requirements.txt
```

The project uses Python with GeoPandas, pandas, NumPy, Matplotlib, Seaborn, and Shapely. Jupyter is included so the notebooks can be opened and run locally.

## Running the Notebook

1. Clone or download this repository.
2. Install the dependencies listed in `requirements.txt`.
3. Confirm that the required data files are available under `data/raw/`.
4. Open `SES230_GroupMercury_FinalReport.ipynb`.
5. Run the notebook cells from top to bottom.

The main reusable Python workflow can also be run with:

```bash
python code/analysis.py
```

## Data Access

The repository includes the project data under `data/raw/` when file size allows. The analysis expects California earthquake and geologic map shapefile components, including `.shp`, `.dbf`, `.shx`, `.prj`, and related companion files.

Primary data sources include:

- USGS earthquake catalog data
- California Geological Survey geologic map data

See `data/README.md` for more detail about expected raw data files and organization.

## Zotero Library

The exported Zotero library is stored in `zotero/Zotero_Library_SES230.ris`. Additional bibliography placeholders or exports may also be present in the `zotero/` folder.
