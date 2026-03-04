import streamlit as st
import pandas as pd

from functions.calculations import calculate_bacterial_growth, get_growth_steps


st.title("🧫 Bakterien-Rechner")

st.info("""
**🔬 Biologisches Prinzip:**  
Dieses Tool nutzt das Modell des exponentiellen Wachstums: $N_t = N_0 \cdot 2^{(t/g)}$. 
Stelle sicher, dass Zeit ($t$) und Generationszeit ($g$) in der **gleichen Einheit** (hier: Minuten) angegeben werden.
""")

with st.expander("❓ Hilfe zur Eingabe & Beispiele"):
    st.write("""
    Hier sind einige Richtwerte für die **Generationszeit (g)** bei 37°C:
    *   **E. coli:** 20 Minuten
    *   **B. subtilis:** 26 Minuten
    *   **S. aureus:** 30 Minuten
    
    *Hinweis: Wenn die Temperatur sinkt, erhöht sich die Generationszeit massiv!*
    """)



with st.form("my_form"):
        n0 = st.number_input("Startanzahl", value=100)
        t = st.number_input("Zeit (min)", value=120)
        g = st.number_input("Generationszeit (min)", value=20)
        submit = st.form_submit_button("Rechnen")

        
if submit:

            nt, n_gen = calculate_bacterial_growth(n0, t, g)
        
            st.metric("Ergebnis", f"{int(nt)} Bakterien")
        
            times, counts = get_growth_steps(n0, t, g)
            df = pd.DataFrame({"Zeit": times, "Anzahl": counts})
            st.bar_chart(df.set_index("Zeit"))


