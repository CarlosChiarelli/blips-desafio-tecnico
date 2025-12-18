from typing import List, Optional

from src.clients.dummy_json import DummyJsonClient
from src.repositories.lead_repository import LeadRepository
from src.schemas.lead import LeadCreate, LeadResponse


class LeadService:
    def __init__(self, repository: LeadRepository, dummy_client: DummyJsonClient):
        self._repository = repository
        self._dummy_client = dummy_client

    async def create_lead(self, payload: LeadCreate) -> LeadResponse:
        birth_date = await self._dummy_client.fetch_birth_date()
        lead_dict = payload.model_dump()
        lead_dict["birth_date"] = birth_date
        created = await self._repository.create(lead_dict)
        return LeadResponse.model_validate(created)

    async def list_leads(self) -> List[LeadResponse]:
        leads = await self._repository.list_all()
        return [LeadResponse.model_validate(lead) for lead in leads]

    async def get_lead(self, lead_id: str) -> Optional[LeadResponse]:
        lead = await self._repository.get_by_id(lead_id)
        return LeadResponse.model_validate(lead) if lead else None
