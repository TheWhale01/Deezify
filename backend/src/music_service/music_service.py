from abc import ABC, abstractmethod
from fastapi import Request
from tokens.token import Token

class MusicService(ABC):
	def __init__(self, token_url: str, auth_url: str, base_url: str, service: int):
		self.token_url = token_url
		self.auth_url = auth_url
		self.base_url: str = base_url
		self.service: int = service


	def login(self, url: str):
		return {'url': url}

	@abstractmethod
	def callback(self, request: Request) -> Token:
		pass

	@abstractmethod
	def get_user(self) -> dict:
		pass

	@abstractmethod
	def search(self, query: str) -> dict:
		pass

	@abstractmethod
	def get_track(self, track_id: str) -> dict:
		pass

	@abstractmethod
	def add_to_queue(self, track_id: str, device_id: str, token: str) -> None: 
		pass
