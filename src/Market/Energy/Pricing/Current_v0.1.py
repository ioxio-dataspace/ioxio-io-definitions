import datetime

from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import Field


class EnergyPriceRequest(CamelCaseModel):
    countryCode: str = Field(
        ...,
        title="Country code (ISO 3166-1 alpha 3)",
        description="The country of the energy price in ISO 4155-1 alpha-3 format",
        examples=["FIN"],
    )


class EnergyPriceResponse(CamelCaseModel):
    price: float = Field(
        ...,
        title="Price (€/MWh)",
        description="Current market price in euros per megawatt hour",
        examples=["29.12"],
    )
    timestamp: datetime.datetime = Field(
        ...,
        title="Timestamp (RFC 3339)",
        description="Time of the request in RFC 3339 format",
        examples=[""],
    )


DEFINITION = DataProductDefinition(
    version="0.1.1",
    title="Current energy price",
    description="Current energy price in euros / MWh in a specific country",
    request=EnergyPriceRequest,
    response=EnergyPriceResponse,
)
