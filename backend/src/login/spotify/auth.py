import os
import sys
import requests
from utils import generate_random_string
from fastapi import APIRouter, HTTPException, status, Request
from fastapi.responses import RedirectResponse
from tokens.spotify_token import SpotifyToken 
from ..music_service import MusicService
from fastapi.security.oauth2 import OAuth2AuthorizationCodeBearer
from base64 import b64encode

router = APIRouter(
    prefix='/login/spotify'
)

class SpotifyService(MusicService):
    def __init__(self):
        super().__init__(
            token_url='https://accounts.spotify.com/api/token',
            auth_url=f'https://accounts.spotify.com/authorize'
        )

    def callback(self, request: Request) -> RedirectResponse:
        code: str | None = request.query_params.get('code')
        state: str | None = request.query_params.get('state')
        if state is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='state mismatch')
        to_encode: bytes = f'{os.getenv("SPOTIFY_CLIENT_ID")}:{os.getenv("SPOTIFY_CLIENT_SECRET")}'.encode()
        data = {
            'code': code,
            'redirect_uri': os.getenv('SPOTIFY_CALLBACK_URL'),
            'grant_type': 'authorization_code'
        }
        headers = {
            'content-type': 'application/x-www-form-urlencoded',
            'Authorization': f'Basic {b64encode(to_encode).decode()}'
        }
        response = requests.post(self.token_url, data=data, headers=headers, json=True)
        if response.status_code != status.HTTP_200_OK:
            raise HTTPException(status_code=response.status_code, detail=response.text)
        print(response.json(), file=sys.stderr)
        token = SpotifyToken(**(response.json()))
        response = RedirectResponse(url=os.getenv('FRONTEND_URI'))
        response.set_cookie(key='access_token', value=token.access_token, httponly=True, samesite='lax')
        return response

sp_service = SpotifyService()

oauth2_scheme = OAuth2AuthorizationCodeBearer(authorizationUrl=sp_service.auth_url, tokenUrl=sp_service.token_url)

@router.get('/')
def login():
    state = generate_random_string(32)
    url = (
        f"{sp_service.auth_url}?response_type=code"
        f"&client_id={os.getenv('SPOTIFY_CLIENT_ID')}"
        f"&scope={os.getenv('SPOTIFY_SCOPES')}"
        f"&redirect_uri={os.getenv('SPOTIFY_CALLBACK_URL')}"
        f"&state={state}"
    )
    response = sp_service.login(url)
    return response


@router.get('/callback')
def callback(request: Request):
    # Before returning, store credentials in database
    return sp_service.callback(request)
