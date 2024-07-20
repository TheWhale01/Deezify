from abc import ABC, abstractmethod
from fastapi import HTTPException, status, Request
from fastapi.responses import RedirectResponse

class MusicService(ABC):
    def __init__(self, token_url: str, auth_url: str):
        self.token_url = token_url
        self.auth_url = auth_url

    def login(self, url: str):
        # response = requests.get(url)
        # if response.status_code != status.HTTP_200_OK:
        #     raise HTTPException(status_code=response.status_code, detail=response.text)
        # return response
        return {'url': url}

    @abstractmethod
    def callback(self, request: Request) -> RedirectResponse:
        pass
