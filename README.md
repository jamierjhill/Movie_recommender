# Movie Recommendation App - README

## Project Overview
This project is a movie recommendation web application, developed as my second project and my first experience working with an API. The application uses the TMDb (The Movie Database) API to recommend movies based on user preferences, including genre, runtime, and available streaming services. The app is powered by Flask, hosted via an ngrok tunnel, and provides dynamic recommendations of recent and older movies tailored to user-selected criteria.

## Features
- **Genre Selection**: Users can choose a genre from a predefined list.
- **Runtime Filter**: Recommendations are filtered based on the user’s available time.
- **Streaming Services Filter**: Only shows movies available on selected streaming platforms.
- **Recent and Older Movies**: The app recommends a recent movie (from the last 10 years) and an older movie (over 10 years old) if they match the user's criteria.

## Installation and Setup
### Prerequisites
- Python 3.x
- Access to Google Colab or a local environment that supports Flask and ngrok
- Basic understanding of Python and APIs

### Installing Dependencies
Install the required libraries:
```python
!pip install requests
!pip install flask
!pip install pyngrok
```

### Cloning the Project
Copy the project code and adjust the paths for templates to fit your environment.

### Setting Up API Keys and ngrok
1. **TMDb API Key**: Replace the `API_KEY` variable with your own TMDb API key.
2. **ngrok Auth Token**: Replace `ngrok.set_auth_token()` with your ngrok authentication token.

## Project Structure
- **`app.py`**: Main Flask application file.
- **`templates`**: HTML templates for user inputs (`recommend_input.html`) and recommendations (`recommendations.html`).

## Usage
1. **Starting the Application**: Run `app.py` in your Python environment. The ngrok tunnel will generate a URL, providing access to your Flask app.
2. **Using the Web App**:
   - On the home page, select a genre, specify your available time, and choose your streaming services.
   - Click "Recommend" to receive a list of recommended movies.

### API Details
- **TMDb API**: Fetches movie details, including title, release date, rating, runtime, cast, and streaming availability.
- **Genre Mapping**: Maps user-input genres to TMDb genre IDs for accurate recommendations.

### Example Workflow
1. **User Input**:
   - Genre: "Comedy"
   - Time Available: 120 minutes
   - Streaming Services: "Netflix", "Amazon Prime"
2. **Recommendations**:
   - A recent movie and an older movie are selected based on the criteria and displayed with relevant details like title, release date, rating, cast, and available streaming services.

## Code Walkthrough
- **`get_movie_details()`**: Fetches detailed information about a movie from TMDb, including cast, runtime, and streaming options.
- **`get_tmdb_movies()`**: Retrieves movies based on genre, runtime, and popularity. It uses additional filters for year and rating.
- **Home and Recommendation Routes**:
  - **Home Route (`/`)**: Displays the user input form for selecting genre, runtime, and streaming services.
  - **Recommendation Route (`/recommend`)**: Processes user inputs, fetches matching movies, and displays them on the recommendations page.

## Future Improvements
- Add more filtering options, such as language.
- Add TV Shows
- Enable user account creation to save favorite recommendations.
- Improve runtime accuracy by suggesting movies closer to the specified time.

## Acknowledgments
Cheers to the TMDb API for providing access to  movie data and to ngrok for allowing easy tunneling for local development.
