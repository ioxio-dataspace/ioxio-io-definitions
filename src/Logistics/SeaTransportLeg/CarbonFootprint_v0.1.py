from datetime import date
from typing import Optional

from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import Field


class Location(CamelCaseModel):
    location_id: str = Field(
        ...,
        title="Location identifier",
        description="Location identification number based on UN/LOCODE number of the transport location.",
        min_length=0,
        max_length=40,
        examples=["DEHAM"],
    )
    city: Optional[str] = Field(
        None,
        title="City",
        description="The name of the city.",
        min_length=0,
        max_length=40,
        examples=["Hamburg"],
    )
    country: Optional[str] = Field(
        None,
        title="Country",
        description="The country code in Alpha-2 format.",
        pattern=r"^[A-Z]{2}$",
        examples=["DE"],
    )


class Request(CamelCaseModel):
    origin_port: str = Field(
        ...,
        title="Location identifier",
        description="UN/LOCODE identifying the origin of the sea transport leg for the cargo.",
        min_length=0,
        max_length=10,
        examples=["FIHEL"],
    )
    destination_port: str = Field(
        ...,
        title="Location identifier",
        description="UN/LOCODE identifying the destination of a sea transport leg for the cargo.",
        min_length=0,
        max_length=10,
        examples=["DEHAM"],
    )
    id: str = Field(
        ...,
        title="ID",
        description="An identifier used for a sea transportation.",
        min_length=0,
        max_length=40,
        examples=["TRLG56A9B2E1"],
    )
    reference_date: Optional[date] = Field(
        None,
        title="Reference date",
        description="A date value used to uniquely reference or categorize a transport leg or delivery within a transport chain.",
        examples=[date.fromisoformat("2025-02-06")],
    )


class Response(CamelCaseModel):
    origin: Location = Field(
        ...,
        title="Origin",
        description="The origin of the sea transport leg.",
    )
    destination: Location = Field(
        ...,
        title="Destination",
        description="The destination of the sea transport leg.",
    )
    transport_chain_footprint: float = Field(
        ...,
        title="Transport chain footprint (kg of CO2e)",
        description="The total greenhouse gas (GHG) emissions of the transports and related logistics hub operations measured in kilograms of CO2e.",
        examples=[5.8],
    )
    calculation_method: str = Field(
        ...,
        title="Calculation method",
        description="A brief description of the method used to calculate the transport emissions.",
        min_length=0,
        max_length=400,
        examples=[
            "Primary measured data in accordance with ISO 14083, following standardized Transport Chain Elements (TCE) for the corresponding sea transport operations."
        ],
    )
    distance: Optional[float] = Field(
        None,
        title="Distance (km)",
        description="The distance of the transport chain in kilometers.",
        examples=[484],
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


DEFINITION = DataProductDefinition(
    version="0.1.0",
    title="Carbon footprint for a sea transport leg",
    description="Carbon footprint for a sea transport leg within a transport chain of a cargo compliant with GHG protocol Scope 3 transport emissions guidance and ISO 14083 standard.",
    tags=["Logistics", "Emissions"],
    request=Request,
    response=Response,
)
