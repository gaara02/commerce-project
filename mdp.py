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
array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']





curseur.execute('SELECT idClient FROM clients')
idClients = [row[0] for row in curseur.fetchall()]

for id_client in idClients:
    mdp = ''.join(random.choice(array) for _ in range(10))
    motdepasse = mdp

    req_update = "UPDATE clients Set mdp = %s WHERE idClient = %s"
    curseur.execute(req_update,(motdepasse, id_client))

conn_bd.commit()

    
curseur.close()
conn_bd.close()


