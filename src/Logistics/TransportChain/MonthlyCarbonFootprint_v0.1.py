from typing import Optional

from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import Field


class Location(CamelCaseModel):
    location_id: Optional[str] = Field(
        None,
        title="Location identifier",
        description="Location identification number based on UN/LOCODE number of the transport location.",
        min_length=0,
        max_length=40,
        examples=["DEHAM"],
    )
    city: str = Field(
        ...,
        title="City",
        description="The name of the city.",
        min_length=0,
        max_length=40,
        examples=["Hamburg"],
    )
    country: str = Field(
        ...,
        title="Country",
        description="The country code in Alpha-2 format.",
        pattern=r"^[A-Z]{2}$",
        min_length=2,
        max_length=2,
        examples=["DE"],
    )


class MonthlyFootprint(CamelCaseModel):
    origin: Location = Field(
        ...,
        title="Origin",
        description="The origin of the transport chain.",
    )
    destination: Location = Field(
        ...,
        title="Destination",
        description="The destination of the transport chain.",
    )
    calculation_method: str = Field(
        ...,
        title="Calculation method",
        description="A brief description of the method used to calculate the transport emissions.",
        min_length=0,
        max_length=400,
        examples=[
            "Used primary measured data from the following ISO 14083 standardized transport chain elements (TCE): transport and transfer operations."
        ],
    )
    carbon_footprint: float = Field(
        ...,
        title="Carbon footprint (kg of CO2e)",
        description="The total greenhouse gas (GHG) emissions of the transports and logistics hub operations measured in kilograms of CO2e for the requested time period.",
        examples=[5.8],
    )
    fossil_share: Optional[float] = Field(
        None,
        title="Fossil share (%)",
        description="The share of emissions from fossil sources, expressed as a percentage of total emissions.",
        gte=0,
        lte=100,
        examples=[25.0],
    )
    biogenic_share: Optional[float] = Field(
        None,
        title="Biogenic share (%)",
        description="The share of emissions from biogenic sources (e.g. biofuels), expressed as a percentage of total emissions.",
        gte=0,
        lte=100,
        examples=[50.0],
    )
    luluc_share: Optional[float] = Field(
        None,
        title="LULUC share (%)",
        description="The share of emissions from land use and land-use change associated with biomass or biofuel production, expressed as a percentage of total emissions.",
        gte=0,
        lte=100,
        examples=[25.0],
    )


class Request(CamelCaseModel):
    id: str = Field(
        ...,
        title="ID",
        description="The unique identifier that enables the identification of the legal entity across systems.",
        min_length=0,
        max_length=30,
        examples=["29771-01"],
    )
    month: str = Field(
        ...,
        title="Month",
        description="The year and month representing the reporting period for the carbon footprint, expressed in ISO 8601 format.",
        pattern=r"^\d{4}-(0[1-9]|1[0-2])$",
        examples=["2025-08"],
    )


class Response(CamelCaseModel):
    monthly_footprints: list[MonthlyFootprint] = Field(
        ...,
        title="Monthly footprints",
        description="A list of monthly carbon footprints for transport chains.",
    )


DEFINITION = DataProductDefinition(
    version="0.1.0",
    title="Monthly carbon footprint for logistics transport chains",
    description="Monthly logistics carbon footprint for a cargo owner compliant with GHG protocol Scope 3 transport emissions based on ISO 14083 standard.",
    tags=["Logistics", "Carbon footprint", "Emissions"],
    request=Request,
    response=Response,
)
