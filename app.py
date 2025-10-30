import streamlit as st
import pickle
import requests
import random

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def user_based_recommendations():
    random_indices = random.sample(range(len(movies_list)), 5)
    random_movies = []
    random_posters = []

    for idx in random_indices:
        random_movies.append(movies_list.iloc[idx].title)
        random_posters.append(fetch_poster(movies_list.iloc[idx].movie_id))

    return random_movies, random_posters


def recommend(movie):
  movie_index=movies_list[movies_list['title']==movie].index[0]
  distances=similarity[movie_index]
  new_movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
  recommended_movies=[]
  recommended_posters=[]
  for i in new_movies_list:
    recommended_movies.append(movies_list.iloc[i[0]].title)
    recommended_posters.append(fetch_poster(movies_list.iloc[i[0]].movie_id))
  return recommended_movies, recommended_posters

movies_list = pickle.load(open("movies.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))
st.title("Movie Recommendation System")
option = st.selectbox(
    "Choose a movie:",
    (movies_list['title'].values)
)

if st.button("Reccomend", type="primary"):
    st.header('Content based recommendation:')
    name,poster = recommend(option)
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.text(name[0])
        st.image(poster[0])
    with col2:
        st.text(name[1])
        st.image(poster[1])
    with col3:
        st.text(name[2])
        st.image(poster[2])
    with col4:
        st.text(name[3])
        st.image(poster[3])
    with col5:
        st.text(name[4])
        st.image(poster[4])
    st.header('user based recommendation:')
    names, posters = user_based_recommendations()
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