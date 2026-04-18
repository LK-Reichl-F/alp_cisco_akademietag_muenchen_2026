"""
Erstellt den Orange-Workshop-Workflow als .ows-Datei.
Ausführen mit:
  /home/florian/Dokumente/ALP/orange3/bin/python erstelle_workflow.py
"""

import os
from orangecanvas.scheme import Scheme, SchemeNode, SchemeLink
from orangecanvas.scheme.readwrite import scheme_to_ows_stream
from orangecanvas.registry import WidgetDescription, InputSignal, OutputSignal

# Absoluter Pfad zur CSV-Datei
BASE = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE, "Datensätze", "workshop_ids.tab")
OWS_PATH = os.path.join(BASE, "Datensätze", "workshop_workflow.ows")

# ── Scheme anlegen ────────────────────────────────────────────────────────────
scheme = Scheme(
    title="KI erkennt Netzwerkangriffe – IDS Workshop",
    description=(
        "Workshop-Workflow: CICIDS2017-Subset (BENIGN vs. DDoS). "
        "Datei laden → Daten erkunden → Entscheidungsbaum → Bewertung → Modellvergleich."
    ),
)

# ── Hilfsfunktion: WidgetDescription aus Orange-Widget-Klasse laden ───────────
import importlib

def make_desc(qualified_name):
    """Lädt die WidgetDescription direkt aus der Widget-Klasse."""
    mod_name, cls_name = qualified_name.rsplit(".", 1)
    mod = importlib.import_module(mod_name)
    cls = getattr(mod, cls_name)
    wd = cls.get_widget_description()
    inputs  = [InputSignal(c.name, c.type, c.handler,
                           flags=getattr(c, 'flags', 0),
                           id=getattr(c, 'id', c.name),
                           doc=getattr(c, 'doc', None))
               for c in wd.get('inputs', [])]
    outputs = [OutputSignal(c.name, c.type,
                            flags=getattr(c, 'flags', 0),
                            id=getattr(c, 'id', c.name),
                            doc=getattr(c, 'doc', None))
               for c in wd.get('outputs', [])]
    return WidgetDescription(
        name=wd.get('name', cls_name),
        id=qualified_name,
        qualified_name=qualified_name,
        project_name="Orange3",
        version=wd.get('version', ''),
        inputs=inputs,
        outputs=outputs,
    )

# ── Widget-Definitionen ───────────────────────────────────────────────────────
# (qualified_name, title, position)
NODES = [
    # ID 0
    ("Orange.widgets.data.owfile.OWFile",
     "Datensatz laden", (80, 300)),
    # ID 1
    ("Orange.widgets.data.owtable.OWTable",
     "Datentabelle", (280, 160)),
    # ID 2
    ("Orange.widgets.visualize.owscatterplot.OWScatterPlot",
     "Scatter Plot – Exploration", (280, 420)),
    # ID 3
    ("Orange.widgets.data.owdatasampler.OWDataSampler",
     "Train/Test-Split (70/30)", (280, 300)),
    # ID 4
    ("Orange.widgets.model.owtree.OWTreeLearner",
     "Entscheidungsbaum", (480, 300)),
    # ID 5
    ("Orange.widgets.visualize.owtreeviewer.OWTreeGraph",
     "Baum-Visualisierung", (680, 180)),
    # ID 6
    ("Orange.widgets.evaluate.owtestandscore.OWTestAndScore",
     "Test & Bewertung", (680, 380)),
    # ID 7
    ("Orange.widgets.evaluate.owconfusionmatrix.OWConfusionMatrix",
     "Confusion Matrix", (880, 380)),
    # ID 8
    ("Orange.widgets.visualize.owscatterplot.OWScatterPlot",
     "Scatter Plot – Fehler", (1080, 380)),
    # ID 9
    ("Orange.widgets.model.owrandomforest.OWRandomForest",
     "Random Forest", (480, 460)),
    # ID 10
    ("Orange.widgets.model.owknn.OWKNNLearner",
     "k-Nearest Neighbors", (480, 540)),
]

# Nodes erstellen
nodes = []
for qname, title, pos in NODES:
    node = SchemeNode(
        description=make_desc(qname),
        title=title,
        position=pos,
    )
    scheme.add_node(node)
    nodes.append(node)

# ── Verbindungen ──────────────────────────────────────────────────────────────
# (source_id, source_channel, sink_id, sink_channel)
LINKS = [
    # Daten erkunden
    (0, "Data",          1, "Data"),           # File → Datentabelle
    (0, "Data",          2, "Data"),           # File → Scatter Plot Exploration
    # Train/Test
    (0, "Data",          3, "Data"),           # File → Data Sampler
    # Entscheidungsbaum
    (3, "Data Sample",   4, "Data"),           # Data Sampler → Tree
    (4, "Model",         5, "Tree"),           # Tree → Tree Viewer
    (5, "Selected Data", 2, "Data Subset"),    # Tree Viewer → Scatter Plot (Hervorhebung)
    # Bewertung
    (0, "Data",          6, "Data"),           # File → Test & Score
    (4, "Learner",       6, "Learner"),        # Tree → Test & Score
    (9, "Learner",       6, "Learner"),        # Random Forest → Test & Score
    (10, "Learner",      6, "Learner"),        # kNN → Test & Score
    # Confusion Matrix
    (6, "Evaluation Results", 7, "Evaluation Results"),
    (7, "Selected Data", 8, "Data Subset"),    # Confusion Matrix → Scatter Plot Fehler
    (0, "Data",          8, "Data"),           # File → Scatter Plot Fehler
]

for src_id, src_ch, snk_id, snk_ch in LINKS:
    link = SchemeLink(
        source_node=nodes[src_id],
        source_channel=src_ch,
        sink_node=nodes[snk_id],
        sink_channel=snk_ch,
    )
    scheme.add_link(link)

# ── Workflow speichern ────────────────────────────────────────────────────────
with open(OWS_PATH, "wb") as f:
    scheme_to_ows_stream(scheme, f)

print(f"Workflow gespeichert: {OWS_PATH}")
print()
print("Nächste Schritte in Orange:")
print(f"  1. Workflow öffnen: {OWS_PATH}")
print(f"  2. 'Datensatz laden' doppelklicken → Datei wählen: {CSV_PATH}")
print("  3. 'Scatter Plot – Exploration': X = 'Packet Length Mean', Y = 'Down/Up Ratio', Farbe = 'Label'")
print("  4. 'Train/Test-Split': Sampling = Fixed proportion, 70% Training")
