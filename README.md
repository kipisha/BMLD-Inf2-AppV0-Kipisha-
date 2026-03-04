# 🧫 CellCompute | Bakterien-Wachstumsrechner

## Projektbeschreibung
Dieses Projekt wurde im Rahmen des Moduls **Informatik 2 (BMLD)** an der ZHAW entwickelt. Die App bietet ein interaktives Werkzeug zur Simulation von Bakterienwachstum in der exponentiellen Phase.


* **Darlene Armenio** (armdar01@students.zhaw.ch)
* **Kipisha Selvan** (selvakip@students.zhaw.ch)


* **Interaktiver Rechner:** Eingabe von Startanzahl ($N_0$), Zeit ($t$) und Generationszeit ($g$).
* **Visualisierung:** Automatisches Balkendiagramm des Wachstumsverlaufs.
* **Labortools:** Zusätzlicher Verdünnungsrechner für die Probenvorbereitung.


* **Framework:** Streamlit (Python)
* **Struktur:** Modularer Aufbau mit `views/` für das UI und `functions/` für die Berechnungslogik.
* **Elemente:** Nutzt `st.form`, `st.metric`, `st.bar_chart`, `st.navigation` und weitere API-Features.


1. Repository klonen oder ZIP entpacken.
2. Notwendige Bibliotheken installieren:
   ```bash
   pip install streamlit pandas numpy



