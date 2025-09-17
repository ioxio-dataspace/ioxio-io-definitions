from enum import Enum
from typing import Optional

from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import Field


class CargoType(str, Enum):
    CONTAINER = "container"
    BULK = "bulk"
    BREAKBULK = "breakbulk"
    LIQUID = "liquid"


class CargoItem(CamelCaseModel):
    weight: Optional[float] = Field(
        None,
        title="Weight (kg)",
        description="The weight of the cargo item in kilograms.",
        examples=[2000],
    )
    volume: Optional[float] = Field(
        None,
        title="Volume (m^3)",
        description="The volume of the cargo item in cubic meters.",
        examples=[5.25],
    )
    length: Optional[float] = Field(
        None,
        title="Length (m)",
        description="The length of the cargo item in meters.",
        examples=[3.5],
    )
    width: Optional[float] = Field(
        None,
        title="Width (m)",
        description="The width of the cargo item in meters.",
        examples=[1.5],
    )
    height: Optional[float] = Field(
        None,
        title="Height (m)",
        description="The height of the cargo item in meters.",
        examples=[1.0],
    )


class CargoMetricsRequest(CamelCaseModel):
    waybill_number: str = Field(
        ...,
        title="Waybill number",
        description="The unique identifier which is used to track a shipment through the entire delivery chain.",
        max_length=128,
        examples=["5308956234"],
    )


class CargoMetricsResponse(CamelCaseModel):
    cargo_type: CargoType = Field(
        ...,
        title="Cargo type",
        description="The type of the cargo within the delivery.",
        examples=[CargoType.BREAKBULK],
    )
    weight: Optional[float] = Field(
        None,
        title="Weight (kg)",
        description="The weight of the cargo within the delivery in kilograms.",
        examples=[20000],
    )
    volume: Optional[float] = Field(
        None,
        title="Volume (m^3)",
        description="The volume of the cargo within the delivery in cubic meters.",
        examples=[50],
    )
    cargo_units: Optional[int] = Field(
        None,
        title="Cargo units",
        description="The number of the cargo units in the delivery.",
        examples=[1],
    )
    cargo_items: list[CargoItem] = Field(
        ...,
        title="Cargo items",
        description="The details of the cargo items within the delivery.",
    )


DEFINITION = DataProductDefinition(
    version="0.1.1",
    strict_validation=False,
    title="Cargo metrics",
    description="The key metrics of the transported cargo",
    tags=["Cargo", "Metrics", "Volume", "Weight", "Packing list"],
    request=CargoMetricsRequest,
    response=CargoMetricsResponse,
)
