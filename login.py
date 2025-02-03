import streamlit as st
from session import *
import mysql.connector as mysql
from mysql.connector import Error
import requests
import subprocess
import json
import pymongo
from pymongo import MongoClient
import bcrypt

# HOST = "localhost"
# DATABASE = "my_lorenzodintino"
# USER = "lorenzodintino"
# PASSWORD = "" #6zZ4MhnqrYVn


# url = 'https://lorenzodintino.altervista.org/IMPORT_STREAMLIT/CONFIG/config.php'
# data = {
#     "host": HOST,
#     "database": DATABASE,
#     "user": USER,
#     "password": PASSWORD,
# }

# response = requests.post(url, data=data)


# utente = SessionUtente()

# # utente.setNomeUtente = 'Lorenzo'

# st.write(response.text)


# # comando = ['php', 'php/query.php',
# #            'connessione', USER, PASSWORD, HOST, DATABASE]


# # risultato = subprocess.run(comando, capture_output=True, text=True, check=True)


# # st.write(risultato.stdout.strip())


# # url = 'https://lorenzodintino.altervista.org/IMPORT_STREAMLIT/CONFIG/query.php'


# # data = {
# #     'action': 'select_0',
# #     'params': {
# #         'query': "SELECT * FROM ST_utenti"
# #     }
# # }

# # # Invia la richiesta POST
# # response = requests.post(url, data=json.dumps(data), headers={
# #     'Content-Type': 'application/json'})

# # # Verifica la risposta
# # if response.status_code == 200:
# #     result = response.json()
# #     st.write(type(result))

# #     # if 'risultato' in result:
# #     #     st.write("Risultato:", result['risultato'])
# #     # elif 'errore' in result:
# #     #     st.write("Errore:", result['errore'])
# # else:
# #     st.write("Richiesta fallita con status code:", response.status_code)


# config = {
#     'host': HOST,
#     'user': USER,
#     'password': PASSWORD,
#     'database': DATABASE,
#     # 'port': 3306  # Verifica la porta corretta
# }


# try:
#     # Stabilisci la connessione
#     connection = mysql.connect(**config)

#     if connection.is_connected():
#         st.write("Connesso con successo al database")

#         # Crea un cursore per eseguire le query
#         cursor = connection.cursor()

#         # Esegui una query di esempio
#         query = "SELECT * FROM ST_utenti"
#         cursor.execute(query)

#         # Ottieni i risultati della query
#         results = cursor.fetchall()

#         # Stampa i risultati
#         for row in results:
#             st.write(row)

# except Error as e:
#     st.write(f"Errore durante la connessione al database: {e}")

# finally:
#     # Chiudi la connessione
#     if 'connection' in locals() and connection.is_connected():
#         cursor.close()
#         connection.close()
#         st.write("Connessione chiusa")


user = "lodi16799"
password = "P4ssword.M0ng0"

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
