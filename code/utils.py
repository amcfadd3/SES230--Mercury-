from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"
PROCESSED_DATA_DIR = PROJECT_ROOT / "data" / "processed"
FIGURES_DIR = PROJECT_ROOT / "figures"


def ensure_output_dirs() -> None:
    """Create output folders used by the analysis."""
    PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)


def raw_data_path(filename: str) -> Path:
    """Return the path for a file expected in data/raw."""
    return RAW_DATA_DIR / filename
