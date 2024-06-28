import datetime
from enum import Enum
from typing import List, Optional

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


class CargoHandlingEquipmentOperationalStatusResponse(CamelCaseModel):
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
        examples=[0.0],
    )
    gas_level: Optional[float] = Field(
        None,
        title="Gas level",
        description="The percent of gas left in the tank (%)",
        examples=[0.0],
    )
    state_of_charge: Optional[float] = Field(
        None,
        title="State of charge",
        description="The percent of the remaining capacity of the equipment batteries "
        "(%)",
        examples=[0.0],
    )
    location: Location = Field(
        ...,
        title="Location",
        description="The location of the equipment in GPS coordinates",
    )


class CargoHandlingEquipmentOperationalStatusRequest(CamelCaseModel):
    id: str = Field(
        ...,
        max_length=40,
        title="Id",
        description="The unique identifier of the product",
        examples=["71b51878-8a00-11ee-b9d1-0242ac120002"],
    )
    status_time: datetime.datetime = Field(
        ...,
        title="Status time",
        description="The time of the equipment's status in the desired country in RFC "
        "3339 format following ISO 8601",
        examples=[datetime.datetime(2023, 4, 12, 23, 20, 50, 520000)],
    )


DEFINITION = DataProductDefinition(
    version="0.1.0",
    title="Cargo Handling Equipment Operational Status",
    description="General operational status data of a cargo handling equipment "
    "operating in a port",
    request=CargoHandlingEquipmentOperationalStatusRequest,
    response=CargoHandlingEquipmentOperationalStatusResponse,
    tags=["Cargo handling equipment", "Port", "Freight terminal", "Logistics"],
)
