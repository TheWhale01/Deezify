from tokens.token import Token

class DeezerToken(Token):
    def __init__(self, access_token: str, expires: int):
        super().__init__(access_token, expires)
