#!/usr/bin/env python3

#Ce code permet de generer des donnees aleatoires a partir de la base de donnees ecommerce
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

    
req1 = "SELECT country, name FROM villes"
curseur.execute(req1)
resultat = curseur.fetchall()

   
curseur.execute("SELECT idClient FROM clients")
id_clients = [row[0] for row in curseur.fetchall()]

    
for id_client in id_clients:
        valeur = random.choice(resultat)
        ville = valeur[1]
        pays = valeur[0]

        
        req_update = "UPDATE clients SET ville = %s, pays = %s WHERE idClient = %s"
    
       
        curseur.execute(req_update, (ville, pays, id_client))

    
conn_bd.commit()

    
curseur.close()
conn_bd.close()


