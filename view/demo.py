import streamlit as st
import requests
from PIL import Image
import io
import os
import time
import uuid


def mostra():
    with st.sidebar:
        st.title("menu laterale")

        if st.button("logout"):
            st.session_state.chi_loggato = "0"
            st.rerun()

    c1, c2, c3 = st.columns([1, 4, 1])
    with c2:
        with st.container():

            caricafile = st.file_uploader(
                label="Carica documento:", type=['pdf', 'PDF'])

            if caricafile is not None:
                # bytes_data = caricafile.read()
                st.write("nome file:", caricafile.name)
                # st.write(bytes_data)

            fotocamera = st.checkbox("Oppure attiva la fotocamera")

            camera = st.camera_input(
                label="scatta una foto", disabled=not fotocamera)

            if camera:
                st.image(camera)
            
                st.write("Assicurati che il contenuto della foto sia ben leggibile")
                
                if st.button("Utilizza foto"):
                    image = Image.open(io.BytesIO(camera.read()))
                    save_folder = "fotocamera/"  # Cambia con il percorso desiderato
                    os.makedirs(save_folder, exist_ok=True)
                    
                    file_name = f"foto_{uuid.uuid4().hex}.png"
                    file_path = os.path.join(save_folder, file_name)
                    
                    image.save(file_path)
                    
                    # st.image(file_path)