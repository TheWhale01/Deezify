from abc import ABC

class Token(ABC):
    def __init__(self, access_token: str):
        self.access_token: str = access_token
