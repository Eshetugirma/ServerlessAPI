import logging
import os
import json
from google.cloud import firestore
from google.cloud import secretmanager
from flask import jsonify
import openai

# Initialize Firestore DB
db = firestore.Client()

# Get secret from Secret Manager
def get_secret(secret_id):
    client = secretmanager.SecretManagerServiceClient()
    name = f"projects/{os.getenv('GCP_PROJECT_ID')}/secrets/{secret_id}/versions/latest"
    response = client.access_secret_version(name=name)
    return response.payload.data.decode('UTF-8')

# Retrieve OpenAI API key from Secret Manager
openai.api_key = get_secret('openaiapikey')

# Function 1: Return a JSON list of all movies in your DB
def get_movies():
    movie_list = []
    movies_ref = db.collection('movies')
    docs = movies_ref.stream()

    for doc in docs:
        movie_list.append(doc.to_dict())

    return jsonify(movie_list)

# Function 2: Return a list of movies by year
def get_movies_by_year(year):
    movie_list = []
    movies_ref = db.collection('movies')
    docs = movies_ref.where('releaseYear', '==', year).stream()

    for doc in docs:
        movie_list.append(doc.to_dict())

    return jsonify(movie_list)

# Function 3: Generate summary for a movie using OpenAI API
def generate_summary(movie_name):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"Summarize the movie: {movie_name} in 2 sentences"}
        ],
        temperature=1,
        max_tokens=200,
    )
    return response.choices[0].message['content']

# Function to get movie by title and add generated summary
def get_movie_by_summary(title):
    movie_list = []
    movies_ref = db.collection('movies')
    docs = movies_ref.where('title', '==', title).stream()

    for doc in docs:
        movie = doc.to_dict()
        movie['generatedSummary'] = generate_summary(movie['title'])
        movie_list.append(movie)

    return jsonify(movie_list)

# Cloud Function: Get all movies
def get_movies_http(request):
    movies = get_movies()
    return movies

# Cloud Function: Get movies by year
def get_movies_by_year_http(request):
    year = request.args.get('year')
    if not year:
        return jsonify({"error": "Year parameter is required"}), 400
    movies = get_movies_by_year(year)
    return movies

# Cloud Function: Get movie summary
def get_movie_summary_http(request):
    title = request.args.get('title')
    if not title:
        return jsonify({"error": "Title parameter is required"}), 400
    movie = get_movie_by_summary(title)
    return movie


