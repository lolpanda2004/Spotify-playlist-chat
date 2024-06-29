# Spotify Playlist AI Chat

Quickly summarizes the contents of Spotify tracks in a public playlist and answers questions based on it.


## Running the tool

1. Create a `.env` file in the root directory of the project. Replace the placeholders with your actual keys:

   ```bash
   OPENAI_API_TOKEN={OPENAI_API_KEY}
   SPOTIPY_CLIENT_ID={your_spotify_client_id}
   SPOTIPY_CLIENT_SECRET={your_spotify_client_secret}
   EMBEDDER_LOCATOR=text-embedding-ada-002
   EMBEDDING_DIMENSION=1536
   MODEL_LOCATOR=gpt-3.5-turbo
   MAX_TOKENS=200
   TEMPERATURE=0.0


### Prerequisites

#### Python Installation

Make sure that Python 3.10 or above is installed on your machine.

- [Download Python](https://www.python.org/downloads/)

#### Pip Installation

Download and Install Pip to manage project packages.

- [Install Pip](https://pip.pypa.io/en/stable/installation/)

#### OpenAI API Key

Create an OpenAI account and generate a new API Key. To access the OpenAI API, follow these steps:

- [Create OpenAI API Key](https://openai.com/product)

#### Spotify Developer Account

Create a Spotify Developer account and generate a new Client ID and Client Secret. To access the Spotify API, follow these steps:

- [Create Spotify Developer Account](https://developer.spotify.com/dashboard/applications)

Follow these steps to install and get started with the application.

