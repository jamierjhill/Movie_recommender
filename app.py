!pip install requests
!pip install flask
!pip install pyngrok


from flask import Flask, request, render_template
from pyngrok import ngrok
import requests
import random
from datetime import datetime
import os

# Initialize Flask app
app = Flask(__name__, template_folder='/content/drive/MyDrive/Colab Notebooks/movie_recommender/templates')  

# Set ngrok auth token
ngrok.set_auth_token("")
public_url = ngrok.connect(5000)  
print("Ngrok tunnel URL:", public_url)

# TMDb API Key and Base URL
API_KEY = ''
BASE_URL = 'https://api.themoviedb.org/3'

# Genre mapping for direct genre input
genre_mapping = {
    'comedy': 35,
    'thriller': 53,
    'drama': 18,
    'adventure': 12,
    'family': 10751,
    'horror': 27,
    'romance': 10749,
    'action': 28,
    'documentary': 99,
    'mystery': 9648,
    'fantasy': 14,
    'animation': 16,
    'music': 10402,
    'crime': 80,
    'science fiction': 878,
    'history': 36,
    'tv movie': 10770
}

# Function to get movie details from TMDb
def get_movie_details(movie_id, country_code='US'):
    url = f"{BASE_URL}/movie/{movie_id}"
    params = {'api_key': API_KEY, 'append_to_response': 'videos,credits,watch/providers'}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        trailer_url = next((f"https://www.youtube.com/watch?v={video['key']}" for video in data['videos']['results']
                            if video['type'] == 'Trailer' and video['site'] == 'YouTube'), None)
        cast = ', '.join([member['name'] for member in data['credits']['cast'][:5]])
        providers = data['watch/providers']['results'].get(country_code, {})
        streaming_services = ', '.join([provider['provider_name'] for provider in providers.get('flatrate', [])])
        return {
            'title': data['title'],
            'release_date': data.get('release_date', 'N/A'),
            'vote_average': data['vote_average'],
            'runtime': data.get('runtime', 'N/A'),
            'trailer_url': trailer_url,
            'cast': cast,
            'streaming_services': streaming_services or 'Not available for streaming'
        }
    return None

# Function to get movies from TMDb API based on genre, runtime, etc.
def get_tmdb_movies(genre_id, min_runtime, max_runtime, language, year_min=None, year_max=None, min_rating=0):
    url = f"{BASE_URL}/discover/movie"
    params = {
        'api_key': API_KEY,
        'with_genres': genre_id,
        'with_original_language': language,
        'with_runtime.gte': min_runtime,
        'with_runtime.lte': max_runtime,
        'sort_by': 'popularity.desc',
        'vote_average.gte': min_rating,  # Apply the minimum rating filter
        'include_adult': False,
    }
    if year_min:
        params['primary_release_date.gte'] = f"{year_min}-01-01"
    if year_max:
        params['primary_release_date.lte'] = f"{year_max}-12-31"

    response = requests.get(url, params=params)
    if response.status_code == 200:
        movies = response.json().get('results', [])
        return [get_movie_details(movie['id']) for movie in movies if get_movie_details(movie['id']) is not None]
    return []


# Define route for the homepage
@app.route('/')
def home():
    return render_template('recommend_input.html')

# Define route for displaying recommendations
@app.route('/recommend', methods=['POST'])
def recommend():
    user_genre = request.form.get('genre').strip().lower()
    time_available = int(request.form.get('time_available').strip())
    streaming_services = request.form.getlist('streaming_services')

    # Get genre ID directly from the input
    genre_id = genre_mapping.get(user_genre)
    if not genre_id:
        return "Genre not found. Please enter a valid genre.", 400

    min_runtime = max(0, time_available - 20)
    max_runtime = time_available
    current_year = datetime.now().year

    # Fetch movies based on criteria
    recent_movies = get_tmdb_movies(genre_id, min_runtime, max_runtime, language='en', year_min=current_year - 10, year_max=current_year)
    older_movies = get_tmdb_movies(genre_id, min_runtime, max_runtime, language='en', year_max=current_year - 10)

    # Filter movies by streaming services
    recent_movies_filtered = [movie for movie in recent_movies if movie and any(service in movie['streaming_services'] for service in streaming_services)]
    older_movies_filtered = [movie for movie in older_movies if movie and any(service in movie['streaming_services'] for service in streaming_services)]

    # Choose a random movie if available, else set to None
    recent_movie = random.choice(recent_movies_filtered) if recent_movies_filtered else None
    older_movie = random.choice(older_movies_filtered) if older_movies_filtered else None

    recommendations = []
    if recent_movie:
        recommendations.append((recent_movie, "Recent Movie (within last 10 years)"))
    else:
        recommendations.append((None, "No recent movies found matching your criteria."))

    if older_movie:
        recommendations.append((older_movie, "Older Movie (more than 10 years old)"))
    else:
        recommendations.append((None, "No older movies found matching your criteria."))

    return render_template('recommendations.html', genre=user_genre.capitalize(), recommendations=recommendations)

if __name__ == '__main__':
    app.run(port=5000)
