import geopandas as gpd
import pandas as pd

from utils import ensure_output_dirs, raw_data_path


ROCK_TYPES_FILE = "California_Rock_Types.shp"
EARTHQUAKES_FILE = "CA_EQ_Shallow.shp"


def load_spatial_data():
    """Load California rock type polygons and shallow earthquake points."""
    rock_map = gpd.read_file(raw_data_path(ROCK_TYPES_FILE))
    earthquakes = gpd.read_file(raw_data_path(EARTHQUAKES_FILE))
    return rock_map, earthquakes


def count_earthquakes_by_rock_type(rock_map, earthquakes) -> pd.DataFrame:
    """Spatially join earthquakes to rock types and summarize counts."""
    earthquakes = earthquakes.to_crs(rock_map.crs)
    rock_map_clean = rock_map[["Rock_Type", "geometry"]].copy()
    joined = gpd.sjoin(earthquakes, rock_map_clean, how="inner", predicate="within")

    rock_column = "Rock_Type_right" if "Rock_Type_right" in joined.columns else "Rock_Type"
    counts = joined[rock_column].value_counts().sort_values(ascending=False)

    summary = pd.DataFrame(
        {
            "Rock Type": counts.index,
            "Count": counts.values,
            "Percentage": (counts.values / counts.sum() * 100).round(2),
        }
    )
    return summary


def run_analysis() -> pd.DataFrame:
    """Run the full earthquake and rock type analysis."""
    ensure_output_dirs()
    rock_map, earthquakes = load_spatial_data()
    return count_earthquakes_by_rock_type(rock_map, earthquakes)


if __name__ == "__main__":
    print(run_analysis().to_string(index=False))
