import streamlit as st
import pickle
import requests

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=0a12d5dca90871c4e597f8f14ca4270a&language=en-US'.format(movie_id))
    data = response.json()
    return "http://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movies):
    movie_index = movie[movie['title'] == movies].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended = []
    recommended_movies_poster = []
    for i in movies_list:
        movie_id = movie.iloc[i[0]].id
        recommended.append(movie.iloc[i[0]].title)
        #fetch posters from API
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended, recommended_movies_poster

movie = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))
movies_list = movie['title'].values

st.title("Movie Recommender System")
selected_movies_names = st.selectbox('Want to get recommendation! Feel free to search..!!', movies_list)

if st.button('Recommend'):
    names, posters = recommend(selected_movies_names)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])
