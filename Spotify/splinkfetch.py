import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os

def fetch_track_urls(playlist_url):
    # Load environment variables
    client_id = os.getenv("SPOTIPY_CLIENT_ID")
    client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")

    # Authenticate with Spotify API
    sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id, client_secret))

    # Extract playlist ID from URL
    playlist_id = playlist_url.split("/")[-1].split("?")[0]

    # Retrieve track details from the playlist
    results = sp.playlist_tracks(playlist_id)
    track_urls = [item['track']['external_urls']['spotify'] for item in results['items']]

    return track_urls
