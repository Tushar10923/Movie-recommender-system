import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    movie_index = movies[movies['Series_Title'] == movie].index[0]
    distances = similarity[movie_index]
    ms_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies=[]
    recommended_movies_posters=[]
    for i in ms_list:
        recommended_movies.append(movies.iloc[i[0]].Series_Title)
        recommended_movies_posters.append(movies.iloc[i[0]].Poster_Link)
    return recommended_movies,recommended_movies_posters


movies_list = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_list)
st.title('Movie recommender System')

similarity=pickle.load(open('similarity.pkl','rb'))



movie_name = st.selectbox(
    'Which Movie you want to select?',
    movies['Series_Title'].values
)

if st.button('Recommend'):
    names,posters = recommend(movie_name)

    col1, col2, col3, col4, col5 = st.beta_columns(5)
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
