from typing import Optional

from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import Field


class CargoItem(CamelCaseModel):
    product_name: Optional[str] = Field(
        None,
        title="Product name",
        description="Name of the product.",
        examples=["Example product"],
    )
    parcel: Optional[int] = Field(
        None,
        title="Parcel",
        description="Parcel number.",
        examples=[123456],
    )
    quantity: Optional[int] = Field(
        None,
        title="Quantity",
        description="Quantity of the product.",
        examples=[500],
    )
    weight: Optional[float] = Field(
        None,
        title="Weight (kg)",
        description="The weight in kilograms.",
        examples=[2000],
    )
    volume: Optional[float] = Field(
        None,
        title="Volume (m^3)",
        description="The volume in cubic meters.",
        examples=[5.5],
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
    weight: float = Field(
        ...,
        title="Weight (kg)",
        description="The weight of cargo within the same delivery in kilograms.",
        examples=[20000],
    )
    volume: Optional[float] = Field(
        None,
        title="Volume (m^3)",
        description="The volume of cargo within the same delivery in cubic meters if applicable.",
        examples=[50],
    )
    cargo_items: list[CargoItem] = Field(
        ...,
        title="Cargo items",
        description="List of cargo items.",
    )


DEFINITION = DataProductDefinition(
    version="0.1.0",
    title="Cargo metrics",
    description="The key metrics of the transported cargo",
    tags=["Cargo", "Metrics", "Volume", "Weight"],
    request=CargoMetricsRequest,
    response=CargoMetricsResponse,
)
