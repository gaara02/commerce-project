import mysql.connector

# Connect with the MySQL Server
cnx = mysql.connector.connect(host='localhost',user='root', password='', database='ecommerce')

curA = cnx.cursor()

req= ("select * from  villes LIMIT 20")
curA.execute(req)
# Récupérez les résultats et les noms de colonnes
results = curA.fetchall()
column_names = [desc[0] for desc in curA.description]

# Fermez la connexion
cnx.close()

# Déterminez la largeur de chaque colonne en fonction de la donnée la plus longue
column_widths = [len(name) for name in column_names]
for row in results:
    for i, value in enumerate(row):
        column_widths[i] = max(column_widths[i],len(str(value)))
                               
# Affichez les résultats sous forme de tableau bien formaté
# En-têtes
for i in range(len(column_names)):
    print(column_names[i].ljust(column_widths[i]), end=" | ")
print()
print("-" * sum(column_widths + [3 * len(column_names) - 1]))

# Données
for row in results:
    for i in range(len(row)):
        print(str(row[i]).ljust(column_widths[i]), end=" | ")
    print()