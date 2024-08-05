import datetime
from typing import Optional

from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import Field


class CargoMoves(CamelCaseModel):
    pick: int = Field(
        ...,
        title="Number of pick moves",
        description="Count of pick moves the cargo handling equipment has performed during the time period",
        examples=[52],
    )

    place: int = Field(
        ...,
        title="Number of place moves",
        description="Count of place moves the cargo handling equipment has performed during the time period",
        examples=[53],
    )


class HoistMoves(CamelCaseModel):
    lift: int = Field(
        ...,
        title="Number of lift moves",
        description="Count of lift moves the cargo handling equipment has performed during the time period",
        examples=[165],
    )
    lower: int = Field(
        ...,
        title="Number of lowering moves",
        description="Count of lowering moves the cargo handling equipment has performed during the time period",
        examples=[164],
    )


class OperationalPerformanceResponse(CamelCaseModel):
    running_hours: float = Field(
        ...,
        title="Running hours (h)",
        description="The total running hours",
        examples=[550.0],
    )
    distance: float = Field(
        ...,
        title="Cumulative distance (km)",
        description="The total distance driven in kilometers",
        examples=[2500.0],
    )
    cargo_moves: CargoMoves = Field(
        ...,
        title="Cargo moves",
        description="Counts of cargo handling moves per type (pick or place)",
    )
    hoist_moves: HoistMoves = Field(
        ...,
        title="Hoist moves",
        description="Counts of hoist moves per type (lift or fall)",
    )
    cargo_weight_processed: Optional[float] = Field(
        None,
        title="Cargo weight processed (kg)",
        description="The total cargo weight processed in kilograms",
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
        description="The start time of the performance period in RFC 3339 format",
        examples=[
            datetime.datetime(2023, 4, 12, 23, 20, 50, tzinfo=datetime.timezone.utc),
        ],
    )
    end_time: Optional[datetime.datetime] = Field(
        None,
        title="End time",
        description="The end time of the performance period in RFC 3339 format",
        examples=[
            datetime.datetime(2023, 5, 12, 23, 20, 50, tzinfo=datetime.timezone.utc),
        ],
    )


DEFINITION = DataProductDefinition(
    version="0.1.0",
    title="Cargo handling equipment operational performance",
    description="General operational status data of a mobile work machine operating in "
    "a port",
    request=OperationalPerformanceRequest,
    response=OperationalPerformanceResponse,
    tags=["Cargo handling equipment", "Port", "Freight terminal", "Logistics"],
)
