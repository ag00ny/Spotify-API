from dotenv import load_dotenv
import requests, base64, os
import time

load_dotenv()

def get_spotify_token():

    __cached_token = None
    __token_expiry = 0
    if __cached_token and time.time() < __token_expiry:
        return __cached_token
    
    client_id = os.getenv('SPOTIFY_CLIENT_ID')
    client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')
    auth = base64.b64encode(f"{client_id}:{client_secret}".encode()).decode()
    headers = {
        "Authorization": f"Basic {auth}"
    }
    data = {
        "grant_type": "client_credentials"
    }
    auth_response = requests.post("https://accounts.spotify.com/api/token", headers=headers, data=data, auth=(client_id, client_secret))
    data = auth_response.json()
    _cached_token = data.get("access_token")

    __token_expiry = time.time() + data["expires_in"] - 60

    return _cached_token

def get_track(track_id):
    token = get_spotify_token()
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(
        f"https://api.spotify.com/v1/tracks/{track_id}",
        headers=headers
    )

    data =response.json()

    if "error" in data:
        return {"error": data["error"]["message"]}
    # print(data)
    # print(response.status_code)
    # return response.json()
    return{
        "title": data["name"],
        "artist": data["artists"][0]["name"],
        "album": data["album"]["name"],
        "spotify_url": data["external_urls"]["spotify"],
        "release_date": data["album"]["release_date"],
    }

def extract_spotify_id(spotify_url):
    return spotify_url.split("/track/")[1].split("?")[0]