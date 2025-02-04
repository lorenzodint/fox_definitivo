import streamlit as st
import utils
import utils.pdf_to_img
import utils.file_def as ai
import view.caricamento
import shutil


def ai_analisi(image_path, output_dir, ocr):
    api = st.secrets['TEST_FOX']

    result = ai.analyze_and_save(
        api=api,
        image_path=image_path,
        output_dir=output_dir,
        use_ocr=ocr
    )

    st.session_state.risultato = result


def mostra():

    view.caricamento.mostra()

    if st.session_state.documento == "pdf":
        utils.pdf_to_img.convert_pdf(st.session_state.file_path, "images/")
        st.session_state.file_path = "images/page_0.jpg"
    elif st.session_state.documento == "foto":
        old_path = st.session_state.file_path
        new_path = "images/page_0.jpg"
        shutil.move(old_path, new_path)
        st.session_state.file_path = new_path

    if ai_analisi(st.session_state.file_path, "analisi-results", True):
        st.write(st.session_state.risultato)

    if st.button('login'):
        st.session_state.chi_loggato = "0"
