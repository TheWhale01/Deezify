from music_service.music_service import MusicService
from enums.services import Services
from tokens.token	import Token
from tokens.spotify_token	import SpotifyToken
from fastapi import status, HTTPException, Request
from sqlalchemy.orm import Session
from crud import party as party_crud 
import os
import requests
from base64 import b64encode
import sys

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
			if response.status_code != status.HTTP_200_OK:
				raise HTTPException(status_code=response.status_code, detail=response.text)
			response_json: dict = response.json()
			username = response_json.get('display_name')
			if username is None:
				username = 'test'
			return username

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

		def init_playback(self, db: Session, party_id: int, song_id: str | None):
			party = party_crud.get_party(db, party_id)
			device_id: str = party.device_id
			token: str = party.owner.token
			endpoint: str = f'{self.base_url}/me/player/play?device_id={device_id}'
			response = None
			headers: dict = {
				'Authorization': f'{self.token.token_type} {token}'
			}
			if song_id:
				data: dict = {
					"uris": [
						f"spotify:track:{song_id}"
					],
					"position_ms": 0,
				}
				response = requests.put(url=endpoint, headers=headers, json=data)
			else:
				response = requests.put(url=endpoint, headers=headers)
			if response.status_code != status.HTTP_200_OK:
				raise HTTPException(status_code=response.status_code, detail=response.text)

		def add_to_queue(self, track_id: str, device_id: str, token: str) -> None:
			uri: str = f'spotify:track:{track_id}'
			endpoint: str = f'{self.base_url}/me/player/queue?device_id={device_id}&uri={uri}'
			headers: dict = {
				'Authorization': f'{self.token.token_type} {token}'
			}
			response = requests.post(url=endpoint, headers=headers)
			if response.status_code != status.HTTP_200_OK:
				raise HTTPException(
					status_code=response.status_code,
					detail=response.text
				)

		def pause(self, device_id: str):
			endpoint: str = f'{self.base_url}/me/player/pause?device_id={device_id}'
			response = requests.put(url=endpoint, headers=self.headers)
			if response.status_code != status.HTTP_200_OK:
				raise HTTPException(status_code=response.status_code, detail=response.text)
