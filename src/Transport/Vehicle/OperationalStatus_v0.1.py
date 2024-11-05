from datetime import datetime
from typing import Optional

from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import Field


class Location(CamelCaseModel):
    latitude: float = Field(
        ...,
        title="Latitude (°)",
        description="The latitude coordinate in decimal degrees.",
        gte=-90,
        lte=90,
        examples=[60.192059],
    )
    longitude: float = Field(
        ...,
        title="Longitude (°)",
        description="The longitude coordinate in decimal degrees.",
        gte=-180,
        lte=180,
        examples=[24.945831],
    )


class OperationalStatusRequest(CamelCaseModel):
    id: str = Field(
        ...,
        title="ID",
        description="The unique identifier of the vehicle.",
        max_length=40,
        examples=["71b51878-8a00-11ee-b9d1-0242ac120002"],
    )
    time: Optional[datetime] = Field(
        None,
        title="Time",
        description="Request the vehicle's status information at or before this given time, in RFC 3339 format. If empty, provide latest value.",
        examples=[datetime.fromisoformat("2023-04-12T23:20:50Z")],
    )


class OperationalStatusResponse(CamelCaseModel):
    time: Optional[datetime] = Field(
        None,
        title="Time",
        description="The time the status of the vehicle was recorded, in RFC 3339 format.",
        examples=[datetime.fromisoformat("2023-04-12T23:20:50Z")],
    )
    speed: Optional[float] = Field(
        None,
        title="Speed (km/h)",
        description="The speed of the vehicle in kilometers per hour.",
        examples=[60.0],
    )
    fuel_level: Optional[float] = Field(
        None,
        title="Fuel level (%)",
        description="The percent of fuel left as a number value between 0 and 100.",
        gte=0,
        lte=100,
        examples=[75.0],
    )
    charge_level: Optional[float] = Field(
        None,
        title="Charge level (%)",
        description="The percent of battery capacity left as a number value between 0 and 100.",
        gte=0,
        lte=100,
        examples=[75.0],
    )
    location: Optional[Location] = Field(
        None,
        title="Location",
        description="The location in GPS coordinates.",
    )


DEFINITION = DataProductDefinition(
    version="0.1.0",
    title="Transport vehicle operational status",
    description="General operational status data of a transport vehicle.",
    tags=["Road transport", "Logistics", "Truck"],
    request=OperationalStatusRequest,
    response=OperationalStatusResponse,
)
