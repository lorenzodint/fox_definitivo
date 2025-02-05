import streamlit as st
import requests
import subprocess
import json
import pymongo
from pymongo import MongoClient
import bcrypt


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


def registra_utente(username, password):

    # controllo se username gia in uso
    if Collection_Utenti.find_one({"username": username}):
        return [False, "username già esistente"]

    # cifratura della password
    hashed_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    # registrazione utente
    user_data = {
        "username": username,
        "password": hashed_pw
    }

    try:
        Collection_Utenti.insert_one(user_data)
        return [True, "Registrazione avvenuta"]
    except Exception as e:
        return [False, f"Errore registrazione: {e}"]


def login_utente(username, password):
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
    
    c1, c2, c3 = st.columns([1, 4, 1], vertical_alignment="center")

    with c2:
        with st.container(border=True):
            st.header("Login")
            username = st.text_input(label="Username")
            password = st.text_input(label="password", type='password')

            c1, c2, c3 = st.columns([2, 0.1, 1])
            with c1:
                accedi = st.button("Accedi")
                if accedi:
                    loginUtente = login_utente(
                        username=username, password=password)
                    if loginUtente[0]:
                        st.session_state.chi_loggato = loginUtente[2]
                        st.session_state.pagina = "home"
                        st.rerun()
                    else:
                        st.session_state.errore = loginUtente[1]
            with c3:
                registrazione = st.button("Non hai un account?")
                if registrazione:
                    st.session_state.chi_loggato = "-1"
                    st.rerun()


if __name__ == "__main__":
    mostra()
    st.write(st.session_state)
