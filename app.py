import streamlit as st
import requests
from pathlib import Path
######################################################
import view
import view.login
import view.caricamento
import view.demo
import view.elaborazione
import view.home
import view.register
import view.risultato


# # Delete all the items in Session state
# for key in st.session_state.keys():
#     del st.session_state[key]

st.set_page_config(
    layout='wide'
)
st.write("""<meta name="viewport" content="width=device-width, initial-scale=1.0">""",
         unsafe_allow_html=True)


files = []

modules = {}

for file in files:
    response = requests.get(file)
    file_name = file.split("/")[-1]
    namespace = {}

    exec(response.text, namespace)

    module_name = file_name.replace('.py', '')
    modules[module_name] = namespace


Path('document').mkdir(parents=True, exist_ok=True)
Path('images').mkdir(parents=True, exist_ok=True)
Path('analisi').mkdir(parents=True, exist_ok=True)

# SESSION STATE PRINCIPALI
if 'pagina' not in st.session_state:
    st.session_state.pagina = 'home'
if 'chi_loggato' not in st.session_state:
    st.session_state.chi_loggato = "0"
if 'errore' not in st.session_state:
    st.session_state.errore = ""


st.session_state.errore = ""

if 'fotocamera' not in st.session_state:
    st.session_state.fotocamera = False
if 'documento' not in st.session_state:
    st.session_state.documento = "pdf"
if 'caricamento' not in st.session_state:
    st.session_state.caricamento = ""
if 'file_path' not in st.session_state:
    st.session_state.file_path = ""
if 'risultato' not in st.session_state:
    st.session_state.risultato = ""


# CONTROLLO SE LOGGATO
if st.session_state.chi_loggato == "0":
    st.session_state.pagina = "home"
if st.session_state.chi_loggato == "-1":
    st.session_state.pagina = "register"
if st.session_state.chi_loggato == "-2":
    st.session_state.pagina = "login"
    


# MOSTRA PAGINA CORRENTE
if st.session_state.pagina == "login":
    view.login.vanilla()
if st.session_state.pagina == "home":
    view.home.mostra()
if st.session_state.pagina == "register":
    view.register.vanilla()
if st.session_state.pagina == "demo":
    view.demo.mostra()
if st.session_state.pagina == "elaborazione":
    view.elaborazione.mostra()
if st.session_state.pagina == "risultato":
    view.risultato.mostra()


c1, c2, c3 = st.columns([1, 4, 1])
with c2:
    if st.session_state.errore != "":
        st.error(st.session_state.errore)


# st.write(st.session_state)
