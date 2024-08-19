import datetime

from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import Field


class VehicleTurnaroundTimeRequest(CamelCaseModel):
    vehicle_id: str = Field(
        ...,
        title="Vehicle identifier",
        description="Licence plate number or similar identification number of the vehicle",
        examples=["ABC-123"],
    )
    leave_time: datetime.datetime = Field(
        ...,
        title="Leave time",
        description="Time the vehicle left the facility, in RFC 3339 format",
        examples=[
            datetime.datetime(
                2024,
                7,
                15,
                14,
                45,
                00,
                tzinfo=datetime.timezone(datetime.timedelta(hours=2)),
            ),
        ],
    )


class VehicleTurnaroundTimeResponse(CamelCaseModel):
    turnaround_time: int = Field(
        ...,
        title="Turnaround time (s)",
        description="Vehicle's previous turnaround time prior to the leaving time in seconds",
        examples=[7200],
    )


DEFINITION = DataProductDefinition(
    version="0.1.0",
    title="Vehicle turnaround time",
    description="Turnaround time of a vehicle within a facility",
    request=VehicleTurnaroundTimeRequest,
    response=VehicleTurnaroundTimeResponse,
)
