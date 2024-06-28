import datetime
from enum import Enum
from typing import Optional

from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import Field


class OperationalState(str, Enum):
    RUNNING = "running"
    IDLE = "idle"
    CHARGING = "charging"
    REFILLING = "refilling"


class Location(CamelCaseModel):
    latitude: Optional[float] = Field(
        None,
        title="Latitude",
        description="The latitude coordinate of the equipment location",
        ge=-90.0,
        le=90.0,
        examples=[60.192059],
    )
    longitude: Optional[float] = Field(
        None,
        title="Longitude",
        description="The longitude coordinate of the equipment location",
        ge=-180.0,
        le=180.0,
        examples=[24.945831],
    )


class OperationalStatusResponse(CamelCaseModel):
    time: Optional[datetime.datetime] = Field(
        None,
        title="Time",
        description="The time of the equipment's status in RFC 3339 format following "
        "ISO 8601.",
        examples=[
            datetime.datetime(2023, 4, 12, 23, 20, 50, tzinfo=datetime.timezone.utc),
        ],
    )
    operational_state: OperationalState = Field(
        ...,
        title="Operational state",
        description="The state of operation of the equipment",
        examples=[OperationalState.RUNNING],
    )
    fuel_level: Optional[float] = Field(
        None,
        title="Fuel level",
        description="The percent of fuel left in the tank (%)",
        ge=0.0,
        le=100.0,
        examples=[75.0],
    )
    gas_level: Optional[float] = Field(
        None,
        title="Gas level",
        description="The percent of gas left in the tank (%)",
        ge=0.0,
        le=100.0,
        examples=[75.0],
    )
    charge_level: Optional[float] = Field(
        None,
        title="Charge level",
        description="The percent of the remaining capacity of the equipment batteries "
        "(%)",
        ge=0.0,
        le=100.0,
        examples=[75.0],
    )
    location: Location = Field(
        ...,
        title="Location",
        description="The location of the equipment in GPS coordinates",
    )


class OperationalStatusRequest(CamelCaseModel):
    id: str = Field(
        ...,
        max_length=40,
        title="Id",
        description="The unique identifier of the product",
        examples=["71b51878-8a00-11ee-b9d1-0242ac120002"],
    )
    time: Optional[datetime.datetime] = Field(
        None,
        title="Time",
        description="The time of the equipment's status in RFC 3339 format following "
        "ISO 8601. If data on the requested time doesn't exist return data with the "
        "closest time. If the time is not given return data with the latest available "
        "time.",
        examples=[
            datetime.datetime(2023, 4, 12, 23, 20, 50, tzinfo=datetime.timezone.utc),
        ],
    )


DEFINITION = DataProductDefinition(
    version="0.1.0",
    title="Cargo Handling Equipment Operational Status",
    description="General operational status data of a cargo handling equipment "
    "operating in a port",
    request=OperationalStatusRequest,
    response=OperationalStatusResponse,
    tags=["Cargo handling equipment", "Port", "Freight terminal", "Logistics"],
)
