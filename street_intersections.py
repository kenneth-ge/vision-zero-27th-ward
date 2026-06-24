# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.4
#   kernelspec:
#     display_name: base
#     language: python
#     name: python3
# ---

# %%
import pandas as pd
from shapely import wkt

df = pd.read_csv("transportation_20260622.csv", dtype=str)

# Readable street name, e.g. "S YALE AVE"
parts = ["PRE_DIR", "STREET_NAM", "STREET_TYP", "SUF_DIR"]
df["name"] = df[parts].fillna("").agg(" ".join, axis=1).str.split().str.join(" ")

# First and last point of each segment. The first sits at FNODE_ID, the last at TNODE_ID.
def endpoints(geom_text):
    geom = wkt.loads(geom_text)
    if geom.is_empty:                       # 2 rows are MULTILINESTRING EMPTY
        return None, None
    coords = [pt for line in geom.geoms for pt in line.coords]
    return coords[0], coords[-1]

ends = df["the_geom"].apply(endpoints)
df["from_pt"] = ends.str[0]
df["to_pt"]   = ends.str[1]

# One row per segment END: which node, which street, and where it is.
from_ends = pd.DataFrame({"node": df["FNODE_ID"], "street": df["STREETNAME"], "name": df["name"], "pt": df["from_pt"]})
to_ends   = pd.DataFrame({"node": df["TNODE_ID"], "street": df["STREETNAME"], "name": df["name"], "pt": df["to_pt"]})
ends_long = pd.concat([from_ends, to_ends], ignore_index=True)

ends_long["lon"] = ends_long["pt"].apply(lambda p: round(p[0], 6) if p else None)
ends_long["lat"] = ends_long["pt"].apply(lambda p: round(p[1], 6) if p else None)

# For each node: how many distinct streets meet, their names, and the location.
def join_streets(names):
    return " & ".join(sorted(set(names)))

summary = ends_long.groupby("node").agg(
    num_streets=("street", "nunique"),
    streets=("name", join_streets),
    lon=("lon", "first"),
    lat=("lat", "first"),
)

# 2+ distinct streets = real intersection
intersections = summary[summary["num_streets"] >= 2]
intersections.to_csv("chicago_intersections.csv")

# %%
intersections.head()
