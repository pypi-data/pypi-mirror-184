from typing import List, Optional

from howlongtobeatpy import HowLongToBeat
from howlongtobeatpy.HTMLRequests import SearchModifiers


class HowLongToBeatClient:
    def __init__(self) -> None:
        self.client = HowLongToBeat()

    async def search(self, query: str, include_DLCs: Optional[bool] = True) -> List:
        if include_DLCs:
            search_modifiers = SearchModifiers.NONE
        else:
            search_modifiers = SearchModifiers.HIDE_DLC
        results = self.client.search(query, search_modifiers)
        return results  # type: ignore

    async def search_DLCs(self, query: str) -> dict:
        results = self.client.search(query, SearchModifiers.ISOLATE_DLC)
        return results  # type: ignore
