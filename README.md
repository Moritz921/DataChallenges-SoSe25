# Data Challanges - SoSe 2025: Social Network Analysis

Dieses Repository enthält die Ergebnisse unserer Arbeit im Rahmen des Kurses Data Challanges im Sommersemester 2025 an der Goethe-Universität Frankfurt.

## Strukutur des Repositorys

Im Ordner `data` befinden sich alle von uns bereinigten Daten im `.csv`-Format. Die Dateien mit der Endung `_cde.csv`
beinhalten ausschließlich diejeningen Knoten/Kanten, die mit den Typen C, D oder E verbunden sind. Die Datien mit der
Endung `_ost.csv` beinhalten nur diejenigen Knoten/Kanten, die den östlichen Fundorten zuzuordnen sind. Analog dazu
die Dateien mit der Endung `_west.csv`. Die Datei `nodes_geo.csv` beinhaltet zusätzlich zu den gegebenen Informationen
der Fundorte die Koordinaten der Ortschaften, sodass diese im weiteren Verlauf auf einer Karte dargestellt werden können.

Im Ordner `gephi` befinden sich die Projekt-Dateien von Gephi.

Im Ordner `out` befinden sich nach den Datensätzen geordnet die Bilder und Grafiken, welche wir aus Gephi und Orange
erzeugt haben.

Im Ordner `praesentationen` befinden sich die Präsentations-Dateien sowohl der Zwischenpräsentation als auch der
Abschlusspräsentation.

Im Ordner `scripts` befinden sich die Code-Dateien, die wir zur bereinigung und erweiterung der Daten verwendet haben.

### Skripte

Die Dateien `Daten_bereinigen.ipynb` und `clean_csv.py` enthalten die Skripte, die wir zur Bereinigung der Daten verwendet haben. Die Datei `generate_gephi_data.py` verwendet zusätzlich ein Python-Paket zur Geolokalisierung, um die Koordinaten der Fundorte zu ermitteln. Die dadurch generierten Koordinaten mussten jedoch manuell überprüft und gegebenenfalls korrigiert werden. Die Datei `Gefilterte_Datensätze_erstellen.ipynb` erstellt Untermengen des ursprünglichen Datensatzes, sodass die Nordost/Südwest-Gruppen gertrennt betrachtet werden können, sowie die Daten auf die Typen C, D und E reduziert werden können.

## Farbgebung

Um eine einheitliche Farbgebung zu gewährleisten, haben wir uns für die folgenden Farben entschieden:

### Knoten

- Rot: #b3062c
- Grün: #737c45
- Lachs: #FFD9CC

### Kanten

- A: #e81e63
- B: #9c27b0
- C: #ff5722
- D: #00bcd4
- E: #3f51b5
- F: #959595
- G: #009688
- H: #ff9800
- Prototype: #ffeb3b

Zur besseren Darstellung auf der Karte wurden die Kanten wie folgt angepasst:

- Min-Thickness: 0.2
- Max-Thickness: 1
- Transparency: 75%
