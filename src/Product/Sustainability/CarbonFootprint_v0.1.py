from enum import Enum
from typing import Optional

from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import Field


class QueryLevel(str, Enum):
    MODEL = "model"
    BATCH = "batch"
    ITEM = "item"


class Request(CamelCaseModel):
    product: str = Field(
        ...,
        title="Product",
        description="The product code used for identifying the product model.",
        max_length=150,
        examples=["product-modelX-1234"],
    )
    query_level: QueryLevel = Field(
        ...,
        title="Query level",
        description="The query level of defining the product's carbon footprint emissions.",
        examples=[QueryLevel.BATCH],
    )
    id: str = Field(
        ...,
        title="ID",
        description="If querying on model level an empty string is used. The batch identifier when querying on the batch level. The unique item identifier when querying on the product item level.",
        max_length=40,
        examples=["batch-12345"],
    )


class Response(CamelCaseModel):
    material_footprint: Optional[float] = Field(
        None,
        title="Material footprint (kg of CO2e)",
        description="The carbon footprint of all materials used for manufacturing the product calculated as kilograms of carbon dioxide equivalents using Product Category Rule (PCR) methods.",
        examples=[4.8],
    )
    processing_footprint: Optional[float] = Field(
        None,
        title="Processing footprint (kg of CO2e)",
        description="The carbon footprint generated from the manufacturing process of the product calculated as kilograms of carbon dioxide equivalents using Product Category Rule (PCR) methods.",
        examples=[5.3],
    )
    logistics_footprint: Optional[float] = Field(
        None,
        title="Logistics footprint (kg of CO2e)",
        description="The carbon footprint generated from the upstream logisitics of delivering the product materials to manufacturing calculated as kilograms of carbon dioxide equivalents using Product Category Rule (PCR) methods.",
        examples=[0.3],
    )


DEFINITION = DataProductDefinition(
    version="0.1.3",
    strict_validation=False,
    title="Product carbon footprint",
    description="The carbon footprint of manufacturing a product.",
    tags=["Carbon footprint", "Environment"],
    request=Request,
    response=Response,
)
