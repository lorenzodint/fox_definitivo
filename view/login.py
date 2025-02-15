import streamlit as st
import requests
import subprocess
import json
import pymongo
from pymongo import MongoClient
import bcrypt
import streamlit_shadcn_ui as ui


user = st.secrets['MONGO_USER']
password = st.secrets['MONGO_PASSWORD']

url_mongo = f"mongodb+srv://{user}:{password}@clusterfox.jluye.mongodb.net/"

cluster = MongoClient(url_mongo)
db = cluster.FOX
Collection_Utenti = db.utenti


user = {
    "nome": "Lorenzo",
    "cognome": "D'intino",
    "username": "altroancora"
}

# result = collection.insert_one(user)


def inserisci_x(collection, object):
    collection.insert_many(object)


def inserisci_1(collection, object):
    collection.insert_one(object)

# inserisci_1(collection=collection, object=user)


def update(collection, query_filter, value):
    collection.update_many(
        query_filter,
        {
            "$set":
                value
        }
    )


password = "1"
hashed_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
query_filter = {"username": "lodi"}
value = {"password": hashed_pw}

# update(collection=Collection_Utenti, query_filter=query_filter, value=value)


# collection.create_index([("username" , 1)], unique=True)


def login_utente(username, password):
    username = username.strip()
    password = password.strip()

    if username == "" or username == None:
        return [False, "Il campo username non può essere vuoto"]

    if password == "" or password == None:
        return [False, "Il campo password non può essere vuoto"]

    username = username.strip()
    password = password.strip()

    if username == "" or username == None:
        return [False, "Il campo username non può essere vuoto"]

    if password == "" or password == None:
        return [False, "Il campo password non può essere vuoto"]

    utente = Collection_Utenti.find_one({"username": username})

    if not utente:
        return [False, "Username errato"]

    if bcrypt.checkpw(password.encode('utf-8'), utente['password']):
        return [True, "Accesso effettuato", utente['_id']]
    else:
        return [False, "Password errata"]


# log = login_utente("lodi", "1")
# print(log[1])


def mostra():
    # st.session_state.errore = ""

    col1, col2, col3 = st.columns([1, 3, 1], vertical_alignment="center")

    with col2:
        with st.container(border=True):
            st.header("Login")
            username = ui.input(
                type="text", placeholder="Username", key="input_username")
            password = ui.input(
                type="password", placeholder="Password", key="input_password")

            c1, c2, c3 = st.columns([2, 0.1, 1])
            with c1:
                accedi = ui.button(
                    text="Accedi", variant="default", key="pulsante_accedi")
                if accedi:
                    loginUtente = login_utente(
                        username=username, password=password)
                    if loginUtente[0]:
                        st.session_state.chi_loggato = loginUtente[2]
                        st.session_state.pagina = "demo"
                        st.rerun()
                    else:
                        st.session_state.errore = loginUtente[1]

            with c3:
                registrazione = ui.button(
                    text="Non hai un account?", variant="outline", key="pulsante_vai_registrazione")
                if registrazione:
                    st.session_state.chi_loggato = "-1"
                    st.rerun()


def vanilla():
    c1, c2, c3 = st.columns([1, 3, 1])
    with c2:
        with st.container(border=True):
            st.header("Login")
            username = st.text_input(label="",
                                     placeholder="Username", key="login_username")
            password = st.text_input(label="",
                                     placeholder="Password", key="login_password", type="password")

            c1, c2, c3 = st.columns([2, 0.1, 1])
            with c1:
                accedi = st.button(
                    label="Accedi", key="login_accedi", type="primary")
                if accedi:
                    loginUtente = login_utente(
                        username=username, password=password)
                    if loginUtente[0]:
                        st.session_state.chi_loggato = loginUtente[2]
                        st.session_state.pagina = "demo"
                        st.rerun()
                    else:
                        st.session_state.errore = loginUtente[1]
            with c3:
                registrazione = st.button(
                    label="Non hai un account?", key="login_vai_registrazione")
                if registrazione:
                    st.session_state.chi_loggato = "-1"
                    st.rerun()


if __name__ == "__main__":
    mostra()
    st.write(st.session_state)
