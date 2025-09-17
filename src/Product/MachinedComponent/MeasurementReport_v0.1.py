from datetime import datetime
from typing import Optional

from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import Field


class MeasurementEquipment(CamelCaseModel):
    cmm_serial_number: str = Field(
        ...,
        title="CMM serial number",
        description="The serial number of the coordinate measuring machine.",
        max_length=40,
        examples=["mfg-model-xxxx-yyyy"],
    )
    cmm_type: Optional[str] = Field(
        None,
        title="CMM type",
        description="The type of the coordinate measuring machine.",
        max_length=40,
        examples=["bridge ccm"],
    )
    program_revision: Optional[str] = Field(
        None,
        title="Program revision",
        description="The version of a set of instructions or guidelines used to measure the dimensions and quality of components.",
        max_length=40,
        examples=["mp-001-rv02"],
    )


class ComponentIdentification(CamelCaseModel):
    purchase_order: str = Field(
        ...,
        title="Purchase order ",
        description="The number of the purchase order related to the component.",
        max_length=40,
        examples=["12345"],
    )
    component_name: str = Field(
        ...,
        title="Component name",
        description="The name of the component.",
        max_length=250,
        examples=["valve xyz"],
    )
    production_number: str = Field(
        ...,
        title="Production number",
        description="The production number related to the component manufacturing.",
        max_length=40,
        examples=["pn-20240205-00123"],
    )


class CustomerInformation(CamelCaseModel):
    name: str = Field(
        ...,
        title="Name",
        description="The name of the customer that has issued the component order.",
        max_length=250,
        examples=["Company xyz"],
    )
    department: Optional[str] = Field(
        None,
        title="Department",
        description="The responsible department of the customer that has issued the component order.",
        max_length=250,
        examples=["Department xyz"],
    )


class MeasurementSetup(CamelCaseModel):
    remarks: Optional[str] = Field(
        None,
        title="Remarks",
        description="The considerable notes regarding the measurement.",
        max_length=400,
        examples=[
            "Measurement taken from the outer edge to center, following xyz standards."
        ],
    )
    measurement_id: str = Field(
        ...,
        title="Measurement ID",
        description="The identifier of the quality measurement.",
        max_length=40,
        examples=["1234567"],
    )
    measurement_timestamp: datetime = Field(
        ...,
        title="Measurement timestamp",
        description="The quality measurement time of the component in RFC 3339 format.",
        examples=[datetime.fromisoformat("2025-02-06T09:26:52+00:00")],
    )
    measurement_run_type: str = Field(
        ...,
        title="Measurement run type",
        description="The method used to perform measurements on the components.",
        max_length=250,
        examples=["partial measurement"],
    )
    measured_components: int = Field(
        ...,
        title="Measured components",
        description="Then number of measured components from a batch.",
        examples=[50],
    )
    batch_size: Optional[int] = Field(
        None,
        title="Batch size",
        description="The entire size of the batch applying to same quality measurements.",
        examples=[100],
    )
    deviations: Optional[int] = Field(
        None,
        title="Deviations",
        description="The number of deviations (red values) in the measured values.",
        examples=[5],
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
        description="The identifiers of the equipment used in the measuring of the component.",
    )


class MeasurementResult(CamelCaseModel):
    feature_name: str = Field(
        ...,
        title="Feature name",
        description="The name of the measured feature.",
        max_length=250,
        examples=["valve diameter middle D84"],
    )
    measured_value: float = Field(
        ...,
        title="Measured value (mm)",
        description="The measured value of the feature in millimeters.",
        examples=[84.0250],
    )
    nominal_value: float = Field(
        ...,
        title="Nominal value (mm)",
        description="The nominal (theoretical) value of the measured feature in millimeters.",
        examples=[84.0000],
    )
    upper_tolerance: float = Field(
        ...,
        title="Upper tolerance (mm)",
        description="The upper tolerance allowed for the measurement in millimeters.",
        examples=[0.0550],
    )
    lower_tolerance: float = Field(
        ...,
        title="Lower tolerance (mm)",
        description="The lower tolerance allowed for the measurement in millimeters.",
        examples=[0.0550],
    )
    deviation: float = Field(
        ...,
        title="Deviation (mm)",
        description="Deviation from the measurement value in millimeters.",
        examples=[0.025],
    )
    tolerance_status: Optional[bool] = Field(
        None,
        title="Tolerance status",
        description="The indicator if the measured value is within tolerance.",
        examples=[True],
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
    version="0.1.1",
    strict_validation=False,
    deprecated=True,
    title="Machined component measurement report",
    description="The quality measurement report for a batch of machined components.",
    tags=["Manufacturing", "Machinery and equipment"],
    request=Request,
    response=Response,
)
