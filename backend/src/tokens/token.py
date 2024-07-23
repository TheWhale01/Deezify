from abc import ABC

class Token(ABC):
    def __init__(self, access_token: str, expires_in: int):
        self.access_token: str = access_token
        self.expires_in: int = expires_in
