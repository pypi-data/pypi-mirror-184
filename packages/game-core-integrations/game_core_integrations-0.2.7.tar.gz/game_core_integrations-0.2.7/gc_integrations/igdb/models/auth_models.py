from pydantic import BaseModel


class IGDBAuth(BaseModel):
    access_token: str
    expires_in: int  # In miliseconds
    token_type: str
