from datetime import datetime
from enum import Enum
from typing import Optional

from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import Field


class QueryLevel(str, Enum):
    MODEL = "model"
    BATCH = "batch"
    ITEM = "item"


class CompanyIdentifierScheme(str, Enum):
    GLN = "gln"
    NATIONAL_BUSINESS_ID = "nationalBusinessId"
    DUNS = "duns"


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
        examples=["gln"],
    )
    identifier: str = Field(
        ...,
        title="Identifier",
        description="The identification number according to the selected scheme.",
        min_length=0,
        max_length=20,
        examples=["1234567890123"],
    )


class ComponentIdentification(CamelCaseModel):
    purchase_order: str = Field(
        ...,
        title="Purchase order",
        description="The number of the purchase order related to the component.",
        min_length=0,
        max_length=40,
        examples=["2345"],
    )
    work_order: Optional[str] = Field(
        None,
        title="Work order",
        description="The number of the manufacturing work order related to the component.",
        min_length=0,
        max_length=40,
        examples=["wo-2025-0001"],
    )
    waybill: str = Field(
        ...,
        title="Waybill",
        description="The identifier for the component shipment from the component manufacturer to the customer.",
        min_length=0,
        max_length=40,
        examples=["1x999aa10123456784"],
    )
    blank: Blank = Field(
        ...,
        title="Blank",
        description="The identification details of the the blank used for machining the component.",
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
        description="The identification of the company responsible for manufacturing the component.",
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


class MachiningCenter(CamelCaseModel):
    identifier: str = Field(
        ...,
        title="Identifier",
        description="The identifier of the machining center.",
        min_length=0,
        max_length=40,
        examples=["cnc-101"],
    )
    numerical_control_version: Optional[str] = Field(
        None,
        title="Numerical control version",
        description="The version of the controller software used by the machining center.",
        min_length=0,
        max_length=40,
        examples=["nc-v10.3"],
    )
    routing_version: Optional[str] = Field(
        None,
        title="Routing version",
        description="The process sequence used for machining the component.",
        min_length=0,
        max_length=40,
        examples=["r001"],
    )
    modification_timestamp: Optional[datetime] = Field(
        None,
        title="Modification timestamp",
        description="The latest timestamp used for updating the process routing, in RFC 3339 format.",
        examples=[datetime.fromisoformat("2025-02-06T09:26:52+00:00")],
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
        description="If querying on model level an empty string is used. The batch identifier is used when querying on the batch level. The unique item identifier is used when querying on the product item level.",
        min_length=0,
        max_length=40,
        examples=["batch-12345"],
    )


class Response(CamelCaseModel):
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
    machining_centers: list[MachiningCenter] = Field(
        ...,
        title="Machining centers",
        description="The details of the equipment used for machining the component.",
    )
    surface_treatments: list[str] = Field(
        ...,
        title="Surface treatments",
        description="Details of the surface treatments applied to the component.",
        examples=[["phosphating"], ["powder coating"]],
    )


DEFINITION = DataProductDefinition(
    version="0.1.0",
    title="Machined component traceability information",
    description="The traceability information of a machined metal component.",
    tags=["Manufacturing", "Machinery and equipment"],
    request=Request,
    response=Response,
)
