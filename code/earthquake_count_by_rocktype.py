"""Earthquake count by rock type analysis.

Run from the repository root with:

    python code/earthquake_count_by_rocktype.py
"""

from pathlib import Path

import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd


def find_project_root(start: Path | None = None) -> Path:
    """Find the repository root by locating the data/raw folder."""
    start = Path.cwd().resolve() if start is None else start.resolve()
    for path in [start, *start.parents]:
        if (path / "data" / "raw").exists():
            return path
    raise FileNotFoundError("Could not find a project root containing data/raw.")


PROJECT_ROOT = find_project_root()
RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"
FIGURES_DIR = PROJECT_ROOT / "figures"
FIGURES_DIR.mkdir(exist_ok=True)

ROCK_TYPES_PATH = RAW_DATA_DIR / "California_Rock_Types.shp"
EARTHQUAKES_PATH = RAW_DATA_DIR / "CA_EQ_Shallow.shp"


def main() -> None:
    rock_map = gpd.read_file(ROCK_TYPES_PATH)
    quakes = gpd.read_file(EARTHQUAKES_PATH)

    print("Shapefiles loaded successfully.")
    print(f"Rock type polygons: {len(rock_map):,}")
    print(f"Earthquake points: {len(quakes):,}")

    quakes = quakes.to_crs(rock_map.crs)
    rock_map_clean = rock_map[["Rock_Type", "geometry"]].copy()
    joined = gpd.sjoin(quakes, rock_map_clean, how="inner", predicate="within")

    rock_column = "Rock_Type_right" if "Rock_Type_right" in joined.columns else "Rock_Type"
    counts = joined[rock_column].value_counts().sort_values(ascending=False)

    summary = pd.DataFrame(
        {
            "Rock Type": counts.index,
            "Count": counts.values,
            "Percentage": (counts.values / counts.sum() * 100).round(2),
        }
    )

    print("\nEarthquake Count by Rock Type")
    print("=" * 50)
    print(summary.to_string(index=False))
    print("=" * 50)
    print(f"Total earthquakes in input shapefile: {len(quakes):,}")
    print(f"Earthquakes matched to rock types: {len(joined):,}")

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(summary["Rock Type"], summary["Count"], color="#4c78a8", edgecolor="black")
    ax.set_title("Earthquake Count by Rock Type")
    ax.set_xlabel("Rock Type")
    ax.set_ylabel("Earthquake Count")
    ax.tick_params(axis="x", rotation=35)
    ax.grid(axis="y", alpha=0.3)
    plt.tight_layout()

    output_path = FIGURES_DIR / "earthquake_count_by_rock_type.png"
    plt.savefig(output_path, dpi=300, bbox_inches="tight")
    print(f"Saved figure to {output_path.relative_to(PROJECT_ROOT)}")


if __name__ == "__main__":
    main()
