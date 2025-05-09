from enum import Enum
from typing import List, Optional

from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import EmailStr, Field


class ManufacturingLocation(CamelCaseModel):
    country: Optional[str] = Field(
        None,
        title="Country",
        pattern=r"^[A-Z]{3}$",
        description="The country code of the battery manufacturing location in Alpha-3 "
        "format.",
        examples=["DEU"],
    )
    city: Optional[str] = Field(
        None,
        title="City",
        max_length=40,
        description="The city of the battery manufacturing location.",
        examples=["Hamburg"],
    )


class ManufacturerInformation(CamelCaseModel):
    name: Optional[str] = Field(
        None,
        max_length=250,
        title="Name",
        description="The registered trade name of the manufacturer company.",
        examples=["Battery Manufacturer A"],
    )
    street_name: Optional[str] = Field(
        None,
        title="Street Name",
        max_length=40,
        description="The street address of the manufacturer's headquarters.",
        examples=["Example Street 100"],
    )
    postal_code: Optional[str] = Field(
        None,
        title="Postal Code",
        max_length=10,
        description="The postal code of the manufacturer's headquarters.",
        examples=["75034"],
    )
    city: Optional[str] = Field(
        None,
        title="City",
        max_length=40,
        description="The city of the manufacturer's headquarters.",
        examples=["Seattle"],
    )
    country: Optional[str] = Field(
        None,
        title="Country",
        pattern=r"^[A-Z]{3}$",
        description="The country code of the manufacturer's headquarters location in "
        "Alpha-3 format.",
        examples=["USA"],
    )
    website: Optional[str] = Field(
        None,
        pattern=r"^https://",
        max_length=2083,
        title="Website",
        description="The website of the manufacturer.",
        examples=["https://example.com/"],
    )
    email: Optional[EmailStr] = Field(
        None,
        title="Email",
        description="The email address of the manufacturer.",
        examples=["info@example.com"],
    )


class BatteryCategory(str, Enum):
    STATIONARY_ENERGY_STORAGE = "stationary energy storage"
    INDUSTRIAL_BATTERY = "industrial battery"
    LMT_BATTERY = "lmt battery"
    ELECTRIC_VEHICLE_BATTERY = "electric vehicle battery"


class RoundTripEfficiency(CamelCaseModel):
    initial_energy_efficiency: Optional[float] = Field(
        None,
        title="Initial Energy Efficiency",
        description="The initial round trip energy efficiency of a battery in "
        "percentage (%).",
        examples=[75.0],
    )
    degraded_energy_efficiency: Optional[float] = Field(
        None,
        title="Degraded Energy Efficiency",
        description="The round trip energy efficiency of an energy storage battery in "
        "percentage (%) at 50% of expected cycle life.",
        examples=[60.0],
    )


class VoltageLevels(CamelCaseModel):
    nominal_voltage: Optional[float] = Field(
        None,
        title="Nominal Voltage",
        description="The average voltage the battery output when fully charged.",
        examples=[550.0],
    )
    maximum_voltage: Optional[float] = Field(
        None,
        title="Maximum Voltage",
        description="The highest level the battery voltage can reach.",
        examples=[620.0],
    )
    minimum_voltage: Optional[float] = Field(
        None,
        title="Minimum Voltage",
        description="The lowest level the battery voltage can reach.",
        examples=[180.0],
    )


class TemperatureRange(CamelCaseModel):
    minimum_temperature: Optional[float] = Field(
        None,
        title="Minimum Temperature (°C)",
        description="The minimum environment temperature the battery can withstand in "
        "Celsius degrees.",
        examples=[-40.0],
        le=100,
        ge=-100,
    )
    maximum_temperature: Optional[float] = Field(
        None,
        title="Maximum Temperature (°C)",
        description="The maximum environment temperature the battery can withstand in "
        "Celsius degrees.",
        examples=[50.0],
        le=100,
        ge=-100,
    )


class ExpectedLifetime(CamelCaseModel):
    cycle_life: Optional[int] = Field(
        None,
        title="Cycle Life",
        ge=0,
        description="Minimum number of cycles the battery can be recharged to at least "
        "80% of initial capacity.",
        examples=[5000],
    )
    reference_test: Optional[str] = Field(
        None,
        title="Reference Test",
        max_length=250,
        description="The details of the reference test used for defining the expected "
        "lifetime.",
        examples=["Accelerated cycle life testing"],
    )
    cycle_rate: Optional[str] = Field(
        None,
        title="Cycle Rate",
        description="The C-rate used in the cycle life test.",
        examples=["1C"],
    )


class MaterialComposition(CamelCaseModel):
    chemistry: List[str] = Field(
        ...,
        title="Chemistry",
        description="The chemical composition of the battery.",
        examples=[["Sodium", "Cobalt"]],
    )
    hazardous_substances: List[str] = Field(
        ...,
        title="Hazardous Substances",
        description="The hazardous substances present in the battery.",
        examples=[["Sulphuric acid"]],
    )
    critical_raw_materials: List[str] = Field(
        ...,
        title="Critical Raw Materials",
        description="The critical raw materials present in the battery in a "
        "concentration of more than 0.1% weight by weight.",
        examples=[["Cobalt"]],
    )


class RecycledContent(CamelCaseModel):
    substance_name: Optional[str] = Field(
        None,
        title="Substance Name",
        max_length=40,
        description="The name of the substance that has recycled content.",
        examples=["Cobalt"],
    )
    recycling_rate: Optional[float] = Field(
        None,
        title="Recycling Rate",
        description="The amount of recycled content in the substance in percentage (%) "
        "by weight.",
        examples=[8.5],
    )


