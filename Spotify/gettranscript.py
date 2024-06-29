from urllib.parse import urlparse
from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials
from docx import Document
import os

def get_spotify_id(url):
    # Examples:
    # - https://open.spotify.com/track/5yEPktRqvIhko5QFF3aBhQ
    # - spotify:track:5yEPktRqvIhko5QFF3aBhQ
    parsed_url = urlparse(url)
    if parsed_url.scheme in {'http', 'https'} and 'spotify.com' in parsed_url.netloc:
        return parsed_url.path.split('/')[-1]
    elif parsed_url.scheme == 'spotify' and parsed_url.netloc == 'track':
        return parsed_url.path
    return None

def get_transcript(urls):
    # Load environment variables
    client_id = os.getenv("SPOTIPY_CLIENT_ID")
    client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")

    # Authenticate with Spotify API
    sp = Spotify(client_credentials_manager=SpotifyClientCredentials(client_id, client_secret))

    # Create a Word document
    doc = Document()

    for url in urls:
        track_id = get_spotify_id(url)
        if track_id:
            try:
                track = sp.track(track_id)
                track_name = track['name']
                track_artists = ', '.join(artist['name'] for artist in track['artists'])
                track_info = f'Track: {track_name}\nArtists: {track_artists}\nURL: {url}\n'
                doc.add_paragraph(track_info)
                print(f"Info for track URL: {url} retrieved successfully")
                print(f"Info: {track_info}")
            except Exception as e:
                print(f"Error retrieving info for track URL: {url}")
                print(f"Error message: {str(e)}")
        else:
            print(f"Invalid Spotify URL: {url}")

    # Save the Word document to a specific location
    doc.save('./docs/transcript.docx')
    return "transcript.docx"

# Example usage:
get_transcript(["https://open.spotify.com/track/5yEPktRqvIhko5QFF3aBhQ"])
