import streamlit as st


def mostra():
    if st.session_state.caricamento != "":
        st.spinner(st.session_state.caricamento)
