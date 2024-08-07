from music_service.music_service import MusicService
from enums.services import Services
from tokens.token	import Token
from tokens.spotify_token	import SpotifyToken
from fastapi import status, HTTPException, Request
import os
import requests
from base64 import b64encode

class	SpotifyService(MusicService):
		def __init__(self):
			super().__init__(
				token_url='https://accounts.spotify.com/api/token',
				auth_url=f'https://accounts.spotify.com/authorize',
				base_url='https://api.spotify.com/v1',
				service=Services.SPOTIFY
			)
			self.token: SpotifyToken | None =	None
			self.headers:	dict = {}

		def callback(self, request: Request) -> Token:
			code:	str |	None = request.query_params.get('code')
			state: str | None	=	request.query_params.get('state')
			if state is None:
				raise	HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='state mismatch')
			to_encode: bytes = f'{os.getenv("SPOTIFY_CLIENT_ID")}:{os.getenv("SPOTIFY_CLIENT_SECRET")}'.encode()
			data = {
				'code': code,
				'redirect_uri': os.getenv('SPOTIFY_CALLBACK_URL'),
				'grant_type':	'authorization_code'
			}
			headers =	{
				'content-type': 'application/x-www-form-urlencoded',
				'Authorization': f'Basic {b64encode(to_encode).decode()}'
			}
			response = requests.post(self.token_url, data=data, headers=headers, json=True)
			if response.status_code != status.HTTP_200_OK:
				raise	HTTPException(status_code=response.status_code, detail=response.text)
			self.token = SpotifyToken(**(response.json()))
			self.set_header()
			return self.token

		def set_header(self):
			if self.token	is None:
				raise	HTTPException(status_code=500, detail='token is not set')
			self.headers = {
				'Authorization': f'{self.token.token_type} {self.token.access_token}'
			}

		def get_user(self):
			url: str = self.base_url + '/me'
			response = requests.get(url, headers=self.headers)
			return response.json()['display_name']

		def search(self, query: str):
			url: str = self.base_url + f'/search?q={query}&type=track'
			response = requests.get(url, headers=self.headers)
			if response.status_code != status.HTTP_200_OK:
				raise HTTPException(status_code=response.status_code, detail=response.text)
			results: dict = {'data': []}
			for item in response.json()['tracks']['items']:
				results['data'].append({
					'id': item['id'],
					'title': item['name'],
					'artist': item['artists'][0]['name'],
					'cover': item['album']['images'][1]['url']
				})
			return results

		def get_track(self, track_id: str) -> dict:
			endpoint: str = f'{self.base_url}/tracks/{track_id}'
			response = requests.get(endpoint, headers=self.headers)
			if response.status_code != status.HTTP_200_OK:
				raise HTTPException(
					status_code=response.status_code,
					detail=response.text
				)
			track: dict = {}
			track.update({'title': response.json()['name']})
			track.update({'artist': response.json()['artists'][0]['name']})
			track.update({'cover': response.json()['album']['images'][0]['url']})
			return track

		def init_playback(self, device_id: str, song_id: str):
			endpoint: str = f'{self.base_url}/me/player/play?device_id={device_id}'
			data: dict = {
				"uris": [
					f"spotify:track:{song_id}"
				],
				"position_ms": 0,
			}
			response = requests.put(url=endpoint, headers=self.headers, json=data)
			if response.status_code != status.HTTP_200_OK:
				raise HTTPException(status_code=response.status_code, detail=response.text)
			return response
