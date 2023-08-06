from typing import Any, List, Mapping, Optional, Dict

from aiohttp import ClientSession
from gc_integrations.constants import IGDB_API_URL


class IGDBClient:
    def __init__(self, client_id: str, auth_token: str):
        """Instantiates the IGDBClient class.

        Args:
            client_id (str): Your app client id obtained from Twitch Developers.
            auth_token (str): The bearer token used for authentication.
            The helper function "get_bearer_token" can be used to obtain this token.
        """

        self.client_id = client_id
        self.auth_token = auth_token

        self.client = self._build_async_client()

    def _build_async_client(self) -> ClientSession:
        api_url = IGDB_API_URL
        headers = {
            "Client-ID": self.client_id,
            "Authorization": f"Bearer {self.auth_token}",
        }
        return ClientSession(base_url=api_url, headers=headers)

    @staticmethod
    def _map_to_query(query_dict: Optional[Dict[str, Any]]) -> str:
        """Maps a dictionary to a raw apicalypse query. Includes all fields by default."""

        # Return all fields by default
        if query_dict is None:
            query_dict = {"fields": "*"}

        elif "fields" not in query_dict.keys():
            query_dict.update({"fields": "*"})

        query_list = [f"{k} {str(v)};" for k, v in query_dict.items()]
        query = " ".join(query_list)
        return query

    async def _send_request(self, endpoint: str, query_data: Optional[str]) -> list:
        request = await self.client.post(endpoint, content=query_data)
        return await request.json()

    async def make_request(
        self, endpoint: str, query: Optional[Dict[str, Any]] = None
    ) -> list:

        query_str = self._map_to_query(query_dict=query)
        result = await self._send_request(endpoint, query_str)
        return result

    async def resolve_similars(self, game_ids: List[int]):
        """Resolves similar games for a list of game ids.

        Args:
            game_ids (list): A list of game ids.

        Returns:
            list: A list of similar games.
        """

        endpoint = "games"
        game_ids_str = ", ".join([str(game_id) for game_id in game_ids])
        query = {"fields": "*", "where": f"id = ({game_ids_str});"}
        result = await self.make_request(endpoint, query)
        return result
