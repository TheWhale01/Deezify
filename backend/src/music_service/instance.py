from music_service.music_service import MusicService
from enums.services import Services
from music_service.deezer import DeezerService
from music_service.spotify import SpotifyService
import sys

def set_service(mode: Services):
	global service
	if mode == Services.DEEZER:
		service = DeezerService()
	elif mode == Services.SPOTIFY:
		service = SpotifyService()