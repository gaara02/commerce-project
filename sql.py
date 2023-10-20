#!/usr/bin/env python3
import mysql.connector
conn_bd = mysql.connector.connect(
host = "localhost",
user = "root",
password = "root",
database = "ecommerce",
unix_socket= '/Applications/MAMP/tmp/mysql/mysql.sock',
)

curseur = conn_bd.cursor()
req1 = "select* from custormers"
curseur.execute(req1)
resultat = curseur.fetchall()
for row in resultat[:20]:
    print (row)