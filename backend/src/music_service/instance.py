from music_service.music_service import MusicService
from enums.services import Services
from music_service.deezer import DeezerService
from music_service.spotify import SpotifyService

def set_service(mode: int):
	global service
	if mode == Services.DEEZER:
		service = DeezerService()
	elif mode == Services.SPOTIFY:
		service = SpotifyService()
