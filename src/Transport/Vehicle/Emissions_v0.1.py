from datetime import datetime
from typing import Optional

from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import Field


class EmissionsRequest(CamelCaseModel):
    id: str = Field(
        ...,
        title="ID",
        description="The unique identifier of the vehicle.",
        max_length=40,
        examples=["71b51878-8a00-11ee-b9d1-0242ac120002"],
    )
    start_time: Optional[datetime] = Field(
        None,
        title="Start time",
        description="The start time of the evaluation period, in RFC 3339 format.",
        examples=[datetime.fromisoformat("2023-04-12T23:20:50Z")],
    )
    end_time: Optional[datetime] = Field(
        None,
        title="End time",
        description="The end time of the evaluation period in, RFC 3339 format.",
        examples=[datetime.fromisoformat("2023-05-12T23:20:50Z")],
    )


class EmissionsResponse(CamelCaseModel):
    start_time: Optional[datetime] = Field(
        None,
        title="Start time",
        description="The start time of the evaluation period, in RFC 3339 format.",
        examples=[datetime.fromisoformat("2023-04-12T23:20:50Z")],
    )
    end_time: Optional[datetime] = Field(
        None,
        title="End time",
        description="The end time of the evaluation period in, RFC 3339 format.",
        examples=[datetime.fromisoformat("2023-05-12T23:20:50Z")],
    )
    carbon_dioxide: float = Field(
        ...,
        title="Carbon dioxide (kg)",
        description="The mass of the carbon dioxide (CO2) emissions in kilograms.",
        examples=[4000],
    )
    nitrogen_oxides: float = Field(
        ...,
        title="Nitrogen oxides (kg)",
        description="The mass of the nitrogen oxides emissions (NOx) in kilograms.",
        examples=[1.5],
    )
    particulate_matter: float = Field(
        ...,
        title="Particulate matter (kg)",
        description="The mass of the particulate matter emissions (PM) in kilograms.",
        examples=[0.05],
    )


DEFINITION = DataProductDefinition(
    version="0.1.3",
    strict_validation=False,
    title="Transport vehicle emissions",
    description="The emissions of a transport vehicle.",
    tags=["Road transport", "Logistics", "Environment", "Emissions"],
    request=EmissionsRequest,
    response=EmissionsResponse,
)