class RenewableContent(CamelCaseModel):
    substance_name: Optional[str] = Field(
        None,
        title="Substance Name",
        max_length=40,
        description="The name of the substance that has renewable content.",
        examples=["Ligning"],
    )
    proportion: Optional[float] = Field(
        None,
        title="Proportion",
        description="The share of the renewable content present in the battery in "
        "percentage (%) by weight.",
        examples=[2.0],
    )


class LegalConformity(CamelCaseModel):
    battery_act_compliance: Optional[bool] = Field(
        None,
        title="Battery Act Compliance",
        description="The indicator if the battery complies with the requirements of "
        "the battery act or not.",
        examples=[True],
    )
    requirement_conformity: List[str] = Field(
        ...,
        title="Requirement Conformity",
        description="The compliance of the battery with other legal and standard "
        "requirements.",
        examples=[["ROHS", "CE HSE", "IEC62619"]],
    )
    conformity_declaration: Optional[str] = Field(
        None,
        pattern=r"^https://",
        max_length=2083,
        title="Conformity Declaration",
        description="The link to the EU declaration of conformity documentation.",
        examples=["https://example.com/EUdeclaration"],
    )


class ManufacturingDataSheetResponse(CamelCaseModel):
    product_name: Optional[str] = Field(
        None,
        title="Product Name",
        description="The official sales name of the product.",
        examples=["Battery Model A"],
    )
    battery_model: Optional[str] = Field(
        None,
        title="Battery Model",
        max_length=40,
        description="The model of the battery.",
        examples=["Z37-310-76"],
    )
    battery_category: Optional[BatteryCategory] = Field(
        None,
        title="Battery Category",
        description="The category of the battery based on its intended use.",
        examples=[BatteryCategory.INDUSTRIAL_BATTERY],
    )
    manufacturer_information: Optional[ManufacturerInformation] = Field(
        None,
        title="Manufacturer Information",
        description="The details of the battery manufacturer.",
    )
    manufacturing_location: Optional[ManufacturingLocation] = Field(
        None,
        title="Manufacturing Location",
        description="The details of the location of the battery manufacturing plant.",
    )
    manufacturing_date: Optional[str] = Field(
        None,
        title="Manufacturing Date",
        description="The date of manufacture using month and year.",
        pattern=r"^\d{4}-(0[1-9]|1[0-2])$",
        examples=["2023-07"],
    )
    weight: Optional[float] = Field(
        None,
        title="Weight (kg)",
        description="The total net weight of the product in kilograms.",
        examples=[450.0],
    )
    capacity: Optional[float] = Field(
        None,
        title="Capacity (Ah)",
        description="The total number of ampere-hours that can be withdrawn from "
        "a fully charged battery under reference conditions.",
        examples=[100.0],
    )
    power: Optional[float] = Field(
        None,
        title="Power (W)",
        description="The original power capability of the battery in Watts.",
        examples=[25000.0],
    )
    cell_type: Optional[str] = Field(
        None,
        max_length=250,
        title="Cell Type",
        description="The type of cells used in the battery pack.",
        examples=["sodium-ion"],
    )
    resistance: Optional[float] = Field(
        None,
        title="Resistance (Ω)",
        description="The internal resistance of the battery pack in ohms.",
        examples=[0],
    )
    round_trip_efficiency: Optional[RoundTripEfficiency] = Field(
        None,
        title="Round Trip Efficiency",
        description="The details of the round trip energy efficiency in energy "
        "storages.",
    )
    voltage_levels: Optional[VoltageLevels] = Field(
        None,
        title="Voltage Levels",
        description="The details of the voltage levels of the battery.",
    )
    temperature_range: Optional[TemperatureRange] = Field(
        None,
        title="Temperature Range",
        description="The details of the acceptable environment temperature values for "
        "the battery.",
    )
    expected_lifetime: Optional[ExpectedLifetime] = Field(
        None,
        title="Expected Lifetime",
        description="The details of the battery lifetime.",
    )
    material_composition: Optional[MaterialComposition] = Field(
        None,
        title="Material Composition",
        description="The details of the material composition of the battery.",
    )
    recycled_content: List[RecycledContent] = Field(
        ...,
        title="Recycled Content",
        description="The recycled content information present in the battery.",
    )
    renewable_content: List[RenewableContent] = Field(
        ...,
        title="Renewable Content",
        description="The renewable content information present in the battery.",
    )
    extinguishing_agents: List[str] = Field(
        ...,
        title="Extinguishing Agents",
        description="The type of the fire extinguishing agents that can be used for "
        "the battery.",
        examples=[["foam", "carbon dioxide"]],
    )
    legal_conformity: Optional[LegalConformity] = Field(
        None,
        title="Legal Conformity",
        description="The details of the conformity of the battery with the legal and "
        "harmonized standards.",
    )
    warranty: Optional[str] = Field(
        None,
        title="Warranty",
        description="The date when the battery warranty expires.",
        pattern=r"^\d{4}-(0[1-9]|1[0-2])$",
        examples=["2028-07"],
    )


class ManufacturingDataSheetRequest(CamelCaseModel):
    product: str = Field(
        ...,
        max_length=150,
        title="Product",
        description="The product code used for identifying the product type.",
        examples=["sodium-ion-75kWh"],
    )
    id: str = Field(
        ...,
        max_length=40,
        title="Id",
        description="The unique identifier of the product.",
        examples=["660e8400-e29b-41d4-a716-446655440000"],
    )


DEFINITION = DataProductDefinition(
    version="0.1.3",
    title="Battery Manufacturing Data Sheet",
    description="Manufacturing data sheet as required by Battery Passport "
    "specification of the European Commission's Battery Act (2023/1542).",
    tags=["Digital Product Passport", "Manufacturing"],
    request=ManufacturingDataSheetRequest,
    response=ManufacturingDataSheetResponse,
)
