import datetime
from typing import List, Optional

from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import Field


class TurnaroundTime(CamelCaseModel):
    vehicle_id: str = Field(
        ...,
        title="Vehicle identifier",
        description="Licence plate number or similar identification number of the "
        "vehicle.",
        max_length=40,
        examples=["ABC-123"],
    )
    vehicle_type: Optional[str] = Field(
        None,
        title="Vehicle type",
        description="The type of the vehicle.",
        max_length=40,
        examples=["truck"],
    )
    entry_time: datetime.datetime = Field(
        ...,
        title="Entry time",
        description="The time when the vehicle entered the facility.",
        examples=[
            datetime.datetime(2023, 4, 12, 22, 20, 50, tzinfo=datetime.timezone.utc)
        ],
    )
    leave_time: Optional[datetime.datetime] = Field(
        None,
        title="Leave time",
        description="The time when the vehicle left the facility.",
        examples=[
            datetime.datetime(2023, 4, 12, 23, 20, 50, tzinfo=datetime.timezone.utc)
        ],
    )
    turnaround_time: int = Field(
        ...,
        title="Turnaround time (s)",
        description="Turnaround time of the vehicle in seconds.",
        examples=[3600],
    )


class TurnaroundTimeRequest(CamelCaseModel):
    location_id: str = Field(
        ...,
        title="Location identifier",
        max_length=40,
        description="Location identification number based on UN/LOCODE, or other "
        "similar identification number of the transport location or facility.",
        examples=["FI OUL"],
    )
    start_time: datetime.datetime = Field(
        ...,
        title="Start time",
        description="The start time of the performance period, in RFC 3339 format.",
        examples=[
            datetime.datetime(2023, 4, 12, 23, 20, 50, tzinfo=datetime.timezone.utc)
        ],
    )
    end_time: datetime.datetime = Field(
        ...,
        title="End time",
        description="The end time of the performance period in, RFC 3339 format.",
        examples=[
            datetime.datetime(2023, 5, 12, 23, 20, 50, tzinfo=datetime.timezone.utc)
        ],
    )


class TurnaroundTimeResponse(CamelCaseModel):
    turnaround_times: List[TurnaroundTime] = Field(
        ...,
        title="Turnaround times",
        description="The list of turnaround times of vehicles within the facility.",
    )


DEFINITION = DataProductDefinition(
    version="0.1.0",
    title="Vehicle turnaround times",
    description="Turnaround times of vehicles within a facility.",
    tags=["Logistics"],
    request=TurnaroundTimeRequest,
    response=TurnaroundTimeResponse,
)
