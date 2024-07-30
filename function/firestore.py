from google.cloud import firestore

# Initialize Firestore DB
db = firestore.Client()

# Movie data
movies = [
    {"title": "Inception", "releaseYear": "2010", "genre": "Science Fiction, Action", "coverUrl": "https://example.com/inception.jpg"},
    {"title": "The Shawshank Redemption", "releaseYear": "1994", "genre": "Drama, Crime", "coverUrl": "https://example.com/shawshank-redemption.jpg"},
    {"title": "The Dark Knight", "releaseYear": "2008", "genre": "Action, Crime, Drama", "coverUrl": "https://example.com/dark-knight.jpg"}
]

for movie in movies:
    db.collection('movies').add(movie)
    