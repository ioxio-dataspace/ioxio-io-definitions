import datetime

from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import Field


class VehicleTurnaroundTimeRequest(CamelCaseModel):
    licencePlate: str = Field(
        ...,
        title="Licence plate",
        description="Licence plate number of the vehicle",
        examples=["123-ABC"],
    )
    entryTime: datetime.datetime = Field(
        ...,
        title="Entry time (RFC 3339)",
        description="Entry time in RFC 3339 format",
        examples=[
            datetime.datetime(2023, 4, 12, 23, 20, 50, tzinfo=datetime.timezone.utc),
        ],
    )


class VehicleTurnaroundTimeResponse(CamelCaseModel):
    turnaroundTime: int = Field(
        ...,
        title="Turnaround time (s)",
        description="Turnaround time of the vehicle in seconds",
        examples=["31752000"],
    )


DEFINITION = DataProductDefinition(
    version="0.1.0",
    title="Vehicle turnaround time",
    description="Turnaround time of a vehicle within a facility",
    request=VehicleTurnaroundTimeRequest,
    response=VehicleTurnaroundTimeResponse,
)
