#!/usr/bin/env python3
import random
import mysql.connector

conn_bd = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="ecommerce",
    unix_socket='/Applications/MAMP/tmp/mysql/mysql.sock',
)

curseur = conn_bd.cursor()


curseur.execute("SELECT idCommande FROM commandes")
liste_commandes = curseur.fetchall()


for id_commande in liste_commandes:
    
    no_lignes = random.randint(1, 3)

    
    for i in range(no_lignes):
        curseur.execute("SELECT `idProduit` FROM produits")
        produits = curseur.fetchall()
        id_produit = random.choice(produits)[0]
        
        quantite = random.randint(1, 4)

      
        curseur.execute(
            "INSERT INTO LignesCommandes(noligne, quantite, idProduit, idCommande) VALUES (%s, %s, %s, %s)",
            (i + 1, quantite, id_produit, id_commande[0]),
        )


        conn_bd.commit()


curseur.close()
conn_bd.close()






