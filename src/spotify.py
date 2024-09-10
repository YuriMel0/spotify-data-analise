import streamlit as st
import pandas as pd

st.set_page_config(
    layout="wide",
    page_title="Spotify"
)
df = pd.read_csv("../data/spotify_tracks.csv")
df.set_index("name", inplace=True)

artists = df["artists"].value_counts().index

artist = st.selectbox("Artista", artists)
df_filtered = df[df["artists"] == artist]



st.bar_chart(df_filtered["popularity"])
