# Movie Recommendation App - README

## What’s This App?
Welcome to my second project and my first shot at using an API! This app recommends movies based on your mood, time, and streaming subscriptions. Built with Flask and powered by the TMDb API, it’s a quick way to get movie suggestions that actually fit what you’re looking for. The app is now online at PythonAnywhere, so you can check it out anytime without needing to set it up locally.

## Key Features
- **Pick a Genre**: Choose from a range of genres to set the mood.
- **Set Time Limits**: Recommendations are filtered to fit the time you have available.
- **Choose Streaming Services**: See only movies available on your selected streaming platforms.
- **Recent & Classic Movies**: Get both recent picks (within the last 10 years) and classics (over 10 years old).

## Getting Started
### Requirements
- Python 3.x
- Some basic knowledge of Python and APIs (not a deal-breaker, though!)

### Setting Up Locally (if you want)
Install dependencies:
```python
!pip install requests
!pip install flask
!pip install pyngrok
```

Replace the API keys with your own:
1. **TMDb API Key**: Update the `API_KEY` variable in the code.
2. **ngrok Auth Token**: Add your ngrok token where needed to enable public access.

### Project Files
- **`app.py`**: The main code for running the app.
- **`templates/`**: HTML templates for the input form and results display.

## How to Use It
1. Go to the app’s homepage on PythonAnywhere.
2. Select your genre, set the time you have for a movie, and choose your streaming platforms.
3. Hit “Recommend” to get tailored movie suggestions!

## Behind the Scenes
- **TMDb API**: Pulls movie details like title, release date, rating, cast, and streaming availability.
- **Genre Mapping**: Matches genre names to TMDb genre IDs to filter movies accurately.

### Example Use
1. **You Enter**:
   - Genre: "Comedy"
   - Time Available: 120 minutes
   - Streaming Services: "Netflix" and "Amazon Prime"
2. **You Get**:
   - A recent and an older comedy movie (both available on your selected platforms) with details on cast, runtime, and where to watch.

## Main Code Functions
- **`get_movie_details()`**: Retrieves all the details for a specific movie, like cast, streaming options, and trailer links.
- **`get_tmdb_movies()`**: Fetches movies based on your input for genre, runtime, and popularity.

## Ideas for the Future
- Add more language options.
- Add TV shows to the mix.
- Add account creation so users can save recommendations.
- Fine-tune movie lengths to match exact time limits.

## Thanks!
Shoutout to the TMDb API for the movie data and to ngrok for making remote access easy during development. Enjoy, and happy movie-watching!
