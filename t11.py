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

cursor = conn.cursor()


query = """
INSERT INTO Produits (nomproduit, prix, poids, idCategorie)
SELECT p.`Product Name`, p.`Selling Price`, p.`Shipping Weight`, c.idCategorie
FROM Products p
JOIN Categories c ON p.Category = c.nomCategorie



"""

cursor.execute(query)
conn.commit()


cursor.close()
conn.close()
