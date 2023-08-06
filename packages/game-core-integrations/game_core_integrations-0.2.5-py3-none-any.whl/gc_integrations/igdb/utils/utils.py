import aiohttp
from gc_integrations.constants import IGDB_AUTH_URL

from gc_integrations.igdb.models.auth_models import IGDBAuth


async def get_igdb_auth_token(client_id: str, client_secret: str) -> IGDBAuth:
    """Get IGDB auth token from environment variable."""
    query_params = {
        "client_id": client_id,
        "client_secret": client_secret,
        "grant_type": "client_credentials",
    }

    async with aiohttp.ClientSession() as client:
        request = await client.post(IGDB_AUTH_URL, params=query_params)
        result = await request.json()
        return IGDBAuth(**result)
