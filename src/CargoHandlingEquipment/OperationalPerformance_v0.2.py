import datetime
from typing import Optional

from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import Field


class CargoMoves(CamelCaseModel):
    pick: Optional[int] = Field(
        None,
        title="Number of pick moves",
        description="Count of pick moves the cargo handling equipment has performed during the time period",
        examples=[52],
    )

    place: Optional[int] = Field(
        None,
        title="Number of place moves",
        description="Count of place moves the cargo handling equipment has performed during the time period",
        examples=[53],
    )


class HoistMoves(CamelCaseModel):
    lift: Optional[int] = Field(
        None,
        title="Number of lift moves",
        description="Count of lifting moves the cargo handling equipment has performed during the time period",
        examples=[165],
    )
    lower: Optional[int] = Field(
        None,
        title="Number of lowering moves",
        description="Count of lowering moves the cargo handling equipment has performed during the time period",
        examples=[164],
    )


class OperationalPerformanceResponse(CamelCaseModel):
    start_time: Optional[datetime.datetime] = Field(
        None,
        title="Start time",
        description="The start time of the performance period, in RFC 3339 format",
        examples=[
            datetime.datetime(2023, 4, 12, 23, 20, 50, tzinfo=datetime.timezone.utc),
        ],
    )
    end_time: Optional[datetime.datetime] = Field(
        None,
        title="End time",
        description="The end time of the performance period, in RFC 3339 format",
        examples=[
            datetime.datetime(2023, 5, 12, 23, 20, 50, tzinfo=datetime.timezone.utc),
        ],
    )
    running_hours: float = Field(
        ...,
        title="Running hours (h)",
        description="The running hours during the specified time range",
        examples=[550.0],
    )
    distance: float = Field(
        ...,
        title="Distance (km)",
        description="The total distance driven in kilometers during the specified time range",
        examples=[2500.0],
    )
    cargo_moves: Optional[CargoMoves] = Field(
        None,
        title="Cargo moves",
        description="Counts of cargo handling moves per type (pick or place)",
    )
    hoist_moves: Optional[HoistMoves] = Field(
        None,
        title="Hoist moves",
        description="Counts of hoist moves per type (lift or lower)",
    )
    cargo_weight_processed: Optional[float] = Field(
        None,
        title="Cargo weight processed (kg)",
        description="The total cargo weight processed kilograms",
        examples=[75.0],
    )


class OperationalPerformanceRequest(CamelCaseModel):
    id: str = Field(
        ...,
        max_length=40,
        title="ID",
        description="The unique identifier of the product",
        examples=["71b51878-8a00-11ee-b9d1-0242ac120002"],
    )
    start_time: Optional[datetime.datetime] = Field(
        None,
        title="Start time",
        description="The start time of the performance period, in RFC 3339 format",
        examples=[
            datetime.datetime(2023, 4, 12, 23, 20, 50, tzinfo=datetime.timezone.utc),
        ],
    )
    end_time: Optional[datetime.datetime] = Field(
        None,
        title="End time",
        description="The end time of the performance period in, RFC 3339 format",
        examples=[
            datetime.datetime(2023, 5, 12, 23, 20, 50, tzinfo=datetime.timezone.utc),
        ],
    )


DEFINITION = DataProductDefinition(
    version="0.2.0",
    title="Cargo handling equipment operational performance",
    description="General operational status data of a mobile work machine operating in "
    "a port",
    request=OperationalPerformanceRequest,
    response=OperationalPerformanceResponse,
    tags=["Cargo handling equipment", "Port", "Freight terminal", "Logistics"],
)
