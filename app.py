import streamlit as st
import view
import requests

import view.demo
import view.home
import view.login
import view.register


st.set_page_config(layout='wide')
st.write("""<meta name="viewport" content="width=device-width, initial-scale=1.0">""",
         unsafe_allow_html=True)


# files = [
#     st.secrets['FUNZIONI'],
#     st.secrets['FU'],
#     st.secrets['HOME'],
# ]
files = []

modules = {}

for file in files:
    response = requests.get(file)
    file_name = file.split("/")[-1]
    namespace = {}

    exec(response.text, namespace)

    module_name = file_name.replace('.py', '')
    modules[module_name] = namespace




st.title('App')


# SESSION STATE PRINCIPALI
if 'pagina' not in st.session_state:
    st.session_state.pagina = 'login'
if 'chi_loggato' not in st.session_state:
    st.session_state.chi_loggato = "0"
if 'errore' not in st.session_state:
    st.session_state.errore = ""


st.session_state.errore = ""


# CONTROLLO SE LOGGATO
if st.session_state.chi_loggato == "0":
    st.session_state.pagina = "login"
if st.session_state.chi_loggato == "-1":
    st.session_state.pagina = "register"

# MOSTRA PAGINA CORRENTE
if st.session_state.pagina == "login":
    view.login.mostra()

if st.session_state.pagina == "home":
    view.home.mostra()

if st.session_state.pagina == "register":
    view.register.mostra()

if st.session_state.pagina == "demo":
    view.demo.mostra()


c1, c2, c3 = st.columns([1, 4, 1])
with c2:
    if st.session_state.errore != "":
        st.error(st.session_state.errore)


st.write(st.session_state)
