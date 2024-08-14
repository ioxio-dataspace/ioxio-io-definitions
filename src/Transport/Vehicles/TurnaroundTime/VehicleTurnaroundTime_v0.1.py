import datetime

from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import Field


class VehicleTurnaroundTimeRequest(CamelCaseModel):
    vehicleId: str = Field(
        ...,
        title="Vehicle identifier",
        description="Licence plate number or similar identification number of the vehicle",
        examples=["123-ABC"],
    )
    leaveTime: datetime.datetime = Field(
        ...,
        title="Leaving time",
        description="Time the vehicle left the facility, in RFC 3339 format",
        examples=[
            datetime.datetime(2024, 7, 15, 14, 45, 00, tzinfo=datetime.timezone.utc),
        ],
    )


class VehicleTurnaroundTimeResponse(CamelCaseModel):
    turnaroundTime: int = Field(
        ...,
        title="Turnaround time (s)",
        description="Vehicle's previous turnaround time prior to the leaving time in seconds",
        examples=["7200"],
    )


DEFINITION = DataProductDefinition(
    version="0.1.0",
    title="Vehicle turnaround time",
    description="Turnaround time of a vehicle within a facility",
    request=VehicleTurnaroundTimeRequest,
    response=VehicleTurnaroundTimeResponse,
)
