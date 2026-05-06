# Reproducibility Checklist

- [x] Repository contains a `README.md` with project overview and instructions
- [x] Repository contains an open-source `LICENSE`
- [x] Repository contains `requirements.txt`
- [x] Raw data are organized under `data/raw/`
- [x] Processed data folder exists at `data/processed/`
- [x] Zotero export is included under `zotero/`
- [x] Final report is included as Markdown
- [x] Figures used in the report are stored under `figures/`
- [x] Code and supporting notebooks are stored under `code/`
- [ ] Notebook has been run from start to finish on a clean machine
- [ ] All external data access links have been confirmed, if any required files are too large for GitHub

To reproduce, install dependencies with `pip install -r requirements.txt`, verify the raw data are present in `data/raw/`, then run the notebook or `python code/analysis.py` from the repository root.
