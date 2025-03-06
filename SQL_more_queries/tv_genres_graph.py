import sqlite3
import matplotlib.pyplot as plt

# Connexion à la base de données SQLite
conn = sqlite3.connect('hbtn_0d_tvshows.db')
cursor = conn.cursor()

# Exécution de la requête SQL pour obtenir les genres et le nombre de shows associés
cursor.execute("""
    SELECT tv_genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
    FROM tv_genres
    JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
    GROUP BY tv_genres.name
    HAVING COUNT(tv_show_genres.show_id) > 0
    ORDER BY number_of_shows DESC;
""")

# Récupération des résultats
data = cursor.fetchall()

# Séparer les genres et le nombre de shows pour les afficher graphiquement
genres = [row[0] for row in data]
number_of_shows = [row[1] for row in data]

# Créer le graphique
plt.figure(figsize=(10, 6))
plt.barh(genres, number_of_shows, color='skyblue')
plt.xlabel('Number of Shows')
plt.ylabel('Genre')
plt.title('Number of Shows Linked to Each Genre')
plt.gca().invert_yaxis()  # Inverser l'axe Y pour que le genre avec le plus grand nombre de shows soit en haut
plt.show()

# Fermer la connexion à la base de données
conn.close()
