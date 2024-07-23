import datetime
from typing import Optional

from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import Field


class SustainabilityResponse(CamelCaseModel):
    fuel_consumption: Optional[float] = Field(
        None,
        title="Fuel consumption (l)",
        description="The total fuel consumption of the machine in litres",
        ge=0.0,
        examples=[1000.0],
    )
    gas_consumption: Optional[float] = Field(
        None,
        title="Gas consumption (kg)",
        description="The total gas consumption of the equipment in kilograms",
        ge=0.0,
        examples=[3000.0],
    )
    electricity_consumption: Optional[float] = Field(
        None,
        title="Electricity consumption (kWh)",
        description="The total cumulative electricity consumption of the equipment in "
        "kilowatt hours",
        ge=0.0,
        examples=[1000.0],
    )


class SustainabilityRequest(CamelCaseModel):
    id: str = Field(
        ...,
        max_length=40,
        title="ID",
        description="The unique identifier of the product",
        examples=["71b51878-8a00-11ee-b9d1-0242ac120002"],
    )
    start_time: datetime.datetime = Field(
        ...,
        title="Start time",
        description="The start time of the metric period in RFC 3339 format",
        examples=[
            datetime.datetime(2023, 4, 12, 23, 20, 50, tzinfo=datetime.timezone.utc),
        ],
    )
    end_time: datetime.datetime = Field(
        ...,
        title="End time",
        description="The end time of the metric period in RFC 3339 format",
        examples=[
            datetime.datetime(2023, 5, 12, 23, 20, 50, tzinfo=datetime.timezone.utc),
        ],
    )


DEFINITION = DataProductDefinition(
    version="0.1.0",
    title="Cargo handling equipment sustainability metrics",
    description="The power source consumption for the sustainability evaluation of the "
    "cargo handling equipment operations",
    request=SustainabilityRequest,
    response=SustainabilityResponse,
    tags=["Cargo handling equipment", "Sustainability", "Emissions"],
)
