import streamlit as st
import pandas as pd

from functions.calculations import calculate_bacterial_growth, get_growth_steps

def show():
    st.title("🧫 Bakterien-Rechner")

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


