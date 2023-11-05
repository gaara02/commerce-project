#!/usr/bin/env python3
import random
from datetime import datetime
import mysql.connector
conn_bd = mysql.connector.connect(
host = "localhost",
user = "root",
password = "root",
database = "ecommerce",
unix_socket= '/Applications/MAMP/tmp/mysql/mysql.sock',
)

curseur = conn_bd.cursor()

curseur.execute("SELECT idClient FROM clients")
id_clients = [row[0] for row in curseur.fetchall()]

#Statut
statut = ['en cours', 'payés', 'livrée', 'annulée']


#Date Commande
datedebut = datetime(2020, 1, 1)

datefin = datetime(2022, 9, 1)

debut = datedebut.timestamp()
fin = datefin.timestamp()



for id_client in id_clients:
    nombre_commande = random.randint(0, 5)
    
    for _ in range(nombre_commande):
        date_aleatoire = random.uniform(debut, fin)
        date_commande = datetime.fromtimestamp(date_aleatoire)
        dateCommande = date_commande.strftime("%Y-%m-%d")
        statutRandom = random.choice(statut)

        curseur.execute("INSERT INTO commandes (dateCommande, statut, idClient) VALUES (%s, %s, %s)",
                        (dateCommande, statutRandom, id_client))
        conn_bd.commit()  

curseur.close()
conn_bd.close()
