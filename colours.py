import json

# Load your GeoJSON file
with open("koppen.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Extract unique climate types
climate_set = set()
for feature in data["features"]:
    climate = feature["properties"].get("climate")
    if climate:
        climate_set.add(climate)

# Print sorted unique climate types
for climate in sorted(climate_set):
    print(climate)
