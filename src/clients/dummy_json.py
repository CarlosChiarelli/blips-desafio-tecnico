from typing import Optional

import httpx


class DummyJsonClient:
    def __init__(self, base_url: str, http_client: httpx.AsyncClient):
        self._base_url = base_url
        self._http_client = http_client

    async def fetch_birth_date(self) -> Optional[str]:
        """Fetches the birthDate field from DummyJSON; returns None on any failure."""
        try:
            response = await self._http_client.get(self._base_url, timeout=10)
            response.raise_for_status()
            payload = response.json()
            birth_date = payload.get("birthDate")
            return birth_date if isinstance(birth_date, str) else None
        except Exception:
            return None
