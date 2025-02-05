import streamlit as st


def mostra():
    st.json(st.session_state.risultato)

    if st.button("Analizza altro documento"):
        st.session_state.pagina = "demo"
        st.rerun()
    if st.button("Login"):
        st.session_state.chi_loggato = "-2"
        st.rerun()
