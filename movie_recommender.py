import pandas as pd

file_path = '/Users/caseydudley/Desktop/movie-recommender/tmdb_5000_movies.csv'  # Make sure the path is correct
movies_df = pd.read_csv(file_path)

import ast

# Extract genres as a list from the JSON-like column
def extract_genres(genre_str):
    genres = ast.literal_eval(genre_str)
    return [genre['name'] for genre in genres]

movies_df['genres'] = movies_df['genres'].apply(extract_genres)

# Categorize movies by length
def categorize_runtime(runtime):
    if runtime <= 90:
        return 'Short'
    elif 90 < runtime <= 120:
        return 'Medium'
    else:
        return 'Long'

movies_df['length_category'] = movies_df['runtime'].apply(categorize_runtime)

import streamlit as st

# Streamlit UI
st.title("Movie Recommender")

# Filter by mood (genres)
all_genres = sorted(set([genre for sublist in movies_df['genres'] for genre in sublist]))
selected_genre = st.selectbox("Select a mood/genre", options=all_genres)

# Filter by language
all_languages = movies_df['original_language'].unique()
selected_language = st.selectbox("Select a language", options=all_languages)

# Filter by movie length
length_options = ['Short', 'Medium', 'Long']
selected_length = st.selectbox("Select a movie length", options=length_options)
# Filter the dataset based on user input
filtered_movies = movies_df[
    (movies_df['genres'].apply(lambda x: selected_genre in x)) &
    (movies_df['original_language'] == selected_language) &
    (movies_df['length_category'] == selected_length)
]
# Sort by top-rated first
filtered_movies = filtered_movies.sort_values(by='vote_average', ascending=False)

# Display movies
st.subheader(f"Top {selected_length} {selected_genre} Movies in {selected_language}")

for index, row in filtered_movies.iterrows():
    st.write(f"**{row['title']}**")
    st.write(f"Rating: {row['vote_average']}")
    st.write(f"Overview: {row['overview']}")
    st.write("---")

if filtered_movies.empty:
    st.write("No movies found matching the criteria.")

import streamlit as st
import pandas as pd
import ast

# Load the dataset
file_path = 'path_to_your_file/tmdb_5000_movies.csv'
movies_df = pd.read_csv(file_path)

# Extract genres as a list from the JSON-like column
def extract_genres(genre_str):
    genres = ast.literal_eval(genre_str)
    return [genre['name'] for genre in genres]

movies_df['genres'] = movies_df['genres'].apply(extract_genres)

# Categorize movies by length
def categorize_runtime(runtime):
    if runtime <= 90:
        return 'Short'
    elif 90 < runtime <= 120:
        return 'Medium'
    else:
        return 'Long'

movies_df['length_category'] = movies_df['runtime'].apply(categorize_runtime)

# Streamlit UI
st.title("Movie Recommender")

# Filter by mood (genres)
all_genres = sorted(set([genre for sublist in movies_df['genres'] for genre in sublist]))
selected_genre = st.selectbox("Select a mood/genre", options=all_genres)

# Filter by language
all_languages = movies_df['original_language'].unique()
selected_language = st.selectbox("Select a language", options=all_languages)

# Filter by movie length
length_options = ['Short', 'Medium', 'Long']
selected_length = st.selectbox("Select a movie length", options=length_options)

# Filter the dataset based on user input
filtered_movies = movies_df[
    (movies_df['genres'].apply(lambda x: selected_genre in x)) &
    (movies_df['original_language'] == selected_language) &
    (movies_df['length_category'] == selected_length)
]

# Sort by top-rated first
filtered_movies = filtered_movies.sort_values(by='vote_average', ascending=False)

# Display movies
st.subheader(f"Top {selected_length} {selected_genre} Movies in {selected_language}")

for index, row in filtered_movies.iterrows():
    st.write(f"**{row['title']}**")
    st.write(f"Rating: {row['vote_average']}")
    st.write(f"Overview: {row['overview']}")
    st.write("---")

if filtered_movies.empty:
    st.write("No movies found matching the criteria.")
