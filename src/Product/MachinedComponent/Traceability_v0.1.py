from datetime import datetime
from typing import Optional

from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import Field


class ComponentIdentification(CamelCaseModel):
    purchase_order: str = Field(
        ...,
        title="Purchase order",
        description="The number of the purchase order related to the component.",
        max_length=40,
        examples=["2345"],
    )
    work_order: Optional[str] = Field(
        None,
        title="Work order",
        description="The number of the manufacturing work order related to the component.",
        max_length=40,
        examples=["wo-2025-0001"],
    )
    forging_billet: Optional[str] = Field(
        None,
        title="Forging billet",
        description="The number identifying the forging billet batch used for manufacturing the component.",
        max_length=40,
        examples=["st-42crmo4-blt-ht1234-btch5678"],
    )
    waybill: str = Field(
        ...,
        title="Waybill",
        description="The identifier for the component shipment from the manufacturer to the customer.",
        max_length=40,
        examples=["1x999aa10123456784"],
    )
    code_nomenclature: Optional[str] = Field(
        None,
        title="Code nomenclature",
        description="The number identifying the component type according to EU harmonised system and Council Regulation (EEC) No 2658/87.",
        max_length=6,
        examples=["7326.9"],
    )


class ManufacturerInformation(CamelCaseModel):
    name: Optional[str] = Field(
        None,
        title="Name",
        description="The registered trade name of the manufacturer company.",
        max_length=250,
        examples=["Company xyz"],
    )
    website: Optional[str] = Field(
        None,
        title="Website",
        description="The website of the manufacturer.",
        pattern=r"^https://",
        max_length=2083,
        examples=["https://example.com/"],
    )


class Request(CamelCaseModel):
    id: str = Field(
        ...,
        title="ID",
        description="The unique identifier of the component.",
        max_length=40,
        examples=["b1a-0723y-00165"],
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
    drawing_number: Optional[str] = Field(
        None,
        title="Drawing number",
        description="The number identifying the component specification drawing.",
        max_length=40,
        examples=["12345"],
    )
    drawing_revision: Optional[str] = Field(
        None,
        title="Drawing revision",
        description="The version of the component specification drawing.",
        max_length=40,
        examples=["Rev A"],
    )
    machining_center: Optional[str] = Field(
        None,
        title="Machining center",
        description="An identifier or label assigned to a machining center used for machining the component.",
        max_length=40,
        examples=["cnc-101"],
    )
    routing_version: Optional[str] = Field(
        None,
        title="Routing version",
        description="The process sequence used for manufacturing the component.",
        max_length=40,
        examples=["r001"],
    )
    modification_timestamp: Optional[datetime] = Field(
        None,
        title="Modification timestamp",
        description="The latest timestamp used for updating the process routing in RFC 3339 format.",
        examples=[datetime.fromisoformat("2025-02-06T09:26:52+00:00")],
    )


DEFINITION = DataProductDefinition(
    version="0.1.0",
    title="Machined component traceability",
    description="The traceability information of a machined component.",
    tags=["Manufacturing", "Machinery and equipments"],
    request=Request,
    response=Response,
)
