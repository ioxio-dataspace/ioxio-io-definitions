from datetime import datetime
from enum import Enum
from typing import Optional

from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import Field


class QueryLevel(str, Enum):
    MODEL = "model"
    BATCH = "batch"
    ITEM = "item"


class ComponentIdentification(CamelCaseModel):
    purchase_order: str = Field(
        ...,
        title="Purchase order",
        description="The number of the purchase order related to the component.",
        min_length=0,
        max_length=40,
        examples=["12345"],
    )
    component_name: str = Field(
        ...,
        title="Component name",
        description="The name of the component.",
        min_length=0,
        max_length=250,
        examples=["valve xyz"],
    )
    production_number: str = Field(
        ...,
        title="Production number",
        description="The production number related to the component manufacturing.",
        min_length=0,
        max_length=40,
        examples=["pn-20240205-00123"],
    )
    drawing_number: str = Field(
        ...,
        title="Drawing number",
        description="The drawing number related to the component.",
        min_length=0,
        max_length=40,
        examples=["xy00012345687"],
    )


class CustomerInformation(CamelCaseModel):
    name: str = Field(
        ...,
        title="Name",
        description="The name of the customer that has issued the component order.",
        min_length=0,
        max_length=250,
        examples=["Company xyz"],
    )
    department: Optional[str] = Field(
        None,
        title="Department",
        description="The responsible department of the customer that has issued the component order.",
        min_length=0,
        max_length=250,
        examples=["Department xyz"],
    )


class MeasurementResult(CamelCaseModel):
    feature_name: str = Field(
        ...,
        title="Feature name",
        description="The name of the measured feature.",
        min_length=0,
        max_length=250,
        examples=["valve diameter middle D84"],
    )
    measured_value: float = Field(
        ...,
        title="Measured value (mm)",
        description="The measured value of the feature in millimeters.",
        examples=[84.0250],
    )
    nominal_value: Optional[float] = Field(
        None,
        title="Nominal value (mm)",
        description="The nominal (theoretical) value of the measured feature in millimeters.",
        examples=[84.0000],
    )
    upper_tolerance: Optional[float] = Field(
        None,
        title="Upper tolerance (mm)",
        description="The upper tolerance allowed for the measurement in millimeters.",
        examples=[0.0550],
    )
    lower_tolerance: Optional[float] = Field(
        None,
        title="Lower tolerance (mm)",
        description="The lower tolerance allowed for the measurement in millimeters.",
        examples=[0.0550],
    )
    deviation: Optional[float] = Field(
        None,
        title="Deviation (mm)",
        description="Deviation from the measurement value in millimeters.",
        examples=[0.025],
    )
    is_within_tolerance: Optional[bool] = Field(
        None,
        title="Is within tolerance",
        description="The indicator whether the measured value is within tolerance.",
        examples=[True],
    )


class MeasurementEquipment(CamelCaseModel):
    machine_serial_number: Optional[str] = Field(
        None,
        title="Machine serial number",
        description="The serial number of the measuring machine.",
        min_length=0,
        max_length=40,
        examples=["mfg-model-xxxx-yyyy"],
    )


class MeasurementSetup(CamelCaseModel):
    remarks: Optional[str] = Field(
        None,
        title="Remarks",
        description="The notes to consider regarding the measurement.",
        min_length=0,
        max_length=400,
        examples=[
            "Measurement taken from the outer edge to center, following xyz standards."
        ],
    )
    measurement_id: Optional[str] = Field(
        None,
        title="Measurement ID",
        description="The identifier of the quality measurement.",
        min_length=0,
        max_length=40,
        examples=["1234567"],
    )
    measurement_timestamp: Optional[datetime] = Field(
        None,
        title="Measurement timestamp",
        description="Timestamp of the quality measurement of the component, in RFC 3339 format.",
        examples=[datetime.fromisoformat("2025-02-06T09:26:52+00:00")],
    )
    measurement_run_type: Optional[str] = Field(
        None,
        title="Measurement run type",
        description="The method used to perform measurements on the components.",
        min_length=0,
        max_length=250,
        examples=["partial measurement"],
    )
    batch_size: Optional[int] = Field(
        None,
        title="Batch size",
        description="The entire size of the batch that was manufactured under the same id.",
        examples=[100],
    )
    measured_items: Optional[int] = Field(
        None,
        title="Measured items",
        description="The number of measured components from the batch.",
        examples=[50],
    )
    deviations: Optional[int] = Field(
        None,
        title="Deviations",
        description="The number of values that fall outside tolerance in the measured batch (red values).",
    )
    duration: Optional[int] = Field(
        None,
        title="Duration (s)",
        description="The duration of the measurement process in seconds.",
        examples=[825],
    )
    measurement_equipment: list[MeasurementEquipment] = Field(
        ...,
        title="Measurement equipment",
        description="The identifiers of the equipment used to measure the component.",
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
        description="The query level used to define the product's quality measurement report.",
        examples=[QueryLevel.MODEL],
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
    customer_information: CustomerInformation = Field(
        ...,
        title="Customer information",
        description="The details of the customer issuing the order for the component.",
    )
    measurement_setup: MeasurementSetup = Field(
        ...,
        title="Measurement setup",
        description="The details describing the quality measurement setup.",
    )
    measurement_results: list[MeasurementResult] = Field(
        ...,
        title="Measurement results",
        description="The results of the quality measurements.",
    )


DEFINITION = DataProductDefinition(
    version="0.2.1",
    deprecated=True,
    title="Metal component measurement report",
    description="The quality measurement report for metal components.",
    tags=["Manufacturing", "Machinery and equipment"],
    request=Request,
    response=Response,
)
