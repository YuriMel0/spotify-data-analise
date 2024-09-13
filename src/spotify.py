import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(
    layout="wide",
    page_title="Spotify"
)

base_dir = Path(__file__).resolve().parents[1]
db_path = base_dir / 'data' / 'spotify_tracks.csv'
df = pd.read_csv(db_path)

df.set_index("name", inplace=True)

artists = df["artists"].value_counts().index

artist = st.selectbox("Artista", artists)
df_filtered = df[df["artists"] == artist]

albuns = df_filtered["album"].value_counts().index
album = st.selectbox("Album", albuns)

df_filtered2 = df[df["album"] == album]
display = st.checkbox("Grafico")
if display:
    st.bar_chart(df_filtered2["popularity"])

