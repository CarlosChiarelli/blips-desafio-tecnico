from typing import Any, Dict, List, Optional

from bson import ObjectId
from bson.errors import InvalidId
from motor.motor_asyncio import AsyncIOMotorDatabase


class LeadRepository:
    def __init__(self, db: AsyncIOMotorDatabase):
        self._collection = db.get_collection("leads")

    async def create(self, lead_data: Dict[str, Any]) -> Dict[str, Any]:
        result = await self._collection.insert_one(lead_data)
        lead_data["id"] = str(result.inserted_id)
        return lead_data

    async def list_all(self) -> List[Dict[str, Any]]:
        leads: List[Dict[str, Any]] = []
        cursor = self._collection.find()
        async for document in cursor:
            leads.append(self._normalize(document))
        return leads

    async def get_by_id(self, lead_id: str) -> Optional[Dict[str, Any]]:
        try:
            object_id = ObjectId(lead_id)
        except (InvalidId, TypeError):
            return None

        document = await self._collection.find_one({"_id": object_id})
        return self._normalize(document) if document else None

    def _normalize(self, document: Dict[str, Any]) -> Dict[str, Any]:
        normalized = {**document}
        normalized["id"] = str(normalized.pop("_id"))
        return normalized
