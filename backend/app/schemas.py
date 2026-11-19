# This file defines the Pydantic models for validating and structuring API data

from pydantic import BaseModel, ConfigDict


# PROVIDER SCHEMA
class ProviderResponse(BaseModel):

    provider_id: int
    provider_name: str

    model_config = ConfigDict(from_attributes=True)
