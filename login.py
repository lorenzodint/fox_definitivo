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

    utente = Collection_Utenti.find_one({"username": username})

    if not utente:
        return [False, "Username errato"]

    if bcrypt.checkpw(password.encode('utf-8'), utente['password']):
        return [True, "Accesso effettuato"]
    else:
        return [False, "Password errata"]


# log = login_utente("lodi", "1")
# print(log[1])
if __name__ == "__main__":
    st.write('MONGO')

    st.write(cluster.server_info())
    st.write('Login')
