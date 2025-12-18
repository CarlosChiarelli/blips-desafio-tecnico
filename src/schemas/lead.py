from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class LeadBase(BaseModel):
    name: str = Field(..., example="Ada Lovelace")
    email: EmailStr = Field(..., example="ada@example.com")
    phone: str = Field(..., example="+55 11 99999-9999")


class LeadCreate(LeadBase):
    pass


class LeadResponse(LeadBase):
    id: str = Field(..., example="65f15f0f5f0a5c2f0a5c2f0a")
    birth_date: Optional[str] = Field(None, example="1998-02-05")
