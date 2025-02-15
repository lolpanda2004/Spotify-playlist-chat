import os
import streamlit as st
import requests
from dotenv import load_dotenv
import splinkfetch as sf
import gettranscript as gt

# Load environment variables
load_dotenv()
api_host = os.environ.get("HOST", "api")
api_port = int(os.environ.get("PORT", 8080))

# Streamlit UI elements
st.title("Spotify Playlist AI Chat")

sp_url = st.text_input("Enter Spotify playlist link")

question = st.text_input(
    "Search for something",
    placeholder="What data are you looking for?"
)

if sp_url:
    track_urls = sf.fetch_track_urls(sp_url)
    gt.get_transcript(track_urls)

if question:
    url = f'http://{api_host}:{api_port}/'
    data = {"query": question}

    response = requests.post(url, json=data)

    if response.status_code == 200:
        st.write("### Answer")
        st.write(response.json())
    else:
        st.error(f"Failed to send data to Pathway API. Status code: {response.status_code}")
