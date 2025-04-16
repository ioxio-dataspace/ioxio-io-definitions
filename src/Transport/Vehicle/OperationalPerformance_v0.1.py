from datetime import datetime
from typing import Optional

from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import Field


class OperationalPerformanceRequest(CamelCaseModel):
    id: str = Field(
        ...,
        title="ID",
        description="The unique identifier of the vehicle.",
        max_length=40,
        examples=["71b51878-8a00-11ee-b9d1-0242ac120002"],
    )
    start_time: Optional[datetime] = Field(
        None,
        title="Start time",
        description="The start time of the performance period, in RFC 3339 format.",
        examples=[datetime.fromisoformat("2023-04-12T23:20:50Z")],
    )
    end_time: Optional[datetime] = Field(
        None,
        title="End time",
        description="The end time of the performance period in, RFC 3339 format.",
        examples=[datetime.fromisoformat("2023-05-12T23:20:50Z")],
    )


class OperationalPerformanceResponse(CamelCaseModel):
    start_time: Optional[datetime] = Field(
        None,
        title="Start time",
        description="The start time of the performance period, in RFC 3339 format.",
        examples=[datetime.fromisoformat("2023-04-12T23:20:50Z")],
    )
    end_time: Optional[datetime] = Field(
        None,
        title="End time",
        description="The end time of the performance period, in RFC 3339 format.",
        examples=[datetime.fromisoformat("2023-05-12T23:20:50Z")],
    )
    running_hours: float = Field(
        ...,
        title="Running hours (h)",
        description="The running hours during the specified time range.",
        examples=[550.0],
    )
    idling_hours: Optional[float] = Field(
        None,
        title="Idling hours (h)",
        description="The idling hours during the specified time range.",
        examples=[1.5],
    )
    distance: float = Field(
        ...,
        title="Distance (km)",
        description="The total distance driven in kilometers during the specified time range.",
        examples=[3500.0],
    )
    average_fuel_consumption: Optional[float] = Field(
        None,
        title="Average fuel consumption (l/100km)",
        description="The average fuel consumption of the vehicle.",
        examples=[30.0],
    )
    average_electricity_consumption: Optional[float] = Field(
        None,
        title="Average electricity consumption (kWh/100km)",
        description="The average electricity consumption of the vehicle.",
        examples=[150.0],
    )
    average_speed: Optional[float] = Field(
        None,
        title="Average speed (km/h)",
        description="The average speed of the vehicle.",
        examples=[50.0],
    )


DEFINITION = DataProductDefinition(
    version="0.1.1",
    title="Transport vehicle operational performance",
    description="General operational performance data of a transport vehicle.",
    tags=["Road transport", "Logistics"],
    request=OperationalPerformanceRequest,
    response=OperationalPerformanceResponse,
)
