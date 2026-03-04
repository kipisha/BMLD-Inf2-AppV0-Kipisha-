import streanlit as st
from functions.addition import

st.title("Addition")

st.write("Hier ist mein Rechner")

with st.form("addition_form"):
    nummer_1 = st.number_input("Nummer 1")
    nummer_2 = st.number_input("Nummer 2")
    resultat = add(nummer_1,nummer_2)

    submit =st.form_submit_button("Berechnen")

    if submit:
        st.write(resultat)
