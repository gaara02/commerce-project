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
column_names = [desc[0] for desc in curseur.description]
curseur.close()
conn_bd.close()

column_widths = [len(name) for name in column_names]
for valeur in valeurs_aleatoires:
    for i, value in enumerate(valeur):
        column_widths[i] = max(column_widths[i],len(str(value)))
                               

for i in range(len(column_names)):
    print(column_names[i].ljust(column_widths[i]), end=" | ")
print()
print("-" * sum(column_widths + [3 * len(column_names) - 1]))


for valeur in valeurs_aleatoires:
    for i in range(len(valeur)):
        print(str(valeur[i]).ljust(column_widths[i]), end=" | ")
    print()
    print("-" * sum(column_widths + [3 * len(column_names) - 1]))