import streamlit as st


def mostra():
    # st.session_state.errore = ""

    st.header("Registrazione")

    if st.button("login"):
        st.session_state.chi_loggato = "0"
        st.rerun()
