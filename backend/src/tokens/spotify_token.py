from tokens.token import Token

class SpotifyToken(Token):
    def __init__(self, access_token: str, token_type: str, expires_in: int, refresh_token: str, scope: str):
        super().__init__(access_token, expires_in)
        self.token_type: str = token_type
        self.refresh_token: str = refresh_token 
        self.scope: str = scope
