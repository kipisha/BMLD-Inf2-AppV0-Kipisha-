import streamlit as st
import pandas as pd
import plotly.express as px
from functions.calculations import calculate_bacterial_growth, get_growth_steps

# 1. Datenbank definieren
data = {
    "Organismus": [
        "Escherichia coli", "Bacillus subtilis", "Staphylococcus aureus", 
        "Salmonella enterica", "Vibrio cholerae", "Pseudomonas aeruginosa",
        "Listeria monocytogenes", "Mycobacterium tuberculosis", "Treponema pallidum",
        "Clostridium perfringens", "Streptococcus pyogenes", "Campylobacter jejuni"
    ],
    "Generationszeit_min": [20, 26, 28, 25, 13, 45, 40, 720, 1980, 10, 40, 90],
    "Kategorie": ["Darm", "Labor", "Krankenhaus", "Lebensmittel", "Wasser", "Wunde", "Kühlkette", "Lunge", "STD", "Wundinfekt", "Hals", "Darm"]
}
df_bakterien = pd.DataFrame(data)

st.title("Mikrobieller-Rechner 🦠")

st.markdown("""
Wähle einen Organismus aus der Datenbank aus. Die **Generationszeit ($g$)** wird 
automatisch für die Berechnung übernommen.
""")

# 2. Auswahl & Parameter (in einer "App"-Sidebar oder oben)
st.subheader("Bakterien-Katalog")
selected_organism = st.selectbox("Suche in der Datenbank:", df_bakterien["Organismus"])

# Daten aus Liste holen
row = df_bakterien[df_bakterien["Organismus"] == selected_organism].iloc[0]
g_aus_liste = row["Generationszeit_min"]
kategorie = row["Kategorie"]

# Eingabe-Bereich in einem schicken Container
with st.container(border=True):
    col1, col2, col3 = st.columns(3)
    with col1:
        n0 = st.number_input("Startanzahl ($N_0$)", value=100)
    with col2:
        t = st.number_input("Zeit ($t$ in min)", value=180)
    with col3:
        # Erlaubt Anpassung, falls man vom Standard abweichen will
        g = st.number_input(f"$g$ für {selected_organism}", value=int(g_aus_liste))

# 3. Berechnung & Dashboard-Elemente
nt, n_gen = calculate_bacterial_growth(n0, t, g)
times, counts = get_growth_steps(n0, t, g)

# Metriken anzeigen
st.divider()
m1, m2, m3 = st.columns(3)
m1.metric("Endanzahl", f"{int(nt):,}")
m2.metric("Generationen", f"{round(n_gen, 1)}")
m3.metric("Kategorie", kategorie)

# 4. Visualisierung mit Plotly (für richtige Achsen)
chart_df = pd.DataFrame({"Zeit (min)": times, "Anzahl Bakterien": counts})

fig = px.area(chart_df, x="Zeit (min)", y="Anzahl Bakterien", 
              title=f"Wachstumsverlauf: {selected_organism}",
              color_discrete_sequence=['#FF4B4B']) # Rötlich für Krankheitserreger

fig.update_layout(
    xaxis_title="Zeit in Minuten",
    yaxis_title="Gesamtanzahl Zellen",
    hovermode="x unified"
)

st.plotly_chart(fig, use_container_width=True)

# 5. Zusätzliche Info-Card
st.info(f"🧬 **Info:** *{selected_organism}* gehört zur Kategorie **{kategorie}**. "
        f"Bei einer Generationszeit von {g} Minuten verdoppelt sich die Population "
        f"ca. {round(60/g, 1)} mal pro Stunde.")
