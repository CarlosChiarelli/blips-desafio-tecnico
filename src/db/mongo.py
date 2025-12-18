from collections.abc import Callable
from typing import Optional

from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase


class MongoClientManager:
    def __init__(self, uri: str, db_name: str):
        self._uri = uri
        self._db_name = db_name
        self._client: Optional[AsyncIOMotorClient] = None

    async def connect(self) -> AsyncIOMotorDatabase:
        # Motor client creation is non-blocking; keeping the method async keeps the FastAPI lifespan consistent.
        self._client = AsyncIOMotorClient(self._uri)
        return self.database

    @property
    def database(self) -> AsyncIOMotorDatabase:
        if not self._client:
            raise RuntimeError("Mongo client is not initialized")
        return self._client[self._db_name]

    async def disconnect(self) -> None:
        if self._client:
            self._client.close()
            self._client = None


MongoDependency = Callable[[], AsyncIOMotorDatabase]
