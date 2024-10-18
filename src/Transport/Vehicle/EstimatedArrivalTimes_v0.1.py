from datetime import datetime
from typing import Optional

from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import Field


class EstimatedArrival(CamelCaseModel):
    vehicle_id: str = Field(
        ...,
        title="Vehicle identifier",
        description="Licence plate number or similar identification number of the "
        "vehicle or vessel.",
        max_length=128,
        examples=["ABC-123"],
    )
    vehicle_name: Optional[str] = Field(
        None,
        title="Vehicle name",
        description="Name of the vehicle or vessel.",
        max_length=128,
        examples=["Havelland"],
    )
    vehicle_type: Optional[str] = Field(
        None,
        title="Vehicle type",
        description="The type of the arriving vehicle.",
        max_length=128,
        examples=["container ship", "truck"],
    )
    estimated_arrival: datetime = Field(
        ...,
        title="Estimated arrival",
        description="Expected time of arrival for the vehicle to the facility, in RFC "
        "3339 format.",
        examples=[datetime.fromisoformat("2023-04-12T23:45:00Z")],
    )


class Request(CamelCaseModel):
    location_id: str = Field(
        ...,
        title="Location identifier",
        description="Location identification number based on UN/LOCODE, IATA or other "
        "similar identification number of the transport location.",
        max_length=40,
        examples=["FIOUL"],
    )
    start_time: datetime = Field(
        ...,
        title="Start time",
        description="The start time of the evaluation period, in RFC 3339 format.",
        examples=[datetime.fromisoformat("2023-04-12T23:20:50Z")],
    )
    end_time: datetime = Field(
        ...,
        title="End time",
        description="The end time of the evaluation period, in RFC 3339 format.",
        examples=[datetime.fromisoformat("2023-05-12T23:20:50Z")],
    )


class Response(CamelCaseModel):
    estimated_arrivals: list[EstimatedArrival] = Field(
        ...,
        title="Estimated arrivals",
        description="Estimated arrival times.",
    )


DEFINITION = DataProductDefinition(
    version="0.1.0",
    title="Estimated arrival times",
    description="Estimated arrival times of vehicles within a transport location.",
    tags=["Logistics", "ETA"],
    request=Request,
    response=Response,
)
