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
        column_widths[i] = max(column_widths[i], len(str(value)))

# Affichez les résultats sous forme de tableau bien formaté
# En-têtes
header = " | ".join(name.ljust(width) for name, width in zip(column_names, column_widths))
print(header)
print("-" * len(header))  # Ligne de séparation pour les en-têtes

# Données
for row in results:
    row_str = " | ".join(str(value).ljust(width) for value, width in zip(row, column_widths))
    print(row_str)
    print("-" * len(header))
