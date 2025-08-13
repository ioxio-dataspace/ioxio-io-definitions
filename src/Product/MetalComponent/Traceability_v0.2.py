from datetime import date
from enum import Enum
from typing import Optional

from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import Field


class QueryLevel(str, Enum):
    BATCH = "batch"
    ITEM = "item"


class CompanyIdentifierScheme(str, Enum):
    GLN = "gln"
    NATIONAL_BUSINESS_ID = "nationalBusinessId"
    DUNS = "duns"


class SubComponent(CamelCaseModel):
    name: Optional[str] = Field(
        None,
        title="Name",
        description="The name of the subcomponent.",
        min_length=0,
        max_length=150,
        examples=["metal fastener"],
    )
    identifier: Optional[str] = Field(
        None,
        title="Identifier",
        description="The identifier of the subcomponent either on a batch or item level.",
        min_length=0,
        max_length=20,
        examples=["batch-2024-ssbolt-0037"],
    )


class Blank(CamelCaseModel):
    identifier: Optional[str] = Field(
        None,
        title="Identifier",
        description="The identifier of the blank used for machining the component.",
        min_length=0,
        max_length=40,
        examples=["st-42crmo4-blt-ht1234-btch5678"],
    )
    type: Optional[str] = Field(
        None,
        title="Type",
        description="The type of the blank used for machining the component.",
        min_length=0,
        max_length=40,
        examples=["forging billet"],
    )


class CompanyIdentification(CamelCaseModel):
    identifier_scheme: CompanyIdentifierScheme = Field(
        ...,
        title="Identifier scheme",
        description="The identification scheme in use for the company. ",
        examples=[CompanyIdentifierScheme.GLN],
    )
    identifier: str = Field(
        ...,
        title="Identifier",
        description="The identification number according to the selected scheme.",
        min_length=0,
        max_length=20,
        examples=["1234567890123"],
    )


class ProcessIdentification(CamelCaseModel):
    identifier: Optional[str] = Field(
        None,
        title="Identifier",
        description="A unique identifier for the full sequence of manufacturing steps applied to a metal component or batch, including forming, cutting, machining, surface treatment, and related processes.",
        min_length=0,
        max_length=40,
        examples=["procset-metal-2024-0458"],
    )


class ComponentIdentification(CamelCaseModel):
    name: Optional[str] = Field(
        None,
        title="Name",
        description="The name of the component.",
        min_length=0,
        max_length=150,
    )
    sub_component_declaration: list[SubComponent] = Field(
        ...,
        title="Sub component declaration",
        description="List of declared subcomponents used in the component assembly.",
    )
    purchase_order: str = Field(
        ...,
        title="Purchase order",
        description="The number of the purchase order related to the component.",
        min_length=0,
        max_length=40,
        examples=["2345"],
    )
    work_order: str = Field(
        ...,
        title="Work order",
        description="The number of the manufacturing work order related to the component.",
        min_length=0,
        max_length=40,
        examples=["wo-2025-0001"],
    )
    shipment_id: Optional[str] = Field(
        None,
        title="ShipmentId",
        description="A unique identifier representing the release of goods from a location as part of a specific delivery or shipment.",
        min_length=0,
        max_length=40,
        examples=["19910123456784"],
    )
    blanks: list[Blank] = Field(
        ...,
        title="Blanks",
        description="The identification details of the the blanks used for manufacturing the component.",
    )
    code_nomenclature: Optional[str] = Field(
        None,
        title="Code nomenclature",
        description="The number identifying the component type according to EU harmonised system and Council Regulation (EEC) No 2658/87.",
        min_length=0,
        max_length=10,
        examples=["73269010"],
    )
    drawing_number: str = Field(
        ...,
        title="Drawing number",
        description="The number identifying the component specification drawing.",
        min_length=0,
        max_length=40,
        examples=["12345"],
    )
    drawing_revision: Optional[str] = Field(
        None,
        title="Drawing revision",
        description="The version of the component specification drawing.",
        min_length=0,
        max_length=40,
        examples=["Rev A"],
    )


class ManufacturerInformation(CamelCaseModel):
    name: str = Field(
        ...,
        title="Name",
        description="The registered trade name of the manufacturer company.",
        min_length=0,
        max_length=40,
        examples=["Company xyz"],
    )
    identification: CompanyIdentification = Field(
        ...,
        title="Identification",
        description="The identification of the company responsible for manufacturing the component. ",
    )
    address: Optional[str] = Field(
        None,
        title="Address",
        description="The address of the manufacturing site.",
        min_length=0,
        max_length=250,
        examples=["Rue des Lilas 12, 1050 Bruxelles, Belgium"],
    )
    contact_email: Optional[str] = Field(
        None,
        title="Contact email",
        description="The designated email contact for inquiries related to component manufacturing.",
        min_length=0,
        max_length=40,
        examples=["contact@company.com"],
    )


class Request(CamelCaseModel):
    product: str = Field(
        ...,
        title="Product",
        description="The product code used for identifying the product model.",
        min_length=0,
        max_length=150,
        examples=["product-modelX-1234"],
    )
    query_level: QueryLevel = Field(
        ...,
        title="Query level",
        description="The query level used to define the product's traceability information.",
        examples=[QueryLevel.BATCH],
    )
    id: str = Field(
        ...,
        title="ID",
        description="The batch identifier is used when querying on the batch level. The unique item identifier is used when querying on the product item level.",
        min_length=0,
        max_length=40,
        examples=["batch-12345"],
    )


class Response(CamelCaseModel):
    manufacturing_date: Optional[date] = Field(
        None,
        title="Manufacturing date",
        description="The manufacturing date of the product batch or item. ",
        examples=[date.fromisoformat("2025-02-06")],
    )
    delivery_date: Optional[date] = Field(
        None,
        title="Delivery date",
        description="The recorded date on which the component was shipped or handed over for delivery.",
        examples=[date.fromisoformat("2025-03-07")],
    )
    component_identification: ComponentIdentification = Field(
        ...,
        title="Component identification",
        description="The identifiers related to the component.",
    )
    manufacturer_information: ManufacturerInformation = Field(
        ...,
        title="Manufacturer information",
        description="The details of the component manufacturer.",
    )
    process_identification: ProcessIdentification = Field(
        ...,
        title="Process identification",
        description=None,
    )


DEFINITION = DataProductDefinition(
    version="0.2.1",
    deprecated=True,
    title="Metal component traceability information",
    description="The traceability information of a metal component.",
    tags=["Manufacturing", "Machinery and equipment"],
    request=Request,
    response=Response,
)
