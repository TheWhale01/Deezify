import os
import sys
import requests
from fastapi import HTTPException, status, Request
from music_service.music_service import MusicService
from tokens.token import Token
from tokens.deezer_token import DeezerToken
from enums.services import Services

class DeezerService(MusicService):
	def __init__(self):
		super().__init__(
			auth_url=f'https://connect.deezer.com/oauth/auth.php?app_id={os.getenv("DEEZER_APP_ID")}&redirect_uri={os.getenv("DEEZER_CALLBACK_URL")}&perms={os.getenv("DEEZER_PERMS")}',
			token_url=f'https://connect.deezer.com/oauth/access_token.php?app_id={os.getenv("DEEZER_APP_ID")}&secret={os.getenv("DEEZER_SECRET_KEY")}&output=json',
			base_url='https://api.deezer.com',
			service=Services.DEEZER
		)
		self.token: DeezerToken | None = None

	def callback(self, request: Request) -> Token:
		code : str | None = request.query_params.get('code')
		if code is None:
			raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="token not set")
		self.token_url += f'&code={code}'
		response = requests.get(self.token_url)
		if response.status_code != status.HTTP_200_OK:
			raise HTTPException(status_code=response.status_code, detail=response.text)
		self.token = DeezerToken(**(response.json()))
		return self.token

	def get_user(self):
		if self.token is None:
			raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="token not set")
		response = requests.get(self.base_url + f'/user/me?access_token={self.token.access_token}')
		if response.status_code != status.HTTP_200_OK:
			raise HTTPException(status_code=response.status_code, detail=response.text)
		return response.json()['name']

	def search(self, query: str) -> dict:
		if self.token is None:
			raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="token not set")
		response = requests.get(self.base_url + f'/search?q={query}&access_token={self.token.access_token}&output=json')
		if response.status_code != status.HTTP_200_OK:
			raise HTTPException(status_code=response.status_code, detail=response.text)
		results: dict = {'data': []}
		for item in response.json()['data']:
			results['data'].append({
				'id': item['id'],
				'title': item['title'],
				'artist': item['artist']['name'],
				'cover': item['album']['cover_medium']
			})
		return results

	def get_track(self, track_id: str) -> dict:
		if self.token is None:
			raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="token not set")
		endpoint: str = f'{self.base_url}/track/{track_id}?access_token={self.token.access_token}'
		response = requests.get(endpoint)
		if response.status_code != status.HTTP_200_OK:
			raise HTTPException(
				status_code=response.status_code,
				detail=response.text
			)
		track: dict = {}
		track.update({'title': response.json()['title']})
		track.update({'artist': response.json()['artist']['name']})
		track.update({'cover': response.json()['album']['cover_big']})
		return track

	def add_to_queue(self, track_id: str, device_id: str) -> None:
		print(track_id)
		print(device_id)
