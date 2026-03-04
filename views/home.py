import streamlit as st

# Titel der Startseite
st.title("CellCompute: Digitaler Bakterien-Rechner 🧫")

# CSS für das wissenschaftliche Design (Cards)
st.markdown("""
    <style>
    .author-card {
        background-color: rgba(255, 255, 255, 0.8);
        padding: 20px;
        border-radius: 12px;
        border-left: 6px solid #007bff; /* Blau für Wissenschaft */
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("### Projekt-Übersicht")
st.write("Willkommen zu unserer App für das Modul **Informatik 2 (BMLD/ZHAW)**.")

st.divider()

st.header("Autoren 👩‍🔬")
col1, col2 = st.columns(2)

with col1:
    st.markdown("""<div class="author-card">
        <strong>Autorin 1</strong><br>
        Darlene Armenio<br>
        <span style="font-size: 0.9em;">📧 armdar01@students.zhaw.ch</span>
    </div>""", unsafe_allow_html=True)

with col2:
    st.markdown("""<div class="author-card">
        <strong>Autorin 2</strong><br>
        Kipisha Selvan<br>
        <span style="font-size: 0.9em;">📧 selvakip@students.zhaw.ch</span>
    </div>""", unsafe_allow_html=True)

st.divider()
st.info("💡 **Anleitung:** Nutze das Menü links, um zum Rechner zu navigieren.")
st.caption("Entwickelt im Frühjahr 2026 | BMLD | ZHAW")
