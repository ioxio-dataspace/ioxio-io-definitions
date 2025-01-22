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
        description="The query level of defining the product carbon footprint emissions.",
        examples=[QueryLevel.BATCH],
    )
    id: str = Field(
        ...,
        title="ID",
        description="If querying on model level an empty string is used. The batch id when querying on the batch level. The unique item id when querying on the item level.",
        max_length=40,
        examples=["batch-12345"],
    )


class Response(CamelCaseModel):
    material_footprint: Optional[float] = Field(
        None,
        title="Material footprint (kg of CO2e)",
        description="The carbon footprint of all materials used for manufacturing the product calculated as kg of CO2e using Product Category Rules (PCR).",
        examples=[4.8],
    )
    processing_footprint: Optional[float] = Field(
        None,
        title="Processing footprint (kg of CO2e)",
        description="The carbon footprint generated from the manufacturing process of the product calculated as kg of CO2e using Product Category Rules (PCR).",
        examples=[5.3],
    )
    logistics_footprint: Optional[float] = Field(
        None,
        title="Logistics footprint (kg of CO2e)",
        description="The carbon footprint generated from the upstream logisitics of delivering the product materials to manufacturing calculated as kg of CO2e using Product Category Rules (PCR).",
        examples=[0.3],
    )


DEFINITION = DataProductDefinition(
    version="0.1.0",
    title="Product carbon footprint",
    description="The carbon footprint of the product manufacturing",
    tags=["Carbon footprint", "PCR", "Product category rules"],
    request=Request,
    response=Response,
)
