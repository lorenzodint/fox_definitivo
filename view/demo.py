import streamlit as st
import requests
from PIL import Image
import io
import os
import time
import uuid
import base64


def display_pdf(file):
    with open(file, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')

        pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height:"auto" type="application/pdf"></iframe>'

        st.write(pdf_display, unsafe_allow_html=True)


def mostra():
    with st.container(border=True):
        with st.sidebar:
            st.title("menu laterale")

            if st.button("logout"):
                st.session_state.chi_loggato = "0"
                st.rerun()

    c1, c2, c3 = st.columns([1, 4, 1])
    with c2:
        with st.container():

            # st.write("Carica un documento, oppure")

            t1, t2 = st.tabs(['PDF', 'Fotocamera'])

            with t1:
                caricafile = st.file_uploader(
                    label="Carica documento:", type=['pdf', 'PDF'])
                if caricafile is not None:
                    # bytes_data = caricafile.read()
                    # st.write("nome file:", caricafile.name)
                    # st.write(bytes_data)
                    st.divider()
                    # display_pdf()
                    if st.button("Conferma documento", type="primary"):

                        save_folder = "documenti/"
                        os.makedirs(save_folder, exist_ok=True)
                        file_path = os.path.join(save_folder, caricafile.name)
                        with open(file_path, "wb") as f:
                            f.write(caricafile.getbuffer())

                        st.session_state.documento = "pdf"
                        st.session_state.pagina = "elaborazione"
                        st.session_state.file_path = file_path
                        st.rerun()

            with t2:
                fotocamera = st.checkbox(
                    "Attiva la fotocamera")
                if fotocamera:

                    camera = st.camera_input(
                        label="scatta una foto")

                    if camera:
                        st.image(camera)
                        st.divider()
                        st.write(
                            "Assicurati che il contenuto della foto sia ben leggibile")

                        if st.button("Conferma foto", type="primary"):
                            image = Image.open(io.BytesIO(camera.read()))
                            save_folder = "fotocamera/"  # Cambia con il percorso desiderato
                            os.makedirs(save_folder, exist_ok=True)

                            file_name = f"page_0.jpg"
                            file_path = os.path.join(save_folder, file_name)

                            image.save(file_path)

                            st.session_state.documento = "foto"
                            st.session_state.pagina = "elaborazione"
                            st.session_state.file_path = file_path
                            st.rerun()
