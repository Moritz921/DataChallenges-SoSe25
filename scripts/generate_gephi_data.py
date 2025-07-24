import pandas as pd
import geopy
import time
import tqdm
from itertools import combinations
from collections import defaultdict, Counter

# --- Parameter ---
input_file = "muenzdaten-new.csv"  # Passe den Dateinamen an
delimiter = ";"                # CSV-Trennzeichen
typ_key = "Typ"  # Spalte für den Typ
findspot_key = "Findspot_1"  # Spalte für den Fundort

# --- CSV einlesen ---
df = pd.read_csv(input_file, delimiter=delimiter)

# Nur die Spalten, die wir brauchen
df = df[[typ_key, findspot_key]].dropna()

# Dictionary: typ -> set of findspots (Mehrfache Fundorte bleiben erhalten)
type_to_spots = defaultdict(list)

type_to_spot_counts = defaultdict(Counter)
for _, row in df.iterrows():
    typ = row[typ_key]
    spot = row[findspot_key]
    type_to_spots[typ].append(spot)
    type_to_spot_counts[typ][spot] += 1

# --- Kanten berechnen ---
edge_weights = defaultdict(int)
edge_types = defaultdict(list)  # speichert Typen pro Kante

# print(type_to_spot_counts)

edges = []
for typ, spot_counts in type_to_spot_counts.items():
    spots = list(spot_counts.keys())
    for a, b in combinations(spots, 2):
        if a != b:
            weight = min(spot_counts[a], spot_counts[b])  # Gewicht als Minimum der Vorkommen
            if weight > 0:
                edges.append({
                    "Source": a,
                    "Target": b,
                    "Types": typ,
                    "Weight": weight
                })

for i, (i_index, i_row) in tqdm.tqdm(enumerate(df.iterrows()), total=len(df), desc="Berechne Kanten"):
    i_typ = i_row[typ_key]
    i_spot = i_row[findspot_key]
    for _, j_row in df.iloc[i + 1:].iterrows():
        j_typ = j_row[typ_key]
        j_spot = j_row[findspot_key]
        if i_spot != j_spot and i_typ == j_typ:
            # same type and different spots

            # check if edge already exists
            not_exists = True
            for edge in edges:
                if (edge['Source'] == i_spot and edge['Target'] == j_spot and edge["Type"] == i_typ) or \
                   (edge['Source'] == j_spot and edge['Target'] == i_spot and edge["Type"] == i_typ):
                    edge['Weight'] += 1
                    not_exists = False
                    break

            if not_exists:
                edges.append({
                    "Source": i_spot,
                    "Target": j_spot,
                    "Type": i_typ,
                    "Weight": 1
                })

# --- Knotenliste erstellen ---
all_nodes = set(df['Findspot_1'].dropna())

geolocator = geopy.Nominatim(user_agent="geo_finder")

coordinates = []

for node in tqdm.tqdm(all_nodes):
    try:
        location = geolocator.geocode(node, timeout=10)
        if location:
            coordinates.append({
                "Id": node,
                "Label": node,
                "Latitude": location.latitude,
                "Longitude": location.longitude
            })
        else:
            print(f"Warnung: Keine Koordinaten für {node} gefunden.")
            coordinates.append({
                "Id": node,
                "Label": node,
                "Latitude": None,
                "Longitude": None
            })
    except Exception as e:
        print(f"Fehler bei der Geokodierung von {node}: {e}")
    time.sleep(1.2)

nodes_df = pd.DataFrame(coordinates)
nodes_df.to_csv("nodes_geo.csv", sep=";", index=False)

# --- Kantenliste erstellen ---
edges_df = pd.DataFrame(edges)
print(edges_df)
edges_df.to_csv("edges.csv", sep=";", index=False)

print("Fertig: nodes.csv und edges.csv wurden erstellt.")
