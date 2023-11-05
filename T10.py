#!/usr/bin/env python3
import mysql.connector

# Se connecter à la base de données
conn_bd = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="ecommerce",
    unix_socket='/Applications/MAMP/tmp/mysql/mysql.sock',
)

curseur = conn_bd.cursor()


curseur.execute("SELECT category FROM products")
categories = curseur.fetchall()


relations_categories = {}


for cat in categories:
    cat_chaine = cat[0].split(" | ")  
    cat_mere = None

    for cat_fille in cat_chaine:
       
        if cat_fille not in relations_categories:
            
            curseur.execute("INSERT INTO Categories (nomCategorie, idCategorieMere) VALUES (%s, %s)",
                            (cat_fille, cat_mere))
            conn_bd.commit()

           
            curseur.execute("SELECT LAST_INSERT_ID()")
            id_cat_fille = curseur.fetchone()[0]

            
            relations_categories[cat_fille] = id_cat_fille

        
        cat_mere = relations_categories[cat_fille]

curseur.close()
conn_bd.close()
