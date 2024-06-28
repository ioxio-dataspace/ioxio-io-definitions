import datetime
from enum import Enum
from typing import List, Optional

from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import Field


class CargoMoveType(str, Enum):
    PICK = "pick"
    PLACE = "place"


class HoistMoveType(str, Enum):
    LIFT = "lift"
    FALL = "fall"


class CargoMoves(CamelCaseModel):
    type: Optional[CargoMoveType] = Field(
        None,
        title="Type",
        description="The type of the cargo moves operated with the equipment",
        examples=[CargoMoveType.PICK],
    )
    count: Optional[int] = Field(
        None,
        title="Count",
        description="The number of cargo moves operated with the equipment",
        examples=[52],
    )


class HoistMoves(CamelCaseModel):
    type: Optional[HoistMoveType] = Field(
        None,
        title="Type",
        description="The type of the hoist moves operated with the equipment",
        examples=[HoistMoveType.LIFT],
    )
    count: Optional[int] = Field(
        None,
        title="Count",
        description="The number of hoist moves operated with the equipment",
        examples=[165],
    )


class OperationalPerformanceResponse(CamelCaseModel):
    running_hours: float = Field(
        ...,
        title="Running hours",
        description="The total running hours (h)",
        examples=[550.0],
    )
    distance: float = Field(
        ...,
        title="Cumulative distance",
        description="The total distance driven in kilometers (km) ",
        examples=[2500.0],
    )
    cargo_moves: List[CargoMoves] = Field(
        ...,
        title="Cargo moves",
        description="The details of the cargo handling moves",
    )
    hoist_moves: List[HoistMoves] = Field(
        ...,
        title="Hoist moves",
        description="The details of the hoist moves",
    )
    cargo_weight_processed: Optional[float] = Field(
        None,
        title="Cargo weight processed",
        description="The total cargo weight processed kilograms (kg)",
        examples=[75.0],
    )


class OperationalPerformanceRequest(CamelCaseModel):
    id: str = Field(
        ...,
        max_length=40,
        title="Id",
        description="The unique identifier of the product",
        examples=["71b51878-8a00-11ee-b9d1-0242ac120002"],
    )
    start_time: Optional[datetime.datetime] = Field(
        None,
        title="Start time",
        description="The start time of the performance period in RFC 3339 format "
        "following ISO 8601",
        examples=[
            datetime.datetime(2023, 4, 12, 23, 20, 50, tzinfo=datetime.timezone.utc),
        ],
    )
    end_time: Optional[datetime.datetime] = Field(
        None,
        title="End time",
        description="The end time of the performance period in the desired country in "
        "RFC 3339 format following ISO 8601",
        examples=[
            datetime.datetime(2023, 5, 12, 23, 20, 50, tzinfo=datetime.timezone.utc),
        ],
    )


DEFINITION = DataProductDefinition(
    version="0.1.0",
    title="Cargo Handling Equipment Operational Performance",
    description="General operational status data of a mobile work machine operating in "
    "a port",
    request=OperationalPerformanceRequest,
    response=OperationalPerformanceResponse,
    tags=["Cargo handling equipment", "Port", "Freight terminal", "Logistics"],
)
