#!/usr/bin/env python3
import mysql.connector

# Connexion à la base de données
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="ecommerce",
    unix_socket='/Applications/MAMP/tmp/mysql/mysql.sock'
)

curseur = conn.cursor()

# Mettez à jour la colonne idCategorie dans la table Produits en utilisant la table Categories
req_update = """
    UPDATE Produits p
JOIN Categories c ON p.idCategorie = c.idCategorie
SET p.idCategorie = c.idCategorie
"""

curseur.execute(req_update)

# Validez la transaction
conn.commit()

# Fermez la connexion
conn.close()
