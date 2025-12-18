from fastapi import APIRouter, Depends, HTTPException, Request, status

from src.clients.dummy_json import DummyJsonClient
from src.repositories.lead_repository import LeadRepository
from src.schemas.lead import LeadCreate, LeadResponse
from src.services.lead_service import LeadService

router = APIRouter()


def get_lead_service(request: Request) -> LeadService:
    db = request.app.state.db
    dummy_client: DummyJsonClient = request.app.state.dummy_client
    repository = LeadRepository(db)
    return LeadService(repository, dummy_client)


@router.post("", response_model=LeadResponse, status_code=status.HTTP_201_CREATED)
async def create_lead(payload: LeadCreate, service: LeadService = Depends(get_lead_service)):
    return await service.create_lead(payload)


@router.get("", response_model=list[LeadResponse])
async def list_leads(service: LeadService = Depends(get_lead_service)):
    return await service.list_leads()


@router.get("/{lead_id}", response_model=LeadResponse)
async def get_lead(lead_id: str, service: LeadService = Depends(get_lead_service)):
    lead = await service.get_lead(lead_id)
    if not lead:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Lead not found")
    return lead
