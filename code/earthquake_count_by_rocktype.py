# Earthquake Count by Rock Type Analysis
# This script performs spatial analysis of earthquakes by rock type

import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Define the base path
base_path = r"c:\Earthquake_correlation_shapefiles"

# Load the shapefiles
rock_map = gpd.read_file(os.path.join(base_path, "California_Rock_Types.shp"))
quakes = gpd.read_file(os.path.join(base_path, "CA_EQ_Shallow.shp"))

print("Shapefiles loaded successfully!")
print(f"Rock Types shapefile: {len(rock_map)} polygons")
print(f"CA_EQ_Shallow shapefile: {len(quakes)} earthquakes")

# Ensure both shapefiles have the same CRS
quakes = quakes.to_crs(rock_map.crs)

print(f"\nCRS synchronized: {quakes.crs}")

# Perform spatial join - find which rock type each earthquake is within
joined = gpd.sjoin(quakes, rock_map, how="inner", predicate="within")

print(f"\nTotal earthquakes matched to rock types: {len(joined)}")

# Count earthquakes by rock type
counts = joined["Rock_Type"].value_counts()

print("\nEarthquake Count by Rock Type:")
print("=" * 50)
print(counts)
print("=" * 50)

# Create a DataFrame for better visualization
counts_df = pd.DataFrame({
    'Rock_Type': counts.index,
    'Count': counts.values,
    'Percentage': (counts.values / counts.sum() * 100).round(2)
})

print("\nDetailed Statistics:")
print(counts_df.to_string(index=False))

# Create visualizations
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Bar chart
axes[0].bar(counts_df['Rock_Type'], counts_df['Count'], color='steelblue', alpha=0.7, edgecolor='black')
axes[0].set_xlabel('Rock Type', fontsize=12, fontweight='bold')
axes[0].set_ylabel('Earthquake Count', fontsize=12, fontweight='bold')
axes[0].set_title('Earthquake Count by Rock Type', fontsize=14, fontweight='bold')
axes[0].tick_params(axis='x', rotation=45)
axes[0].grid(True, alpha=0.3, axis='y')

# Pie chart
colors = plt.cm.Set3(range(len(counts_df)))
axes[1].pie(counts_df['Count'], labels=counts_df['Rock_Type'], autopct='%1.1f%%', 
            colors=colors, startangle=90)
axes[1].set_title('Earthquake Distribution by Rock Type', fontsize=14, fontweight='bold')

plt.tight_layout()
plt.savefig(os.path.join(base_path, "Code", "Earthquake_Count_by_Rock_Type.png"), dpi=300, bbox_inches='tight')
plt.show()

print("\nVisualization saved as 'Earthquake_Count_by_Rock_Type.png'")

# Additional analysis: Summary statistics
print("\n" + "=" * 50)
print("SUMMARY STATISTICS")
print("=" * 50)
print(f"Total earthquakes: {len(quakes)}")
print(f"Earthquakes in mapped rock types: {len(joined)}")
print(f"Earthquakes not in mapped areas: {len(quakes) - len(joined)}")
print(f"Coverage: {(len(joined) / len(quakes) * 100):.2f}%")
print(f"\nMost common rock type: {counts_df.iloc[0]['Rock_Type']} ({counts_df.iloc[0]['Count']} earthquakes)")
print(f"Least common rock type: {counts_df.iloc[-1]['Rock_Type']} ({counts_df.iloc[-1]['Count']} earthquakes)")
