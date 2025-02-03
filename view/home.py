import streamlit as st


def mostra():
    with st.sidebar:
        st.title("menu laterale")

        if st.button("demo"):
            st.session_state.pagina = "demo"
            st.rerun()
        
        if st.button("logout"):
            st.session_state.chi_loggato = "0"
            st.rerun()
    # st.session_state.errore = ""

    st.header("HOME")

    st.write(st.session_state.chi_loggato)

    

    if st.button("logout"):
        st.session_state.chi_loggato = "0"
        st.rerun()
        
    if st.button("demo"):
        st.session_state.pagina = "demo"
        st.rerun()
