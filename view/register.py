import streamlit as st
import streamlit_shadcn_ui as ui
import datetime
from pymongo import MongoClient
import bcrypt

user = st.secrets['MONGO_USER']
password = st.secrets['MONGO_PASSWORD']

url_mongo = f"mongodb+srv://{user}:{password}@clusterfox.jluye.mongodb.net/"

cluster = MongoClient(url_mongo)
db = cluster.FOX
Collection_Utenti = db.utenti


def registra_utente(nome, cognome, nascita, telefono, email, username, password):

    if nome == "" or nome == None:
        return [False, "Inserire un nome"]
    if cognome == "" or cognome == None:
        return [False, "Inserire un cognome"]
    if telefono == "" or telefono == None:
        return [False, "Inserire un numero di telefono"]
    if email == "" or email == None:
        return [False, "Inserire una email"]
    if password == "" or password == None:
        return [False, "Inserire una password"]

    nome = nome.strip()
    cognome = cognome.strip()
    try:
        telefono = int(telefono)
    except ValueError:
        return [False, "Inserire un numero di telefono"]
    email = email.strip()
    username = username.strip()
    password = password.strip()

    if nome == "" or nome == None:
        return [False, "Inserire un nome"]
    if cognome == "" or cognome == None:
        return [False, "Inserire un cognome"]
    if telefono == "" or telefono == None:
        return [False, "Inserire un numero di telefono"]
    if email == "" or email == None:
        return [False, "Inserire una email"]
    if password == "" or password == None:
        return [False, "Inserire una password"]

    # controllo se username gia in uso
    if Collection_Utenti.find_one({"username": username}):
        return [False, "username già esistente"]

    nascita = nascita.isoformat()

    # cifratura della password
    hashed_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    # registrazione utente
    user_data = {
        "nome": nome,
        "cognome": cognome,
        "nascita": nascita,
        "telefono": telefono,
        "email": email,
        "username": username,
        "password": hashed_pw
    }

    try:
        Collection_Utenti.insert_one(user_data)
        return [True, "Registrazione avvenuta"]
    except Exception as e:
        return [False, f"Errore registrazione: {e}"]


def mostra():
    # st.session_state.errore = ""

    c1, c2, c3 = st.columns(
        [1, 3, 1], vertical_alignment='center')
    with c2:
        with st.container(border=True):
            st.header("Registrazione")
            c1, c2 = st.columns([1, 1], vertical_alignment='center')
            with c1:
                nome = ui.input(
                    type='text', placeholder='Nome', key='inp_nome')
                telefono = ui.input(
                    type="number", placeholder="Telefono", key="inp_telefono")

            with c2:
                cognome = ui.input(
                    type='text', placeholder='Cognome', key='inp_cognome')
                email = ui.input(
                    type="email", placeholder="Email", key="inp_email")

            # nascita = ui.date_picker(
            #     key="inp_nascita", mode="single", label="Data di nascita")
            nascita = st.date_input(label="Data di nascita", format="DD/MM/YYYY",
                                    min_value=datetime.date(1920, 1, 1), max_value="today")

            c1, c2 = st.columns([1, 1], vertical_alignment='center')
            with c1:
                username = ui.input(
                    type='username', placeholder='Username', key='inp_username')
            with c2:
                password = ui.input(
                    type='password', placeholder='Password', key='inp_password')

            c1, c2, c3 = st.columns([2, 0.1, 1])
            with c1:
                registrazione = ui.button(
                    text="Registrati", key="pulsante_registrazione", variant="default")
                if registrazione:
                    registraUtente = registra_utente(
                        nome=nome,
                        cognome=cognome,
                        nascita=nascita,
                        telefono=telefono,
                        email=email,
                        username=username,
                        password=password,
                    )

                    if registraUtente[0]:
                        st.session_state.chi_loggato = "-2"
                        st.rerun()
                        # st.write("OK")
                    else:
                        # st.write("NO")
                        st.session_state.errore = registraUtente[1]

            with c3:
                login = ui.button(text="Hai già un account?",
                                  key="pulsante_vai_login_2", variant="outline")
                if login:
                    st.session_state.chi_loggato = "-2"
                    st.rerun()


def vanilla():
    c1, c2, c3 = st.columns([1, 3, 1])
    with c2:
        with st.container(border=True):
            st.header("Registrazione")
            c1, c2 = st.columns([1, 1], vertical_alignment='center')
            with c1:
                nome = st.text_input(
                    label="", placeholder="Nome", key="register_nome")
                # telefono = st.number_input(
                #     label="", placeholder="Telefono", key="register_telefono", value=None)
                telefono = st.text_input(label="", placeholder="Telefono", key="register_telefono")

            with c2:
                cognome = st.text_input(
                    label="", placeholder="Cognome", key="register_cognome")
                email = st.text_input(
                    label="", placeholder="Email", key="register_email")

            nascita = st.date_input(label="Data di nascita", format="DD/MM/YYYY",
                                    min_value=datetime.date(1920, 1, 1), max_value="today", key="register_nascita")

            with c1:
                username = st.text_input(
                    label="", placeholder="Username", key="register_username")
            with c2:
                password = st.text_input(
                    label="", placeholder="Password", key="register_password")

            c1, c2, c3 = st.columns([2, 0.1, 1])
            with c1:
                registrazione = st.button(
                    label="Registrati", type="primary", key="register_registrazione")
                if registrazione:
                    registraUtente = registra_utente(
                        nome=nome,
                        cognome=cognome,
                        nascita=nascita,
                        telefono=telefono,
                        email=email,
                        username=username,
                        password=password,
                    )

                    if registraUtente[0]:
                        st.session_state.chi_loggato = "-2"
                        st.rerun()
                        # st.write("OK")
                    else:
                        # st.write("NO")
                        st.session_state.errore = registraUtente[1]

            with c3:
                login = st.button(label="Hai già un account?",
                                  type="tertiary", key="register_vai_login")
                if login:
                    st.session_state.chi_loggato = "-2"
                    st.rerun()


if __name__ == "__main__":

    print(registra_utente(
        nome="",
        cognome=None,
        nascita="16/07/1999",
        telefono="2323234",
        email="Mail",
        username="Mail",
        password=""
    ))
