#!/usr/bin/env python3
import random
import mysql.connector
conn_bd = mysql.connector.connect(
host = "localhost",
user = "root",
password = "root",
database = "ecommerce",
unix_socket= '/Applications/MAMP/tmp/mysql/mysql.sock',
)

curseur = conn_bd.cursor()
req1 = "select* from villes"
curseur.execute(req1)
resultat = curseur.fetchall()

valeurs_aleatoires = [random.choice(resultat) for _ in range(5)]

curseur.close()
conn_bd.close()


for valeur in valeurs_aleatoires:
    print(valeur)