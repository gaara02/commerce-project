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
req= ("select * from  villes LIMIT 20")
curseur.execute(req)

results = curseur.fetchall()
column_names = [desc[0] for desc in curseur.description]


conn_bd.close()


column_widths = [len(name) for name in column_names]
for row in results:
    for i, value in enumerate(row):
        column_widths[i] = max(column_widths[i],len(str(value)))
                               

for i in range(len(column_names)):
    print(column_names[i].ljust(column_widths[i]), end=" | ")
print()
print("-" * sum(column_widths + [3 * len(column_names) - 1]))


for row in results:
    for i in range(len(row)):
        print(str(row[i]).ljust(column_widths[i]), end=" | ")
    print()
    print("-" * sum(column_widths + [3 * len(column_names) - 1]))