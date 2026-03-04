import streamlit as st


st.title("CellCompute: Digitaler Bakterien-Rechner 🧫")

st.markdown("""
### Projekt-Übersicht
Willkommen zu unserer App für das Modul **Informatik 2 (BMLD/ZHAW)**. 
Diese Anwendung simuliert das **exponentielle Wachstum** von Bakterienkulturen 
basierend auf wissenschaftlichen Parametern.
""")

st.divider()


st.header("Autoren 👩‍🔬")


col1, col2 = st.columns(2)

with col1:
    with st.container(border=True):
        st.subheader("Darlene Armenio")
        st.write("📧 armdar01@students.zhaw.ch")
        st.caption("BMLD | ZHAW")

with col2:
    with st.container(border=True):
        st.subheader("Kipisha Selvan")
        st.write("📧 selvakip@students.zhaw.ch")
        st.caption("BMLD | ZHAW")

st.divider()


st.info("💡 **Anleitung:** Nutze das Menü auf der linken Seite, um zum **Bakterien-Rechner** zu navigieren.")


st.caption("© 2026 | Fachbereich Informatik 2 | ZHAW Life Sciences")
