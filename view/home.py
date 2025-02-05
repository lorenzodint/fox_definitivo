import streamlit as st
import utils.functions as func
from streamlit.components.v1 import html
import streamlit_shadcn_ui as ui


def mostra():
    # trigger_button = ui.button(text="pulsante", key="trigger")

    # if trigger_button:
    #     st.write("ho premuto")

    # ui.alert_dialog(
    #     show=trigger_button,
    #     title="Alert dialog",
    #     description="questo è un alert dialog",
    #     confirm_label="OK",
    #     cancel_label="Annulla",
    #     key="alert_dialog_1"
    # )

    with st.container(border=True):

        cols = st.columns(2)

        with cols[0]:

            st.write(
                f'''<h1 class="" style="">Rivoluziona la gestione degli ordini con l'<span style="color: #0000ff">AI</span></h1>''',
                unsafe_allow_html=True
            )

            st.write(
                f'''<h4>Trasforma ordini cartacei, email, PDF in <span style="color: #ff8b03;">dati strutturati</span> pronti all'uso</h4>''',
                unsafe_allow_html=True
            )

            if ui.button(text="Provalo ora"):
                pass

    st.divider()

    if ui.button("Login", key="pulsante_vai_login"):
        st.session_state.chi_loggato = "-2"
        st.rerun()
