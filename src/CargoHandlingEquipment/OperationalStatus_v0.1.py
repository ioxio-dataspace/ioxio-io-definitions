import datetime
from enum import Enum
from typing import Optional

from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import Field


class OperationalState(str, Enum):
    DRIVING = "driving"
    IDLE = "idle"
    CHARGING = "charging"
    REFILLING = "refilling"


class Location(CamelCaseModel):
    latitude: float = Field(
        ...,
        title="Latitude (°)",
        description="The latitude coordinate in decimal degrees",
        ge=-90.0,
        le=90.0,
        examples=[60.192059],
    )
    longitude: float = Field(
        ...,
        title="Longitude (°)",
        description="The longitude coordinate in decimal degrees",
        ge=-180.0,
        le=180.0,
        examples=[24.945831],
    )


class OperationalStatusResponse(CamelCaseModel):
    time: Optional[datetime.datetime] = Field(
        None,
        title="Time",
        description="The time the status of the equipment was recorded, in RFC 3339 format",
        examples=[
            datetime.datetime(2023, 4, 12, 23, 20, 50, tzinfo=datetime.timezone.utc),
        ],
    )
    operational_state: OperationalState = Field(
        ...,
        title="Operational state",
        description="The state of operation",
        examples=[OperationalState.DRIVING],
    )
    fuel_level: Optional[float] = Field(
        None,
        title="Fuel level (%)",
        description="The percent of fuel left as a number value between 0 and 100",
        ge=0.0,
        le=100.0,
        examples=[75.0],
    )
    gas_level: Optional[float] = Field(
        None,
        title="Gas level (%)",
        description="The percent of gas left as a number value between 0 and 100",
        ge=0.0,
        le=100.0,
        examples=[75.0],
    )
    charge_level: Optional[float] = Field(
        None,
        title="Charge level (%)",
        description="The percent of battery capacity left as a number value between 0 and 100",
        ge=0.0,
        le=100.0,
        examples=[75.0],
    )
    location: Optional[Location] = Field(
        None,
        title="Location",
        description="The location in GPS coordinates",
    )


class OperationalStatusRequest(CamelCaseModel):
    id: str = Field(
        ...,
        max_length=40,
        title="ID",
        description="The unique identifier of the product",
        examples=["71b51878-8a00-11ee-b9d1-0242ac120002"],
    )
    time: Optional[datetime.datetime] = Field(
        None,
        title="Time",
        description="Request the equipment's status information at or before this given time, in RFC 3339 format. If empty, provide latest value.",
        examples=[
            datetime.datetime(2023, 4, 12, 23, 20, 50, tzinfo=datetime.timezone.utc),
        ],
    )


DEFINITION = DataProductDefinition(
    version="0.1.0",
    title="Cargo handling equipment operational status",
    description="General operational status data of a cargo handling equipment "
    "operating in a port",
    request=OperationalStatusRequest,
    response=OperationalStatusResponse,
    tags=["Cargo handling equipment", "Port", "Freight terminal", "Logistics"],
)
